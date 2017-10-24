#!/usr/bin/env python3

def quickSort(num_list):
        ARRAY_LENGTH = len(num_list)
        if( ARRAY_LENGTH <= 1):
            return num_list
        else:
            PIVOT = num_list[0]
            GREATER = [ element for element in num_list[1:] if element > PIVOT ]
            LESSER = [ element for element in num_list[1:] if element <= PIVOT ]
            return quickSort(LESSER) + [PIVOT] + quickSort(GREATER)
