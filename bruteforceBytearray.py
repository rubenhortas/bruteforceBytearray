#!/usr/bin/env python
#_*_ coding: utf-8 _*_

"""
@file:       bruteforceBytearray.py
@author:     Rubén Hortas <rubenhortas@gmail.com>
@website:    http://rubenhortas.blogspot.com.es
@github:     http://github.com/rubenhortas/bruteforceBytearray
@license:    unlicensed
@file:       bruteforceBytearray.py
"""

def print_array(array):
    array_tmp = ''
    for element in array:
        array_tmp =  array_tmp + '[' + str(element) +']'
    print array_tmp

def inc_cell(array, position, min_range, max_range):
    for i in range(min_range, max_range):
        array[position] = i
        print_array(array)

def inc_array(array, current_position, min_range, max_range):
    if current_position == (len(array) -1):
            inc_cell(array, current_position, min_range, max_range)
    else:
        for i in range(min_range,max_range):
            array[current_position] = i
            inc_array(array, (current_position + 1), min_range, max_range)


if __name__ == '__main__':
    array_size = 3
    min_range = 0
    max_range = 10
    array = bytearray(array_size)
    inc_array(array, 0, min_range, max_range)
