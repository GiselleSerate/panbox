#!/bin/bash
printf "Waiting for ELK.\n"
while ! nc -z elk 9200; do sleep 1; done
printf "Done waiting for ELK.\n"