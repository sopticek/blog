#!/usr/bin/env python
#
# Author:   Daniela Ďuričeková <daniela.duricekova@gmail.com>
#


import array
import numpy
import pympler.asizeof
import texttable
import time

from symmetric_matrix import SymmetricMatrix as SM


N = 4000
EXPERIMENTS = 5


def create_array(size):
    return array.array("q", [0] * size)


def to_str_in_mb(size):
    return '{0:.2f} MB'.format(size / 1024 / 1024)


def to_str_in_sec(time):
    return '{0:.2f} sec'.format(time)


def benchmark_memory():
    # Get size of symmetric matrix that stores 64bit integers.
    sm_array = SM(N, create_array)
    size_sm_array = pympler.asizeof.asizeof(sm_array)

    # Get size of numpy matrix that stores 64bit integers.
    m_numpy = numpy.zeros((N, N), numpy.int64)
    size_m_numpy = pympler.asizeof.asizeof(m_numpy)

    # Print table with results.
    table = texttable.Texttable()
    table.set_deco(texttable.Texttable.BORDER |
                   texttable.Texttable.HEADER |
                   texttable.Texttable.VLINES)
    table.header(['Matrix Type', 'Memory Usage'])
    table.add_row([
        'Symmetric Matrix (via array)',
        to_str_in_mb(size_sm_array)
    ])
    table.add_row(['Numpy Matrix', to_str_in_mb(size_m_numpy)])
    print(table.draw())


def benchmark_access_time():
    # Get average access time for the symmetric matrix.
    sm_array = SM(N, create_array)
    time_sm_array_start = time.time()
    for experiment in range(EXPERIMENTS):
        for i in range(N):
            for j in range(N):
                sm_array[i, j] = experiment
    time_sm_array_end = time.time()
    time_sm_array = (time_sm_array_end - time_sm_array_start) / EXPERIMENTS

    # Get average access time for the numpy matrix.
    m_numpy = numpy.zeros((N, N), numpy.int64)
    time_m_numpy_start = time.time()
    for experiment in range(EXPERIMENTS):
        for i in range(N):
            for j in range(N):
                m_numpy[i, j] = experiment
    time_m_numpy_end = time.time()
    time_m_numpy = (time_m_numpy_end - time_m_numpy_start) / EXPERIMENTS

    # Print table with results.
    table = texttable.Texttable()
    table.set_deco(texttable.Texttable.BORDER |
                   texttable.Texttable.HEADER |
                   texttable.Texttable.VLINES)
    table.header(['Matrix Type', 'Access Time'])
    table.add_row([
        'Symmetric Matrix (via array)',
        to_str_in_sec(time_sm_array)
    ])
    table.add_row(['Numpy Matrix', to_str_in_sec(time_m_numpy)])
    print(table.draw())


def main():
    benchmark_memory()
    benchmark_access_time()


if __name__ == '__main__':
    main()
