#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import concurrent.futures

from datetime import datetime


NUMS = list(range(1, 40))


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        results = pool.map(fib, NUMS)
        for n, result in zip(NUMS, results):
            print('{} {:>3} {:>10}'.format(datetime.now().time(), n, result))
