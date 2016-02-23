#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
@file:       bruteforceBytearray.py
@author:     Rubén Hortas <rubenhortas@gmail.com>
@website:    http://rubenhortas.blogspot.com.es
@github:     http://github.com/rubenhortas/bruteforceBytearray
@license:    unlicensed
@file:       bruteforceBytearray.py
"""


def print_array(arr):
    print ''.join('[{0}]'.format(element) for element in arr)


def inc_cell(arr, position, minimum, maximum):
    for i in range(minimum, maximum):
        arr[position] = i
        print_array(arr)


def inc_array(arr, current_position, minimum, maximum):
    if current_position == array_max_position:
        inc_cell(arr, current_position, minimum, maximum)
    else:
        for i in range(minimum, maximum):
            arr[current_position] = i
            inc_array(arr, (current_position + 1), minimum, maximum)


if __name__ == '__main__':
    array_size = 3
    array_max_position = array_size - 1
    min_range = 0
    max_range = 10
    array = bytearray(array_size)
    inc_array(array, 0, min_range, max_range)
