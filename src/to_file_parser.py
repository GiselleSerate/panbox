# Copyright (c) 2019, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Author: Giselle Serate <gserate@paloaltonetworks.com>

'''
Palo Alto Networks to_file_parser.py

Downloads and parses the latest release notes off a PANW firewall, writing them to a file.

Run independently of all other files in this repository; not designed to be imported.
Make sure to configure your .panrc.

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''


import logging
from logging.config import dictConfig
import os
from threading import Thread
import re

from bs4 import BeautifulSoup
from dotenv import load_dotenv

from scraper import FirewallScraper



home = os.getenv('HOME')
dot = os.getenv('PWD')
env_path = os.path.join(dot, 'src', 'lib', '.defaultrc')
load_dotenv(dotenv_path=env_path, verbose=True)
env_path = os.path.join(home, '.panrc')
load_dotenv(dotenv_path=env_path, verbose=True, override=True)


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': os.getenv('LOGGING_LEVEL'),
        'handlers': ['wsgi']
    }
})



def next_path(path_prefix, extension):
    '''
    Finds the next free path in an sequentially named list of files

    path_prefix -- the beginning of the path, up to the varied part of the filename
    extension -- txt, or csv, or some file extension; don't put the period
    '''
    seq_no = 0
    while os.path.exists(f"{path_prefix}{seq_no}.{extension}"):
        seq_no += 1
    return f"{path_prefix}{seq_no}.{extension}"


def parse(soup, pattern, array):
    '''
    Pulls all domains of one type from the soup and then writes them to the array.

    Keyword arguments:
    soup -- the soup to parse
    pattern -- the section header pattern to find in the soup
    array -- the array to put items in after they have been parsed
    '''
    # Pull out a list of tds from parse tree
    try:
        header = soup.find('h3', text=pattern)
        tds = header.find_next_sibling('table').find_all('td')

        # Get domains from table entries
        for td in tds:
            raw_scrape = td.string
            # Extract domains from "Suspicious DNS Query" parentheses
            result = re.search(r'\((.*)\)', raw_scrape)
            if result is None:
                array.append(raw_scrape.split(':')[1])
            else:
                array.append(result.group(1).split(':')[1])

    except Exception as e:
        logging.error(f"Parse of failed. "
                      "Are you sure this HTML file is the right format?")
        logging.error(e)
        # If we can't parse out domains, this suggests a fundamental document
        # format change requiring more maintenance than a simple retry. Get a human to look at this.
        raise e



if __name__ == '__main__':
    # If the number of domains requested is not a number, output all the domains.
    try:
        num_output = int(os.getenv('NUM_DOMAINS_OUTPUT'))
    except ValueError:
        num_output = None

    scraper = FirewallScraper(ip=os.getenv('FW_IP'), username=os.getenv('FW_USERNAME'),
                              password=os.getenv('FW_PASSWORD'),
                              chrome_driver=os.getenv('DRIVER'),
                              binary_location=os.getenv('BINARY_LOCATION'),
                              download_dir=os.getenv('DOWNLOAD_DIR'))
    scraper.latest_download()

    # Domains get stored here
    all_domains = []

    path = f"{os.getenv('DOWNLOAD_DIR')}/Updates_{scraper.versions[0]['version']}.html"

    try:
        data = open(path)
    except Exception as e:
        logging.error(f"Issue opening provided file at {path}.")
        raise e # Reraise so the script stops

    # Parse file
    soup = BeautifulSoup(data, 'html5lib')


    # Start threads for adds and removes
    # Note that we don't actually care which is which; we're just parallelizing cause we can.
    added_thread = Thread(target=parse,
                          args=(soup, re.compile(os.getenv('ADD_REGEX')),
                                all_domains))
    added_thread.start()
    removed_thread = Thread(target=parse,
                            args=(soup, re.compile(os.getenv('REM_REGEX')),
                                  all_domains))
    removed_thread.start()
    added_thread.join()
    removed_thread.join()

    # Write both added and removed arrays to file.
    write_path = next_path(f"{os.getenv('PARSED_DIR')}/Parsed_", "txt")
    try:
        outfile = open(write_path, 'x')
    except Exception as e:
        logging.error(f"Issue creating a new file as {write_path}.")
        raise e

    for domain in all_domains[:num_output]:
        outfile.write(f"{domain}\n")

    outfile.close()
    logging.info(f"Finished running. Find your new file at {write_path}.")
