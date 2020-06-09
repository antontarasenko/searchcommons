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
import os
import json
from urllib.parse import urlparse, quote
from urllib.request import urlopen

__author__ = 'Anton Tarasenko'
__email__ = 'antontarasenko@gmail.com'
__version__ = '0.1'

DATA_SOURCE_ENDPOINT = 'https://query.wikidata.org/sparql?format=json&query='
QUERY_FILE_NAME = 'query.rq'
RESPONSE_FILE_NAME = 'response.json'
REMOVALS = [
    'medium.com'    # The top level domain is not an established newspaper
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create or overwrite file "include.txt"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    args = parser.parse_args()

    if not os.path.isfile(RESPONSE_FILE_NAME):
        with open(QUERY_FILE_NAME, 'rt') as fh:
            encoded_query = quote(fh.read())
            data_request_url = DATA_SOURCE_ENDPOINT + encoded_query
        with urlopen(data_request_url) as req:
            if req.status != 200:
                print('Remote server error')
                exit(1)
            response_body = req.read().decode()
        with open(RESPONSE_FILE_NAME, 'wt') as fh:
            fh.write(response_body)

    domains = []
    with open(RESPONSE_FILE_NAME, 'rt') as fh:
        data = json.loads(fh.read())
        sort_key = lambda x: (x['inception']['value'], urlparse(x['website']['value']).netloc)
        for item in sorted(data['results']['bindings'], key=sort_key):
            website = item['website']['value']
            domain = urlparse(website).netloc
            domain = domain[4:] if domain.startswith('www.') else domain
            if domain in REMOVALS:
                continue
            else:
                domains.append('*.{}/*'.format(domain))

    with open('include.txt', 'wt') as fh:
        fh.write('\n'.join(domains))
