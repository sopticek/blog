#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import requests
import threading


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


class ContentLenThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.content_len = None

    def run(self):
        r = requests.get(self.url)
        self.content_len = len(r.text)


if __name__ == '__main__':
    threads = []
    for url in URLS:
        t = ContentLenThread(url)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for t in threads:
        print((t.url, t.content_len))
