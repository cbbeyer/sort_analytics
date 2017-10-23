#!/usr/bin/env python3
import time
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selection_sort import selectionSort
from native_sort import nativeSort

FILENAMES = [
    [ 'list1.txt', 'int'   ],
    [ 'list2.txt', 'int'   ],
    [ 'list3.txt', 'int'   ],
    [ 'list4.txt', 'int'   ],
    [ 'list5.txt', 'float' ],
    [ 'list6.txt', 'int'   ],
]

SORT_TYPE = [
    [ 'insertionSort', 'Insertion Sort'   ],
    [ 'bubbleSort',    'Bubble Sort'      ],
    [ 'selectionSort', 'Selection Sort'   ],
    [ 'nativeSort',    'Native Sort'      ],
]

# current_milli_time = lambda: int(round(time.time() * 1000))

class Result:
    def __init__(self, name, duration, nums):
        self.name = name
        self.duration = duration
        self.nums = nums
        self.relative = None


def main():

    for i in range(len(FILENAMES)):
        # Open and read in txt file
        results = []

        print(FILENAMES[i][0])
        for sti in range(len(SORT_TYPE)):

            sortType = globals()[SORT_TYPE[sti][0]]
            num_list = []
            list_of_lists = []

            with open(FILENAMES[i][0], 'r') as f:
                numbers = f.read().splitlines()

            for l in numbers:
                if FILENAMES[i][1] == 'int':
                    num_list.append(int(l))
                else:
                    num_list.append(float(l))

            # Copy list 1000 times
            for t in range(0, 1000):
                list_of_lists.append(num_list[:])

            # Get start time
            start_time = int(round(time.time() * 1000))

            # Sort lists
            for unsorted in list_of_lists:
                sorted_insertion = sortType(unsorted)

            # Get end time
            end_time = int(round(time.time() * 1000))
            total_time = (end_time - start_time)

            # Create result object
            result = Result(SORT_TYPE[sti][1], total_time, list_of_lists[0])
            results.append(result)

            # Sort results by duration
            results.sort(key=lambda x: x.duration, reverse=False)


        for r in results:
            print(r.name)
            print(r.duration)
            print(r.relative)
            print('First 10: {}'.format(r.nums[:10]))
            print('Last 10: {}'.format(r.nums[-10:]))
            print()

### Main runner ###
if __name__ == '__main__':
    main()
