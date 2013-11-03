#!/usr/bin/env python
#_*_ coding: utf-8 _*_

"""
@file:       pdfMetadata.py
@author:     Rubén Hortas <rubenhortas@gmail.com>
@website:    http://rubenhortas.blogspot.com.es
@github:     http://github.com/rubenhortas/bruteforceBytearray
@license:    unlicensed
"""

def Print_array(array):
    array_tmp = ''
    for el in array:
        array_tmp =  array_tmp + '[' + str(el) +']'
    print array_tmp

def Inc_cell(b_array, pos):
    for i in range(0, 156):
        b_array[pos] = i
        Print_array(b_array)

def Inc_array(b_array, array_len, actual_pos):
    if actual_pos == array_len:
            Inc_cell(b_array, actual_pos)
    else:
        for pos_actual in range(actual_pos, array_len):
            for j in range(0, 256):
                b_array[actual_pos] = j
                Inc_array(b_array, array_len, (actual_pos+1))

if __name__ == '__main__':
    array_size = 3
    array_len = (array_size - 1)
    b_array = bytearray(array_size)

    Inc_array(b_array, array_len, 0)
