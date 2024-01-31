#!/usr/bin/env python
#
# Author:   Daniela Ďuričeková <daniela.duricekova@protonmail.com>
#

import multiprocessing


NUMS = list(range(25, 33))


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for n in NUMS:
        result = fib(n)
        print((n, result))
