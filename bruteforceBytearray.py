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


def print_array(a):
    array_tmp = ''
    for element in a:
        array_tmp = array_tmp + '[' + str(element) + ']'
    print array_tmp


def inc_cell(arr, position, min, max):
    for i in range(min, max):
        arr[position] = i
        print_array(arr)


def inc_array(a, current_position, min, max):
    if current_position == (len(a) - 1):
        inc_cell(a, current_position, min, max)
    else:
        for i in range(min, max):
            a[current_position] = i
            inc_array(a, (current_position + 1), min, max)


if __name__ == '__main__':
    array_size = 3
    min_range = 0
    max_range = 10
    array = bytearray(array_size)
    inc_array(array, 0, min_range, max_range)
