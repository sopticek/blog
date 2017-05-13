#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import multiprocessing


NUMS = list(range(25, 33))


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def n_fib(n, results):
    results.put((n, fib(n)))


if __name__ == '__main__':
    results = multiprocessing.Queue()
    processes = []
    for n in NUMS:
        p = multiprocessing.Process(target=n_fib, args=(n, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for _ in range(len(NUMS)):
        print(results.get())
