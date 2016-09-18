#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

import ctypes
import functools
import multiprocessing
import unittest

from symmetric_matrix import SymmetricMatrix as SM


class SymmetricMatrixTests(unittest.TestCase):
    def test_len_returns_correct_value(self):
        m = SM(3)
        self.assertEqual(len(m), 3)

    def test_values_are_zero_after_creation(self):
        m = SM(3)
        for x in range(3):
            for y in range(3):
                self.assertEqual(m[x, y], 0)

    def test_value_can_be_read_after_write(self):
        m = SM(3)
        m[0, 0] = 5
        self.assertEqual(m[0, 0], 5)

    def test_write_above_diagonal_does_not_write_to_invalid_index(self):
        m = SM(3)
        m[1, 2] = 5
        self.assertEqual(m[2, 0], 0)

    def test_write_to_x_y_writes_also_to_y_x(self):
        m = SM(3)
        m[1, 2] = 5
        self.assertEqual(m[2, 1], 5)

    def test_access_out_of_range_raises_exception(self):
        m = SM(3)
        with self.assertRaises(IndexError):
            m[3, 0] = 5

    def test_non_positive_size_raises_exception(self):
        with self.assertRaises(ValueError):
            SM(0)

    def test_can_pass_custom_create_storage(self):
        create_storage = functools.partial(
            multiprocessing.RawArray,
            ctypes.c_int
        )
        m = SM(3, create_storage)
        m[1, 2] = 5
        self.assertEqual(m[2, 1], 5)
