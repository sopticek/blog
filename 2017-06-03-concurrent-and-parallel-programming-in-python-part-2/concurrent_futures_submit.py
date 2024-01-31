#!/usr/bin/env python
#
# Author:   Daniela Ďuričeková <daniela.duricekova@protonmail.com>
#

import concurrent.futures
import multiprocessing


def ackermann(m, n):
    assert m >= 0 and n >= 0
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    tasks = multiprocessing.Queue()
    tasks.put((fib, 8))
    tasks.put((ackermann, 2, 4))
    tasks.put((fib, 18))
    tasks.put((ackermann, 3, 1))
    tasks.put((fib, 28))
    tasks.put((ackermann, 3, 4))
    tasks.put((fib, 34))
    tasks.put(None)

    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        while True:
            task = tasks.get()
            if task is None:
                break
            func, *args = task
            result = pool.submit(func, *args)
            results.append((func.__name__, args, result))

        for func_name, args, result in results:
            result = result.result()
            args = ', '.join(str(arg) for arg in args)
            print('{}({}) = {}'.format(func_name, args, result))
