#!/usr/bin/env python
#
# Author:   Daniela Ďuričeková <daniela.duricekova@protonmail.com>
#

import requests


URLS = [
    'https://xkcd.com/138/',
    'https://xkcd.com/149/',
    'https://xkcd.com/285/',
    'https://xkcd.com/303/',
    'https://xkcd.com/327/',
    'https://xkcd.com/387/',
    'https://xkcd.com/612/',
    'https://xkcd.com/648/'
]


def get_content_len(url):
    r = requests.get(url)
    return url, len(r.text)


if __name__ == '__main__':
    for url in URLS:
        result = get_content_len(url)
        print(result)
