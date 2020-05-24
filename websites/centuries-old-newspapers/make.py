#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*****
Usage
*****

Run this script with the parameter ``--help/-h``::

    python3 __PATH_TO_SCRIPT__ --help

"""
import argparse
import csv
import os
from urllib.parse import urlparse

__author__ = 'Anton Tarasenko'
__email__ = 'antontarasenko@gmail.com'
__version__ = '0.1'

DATA_SOURCE_FILE_NAME = 'query.tsv'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create or overwrite file "include.txt"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    args = parser.parse_args()

    if not os.path.isfile(DATA_SOURCE_FILE_NAME):
        print(DATA_SOURCE_FILE_NAME, 'not found. Check local README.md')
        exit(1)

    domains = []
    with open(DATA_SOURCE_FILE_NAME, 'rt') as fh:
        reader = csv.reader(fh, delimiter='\t')
        next(reader)  # headers
        for row in reader:
            website = row[4]
            domain = urlparse(website).netloc
            domain = domain[4:] if domain.startswith('www.') else domain
            domain = '*.{}/*'.format(domain)
            domains.append(domain)

    with open('include.txt', 'wt') as fh:
        fh.write('\n'.join(domains))
