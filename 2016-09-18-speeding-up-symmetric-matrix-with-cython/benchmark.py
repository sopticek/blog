#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import array
import numpy
import texttable
import time

from symmetric_matrix import SymmetricMatrix as SM
from symmetric_matrix_python import SymmetricMatrix as SMP

N = 4000
EXPERIMENTS = 5


def create_array(size):
    return array.array("q", [0] * size)


def to_str_in_sec(time):
    return '{0:.2f} sec'.format(time)


def _experiment(matrix):
    start = time.time()
    for e in range(EXPERIMENTS):
        for i in range(N):
            for j in range(N):
                matrix[i, j] = e
    end = time.time()
    avg_time = (end - start) / EXPERIMENTS
    return avg_time


def benchmark_access_time():
    python_matrix = SMP(N, create_array)
    cython_matrix = SM(N, create_array)
    numpy_matrix = numpy.zeros((N, N), numpy.int64)

    # Print table with results.
    table = texttable.Texttable()
    table.set_deco(texttable.Texttable.BORDER |
                   texttable.Texttable.HEADER |
                   texttable.Texttable.VLINES)
    table.header(['Matrix Type', 'Access Time'])
    table.add_row([
        'Symmetric Matrix (Python version)',
        to_str_in_sec(_experiment(python_matrix))
    ])
    table.add_row([
        'Symmetric Matrix (Cython version)',
        to_str_in_sec(_experiment(cython_matrix))
    ])
    table.add_row([
        'Numpy Matrix',
        to_str_in_sec(_experiment(numpy_matrix))
    ])
    print(table.draw())


def main():
    benchmark_access_time()


if __name__ == '__main__':
    main()
