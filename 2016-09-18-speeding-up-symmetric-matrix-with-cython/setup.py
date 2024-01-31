#!/usr/bin/env python
#
# Author:   Daniela Ďuričeková <daniela.duricekova@protonmail.com>
#

from distutils.core import setup
from Cython.Build import cythonize


setup(
    name='Symmetric Matrix',
    ext_modules=cythonize('symmetric_matrix.pyx')
)
