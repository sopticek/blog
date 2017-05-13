#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import requests
from multiprocessing.pool import ThreadPool
# alternative:
# from multiprocessing.dummy import Pool as ThreadPool

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
    with ThreadPool() as pool:
        results = pool.map(get_content_len, URLS)

    for result in results:
        print(result)
