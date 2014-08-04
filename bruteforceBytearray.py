#!/usr/bin/env python
#_*_ coding: utf-8 _*_

"""
@file:       bruteforceBytearray.py
@author:     Rubén Hortas <rubenhortas@gmail.com>
@website:    http://rubenhortas.blogspot.com.es
@github:     http://github.com/rubenhortas/bruteforceBytearray
@license:    unlicensed
"""

def print_array(array):
    array_tmp = ''
    for element in array:
        array_tmp =  array_tmp + '[' + str(element) +']'
    print array_tmp

def inc_cell(barray, position, min_range, max_range):
    for i in range(min_range, max_range):
        barray[position] = i
        print_array(barray)

def inc_array(barray, current_position, min_range, max_range):
    if current_position == (len(barray) -1):
            inc_cell(barray, current_position, min_range, max_range)
    else:
        for i in range(min_range,max_range):
            barray[current_position] = i
            inc_array(barray, (current_position + 1), min_range, max_range)


if __name__ == '__main__':
    array_size = 3
    min_range = 0
    max_range = 10
    b_array = bytearray(array_size)
    inc_array(b_array, 0, min_range, max_range)
