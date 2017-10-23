#!/usr/bin/env python3

def selectionSort(num_list):
    '''Sorts list of word objects based on count in book'''
    for i in range(len(num_list)-1):
        min_index = i

        for t in range(i+1, len(num_list)):
            if num_list[t] < num_list[min_index]:
                min_index = t
        if min_index != i:
            num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list
