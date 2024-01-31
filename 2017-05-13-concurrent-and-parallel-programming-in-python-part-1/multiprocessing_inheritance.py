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


class FibProcess(multiprocessing.Process):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = multiprocessing.Value('L')

    def run(self):
        self.result.value = fib(self.n)


if __name__ == '__main__':
    processes = []
    for n in NUMS:
        p = FibProcess(n)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for p in processes:
        print((p.n, p.result.value))
