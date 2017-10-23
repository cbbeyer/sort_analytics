#!/usr/bin/env python3

def insertionSort(num_list):
    '''Sorts list of word objects based on count in book'''
    for i in range(1, len(num_list)):
        j = i - 1
        while num_list[j] >= num_list[j+1] and j >= 0:
            if num_list[j] != num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            j -= 1
    return num_list
