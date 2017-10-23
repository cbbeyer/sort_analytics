#!/usr/bin/env python3

def bubbleSort(num_list):
    '''Sorts list of word objects based on count in book'''
    for i in range(len(num_list) - 1):
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list
