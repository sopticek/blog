#!/usr/bin/env python
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#

from distutils.core import setup
from Cython.Build import cythonize


setup(
    name='Symmetric Matrix',
    ext_modules=cythonize('symmetric_matrix.pyx')
)
