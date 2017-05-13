#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

from concurrent.futures import ProcessPoolExecutor


NUMS = list(range(25, 33))


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def n_fib(n):
    return n, fib(n)


if __name__ == '__main__':
    with ProcessPoolExecutor() as pool:
        results = pool.map(n_fib, NUMS)

    for result in results:
        print(result)
