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
Palo Alto Networks testcases.py

Defines parameters for the test. 

Include this file; do not run it directly.

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''

class ParseTest():
    def __init__(self):
        # Static version notes metadata
        self.version = '3026-3536'
        self.version_date = '2019-07-01T04:00:52-07:00'

        # If we process this much or more, we pass
        self.percent_processed = 0.5


        # Establish cases to check are in the database.
        self.cases = [{'raw': 'None:gacyqob.com', 'action': 'added'},
                      {'raw': 'Backdoor.simda:gahyraw.com', 'action': 'added'},
                      {'raw': 'None:pupycag.com', 'action': 'added'},
                      {'raw': 'PWS.simda:qetyhyg.com', 'action': 'added'},
                      {'raw': 'Backdoor.simda:vojykom.com', 'action': 'added'},
                      {'raw': 'Backdoor.simda:vowygem.com', 'action': 'added'},
                      {'raw': 'None:vowyzuk.com', 'action': 'added'},
                      {'raw': 'Worm.pykspa:agadss.biz', 'action': 'added'},
                      {'raw': 'Worm.pykspa:qgasocuiwcymao.info', 'action': 'added'},
                      {'raw': 'Worm.pykspa:ygsink.info', 'action': 'added'},
                      {'raw': 'Worm.ainslot:ryan12345.no-ip.biz', 'action': 'added'},
                      {'raw': 'TrojanDownloader.upatre:hngdecor.com', 'action': 'added'},
                      {'raw': 'TrojanDownloader.upatre:okeanbg.com', 'action': 'added'},
                      {'raw': 'TrojanDownloader.upatre:gert-hof.de', 'action': 'added'},
                      {'raw': 'Packed.fe:spaines.pw', 'action': 'added'},
                      {'raw': 'None:recdataoneveter.cc', 'action': 'added'},
                      {'raw': 'Backdoor.vawtrak:mbbllmv.eu', 'action': 'removed'},
                      {'raw': 'None:mfkxyucmxwhw.com', 'action': 'removed'},
                      {'raw': 'Worm.pykspa:kegbceiq.info', 'action': 'removed'},
                      {'raw': 'Virus.gippers:microsoft.mypicture.info', 'action': 'removed'},
                      {'raw': 'DDoS.nitol:a7677767.vicp.net', 'action': 'removed'},
                      {'raw': 'Worm.pykspa:yeuawkuiwcymao.info', 'action': 'removed'},
                      {'raw': 'None:zief.pl', 'action': 'removed'},
                      {'raw': 'Virus.palevogen:.banjalucke-ljepotice.ru', 'action': 'removed'},
                      {'raw': 'VirTool.ceeinject:digitalmind.cn', 'action': 'removed'},
                      {'raw': 'Virus.virut:irc.zief.pl', 'action': 'removed'},
                      {'raw': 'Trojan.dorv:lyvyxor.com', 'action': 'removed'},
                      {'raw': 'Virus.sality:sungkhomwit.com', 'action': 'removed'},
                      {'raw': 'Virus.sality:asesoriaenexposicion.com', 'action': 'removed'},
                      {'raw': 'TrojanSpy.nivdort:doubledistant.net', 'action': 'removed'},
                      {'raw': 'None:extsc.3322.org', 'action': 'removed'},
                      {'raw': 'Virus.sality:solitaireinfo.com', 'action': 'removed'}]
