#!/usr/bin/env python
#
# Author:   Daniela Ďuričeková <daniela.duricekova@protonmail.com>
#

import multiprocessing

from datetime import datetime


NUMS = [(i, j) for i in range(4) for j in range(5)]


def ackermann(m, n):
    assert m >= 0 and n >= 0
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        results = pool.starmap(ackermann, NUMS)
        for n, result in zip(NUMS, results):
            print('{} {} {}'.format(datetime.now().time(), n, result))
