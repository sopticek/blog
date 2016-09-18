# cython: language_level=3
#
# Author:   Daniela Duricekova <daniela.duricekova@gmail.com>
#


cdef class SymmetricMatrix:
    cdef:
        int _size
        int _data_size
        object _data

    def __init__(self, size, create_storage=None):
        if size <= 0:
            raise ValueError('size has to be positive')

        self._data_size = (size + 1) * size // 2

        if create_storage is None:
            create_storage = lambda n: [0 for i in range(n)]

        self._size = size
        self._data = create_storage(self._data_size)

    def __len__(self):
        return self._size

    def __setitem__(self, position, value):
        cdef int index

        index = self._get_index(position)
        if index < 0 or index >= self._data_size:
            raise IndexError('out of bounds')

        self._data[index] = value

    def __getitem__(self, position):
        cdef int index

        index = self._get_index(position)
        if index < 0 or index >= self._data_size:
            raise IndexError('out of bounds')

        return self._data[index]

    cdef int _get_index(self, position):
        cdef int row, column, index

        row, column = position
        if column > row:
            row, column = column, row

        index = (row) * (row + 1) // 2 + column

        return index
