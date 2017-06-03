#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import multiprocessing

from datetime import datetime


NUMS = list(reversed(range(1, 40)))


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        results = pool.imap(fib, NUMS, chunksize=1)
        for n, result in zip(NUMS, results):
            print('{} {:>3} {:>10}'.format(datetime.now().time(), n, result))
