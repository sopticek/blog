#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import requests
import threading
import queue


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


def get_content_len(url, results):
    r = requests.get(url)
    results.put((url, len(r.text)))


if __name__ == '__main__':
    results = queue.Queue()
    threads = []
    for url in URLS:
        t = threading.Thread(target=get_content_len, args=(url, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    while not results.empty():
        print(results.get())
