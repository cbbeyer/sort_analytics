#!/usr/bin/env python3
import sys
import time
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selection_sort import selectionSort
from native_sort import nativeSort
from quick_sort import quickSort

FILENAMES = [
    [ 'list1.txt', 'int'   , 'list1.txt'         ],
    [ 'list2.txt', 'int'   , 'Powers of 2'       ],
    [ 'list3.txt', 'int'   , 'list3.txt'         ],
    [ 'list4.txt', 'int'   , 'Fibonacci Sequence'],
    [ 'list5.txt', 'float' , 'list5.txt'         ],
    [ 'list6.txt', 'int'   , 'list6.txt'         ],
]

SORT_TYPE = [
    [ 'insertionSort', 'Insertion Sort'     ],
    [ 'bubbleSort'   , 'Bubble Sort'        ],
    [ 'selectionSort', 'Selection Sort'     ],
    [ 'nativeSort'   , 'Native LanguageSort'],
    [ 'quickSort'    , 'Quicksort'          ],
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

        print(FILENAMES[i][2])
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
            start_time = time.time()

            # Sort lists
            for unsorted in list_of_lists:
                sorted_insertion = sortType(unsorted)

            # Get end time
            end_time = time.time()
            total_time = (end_time - start_time)

            # Create result object
            result = Result(SORT_TYPE[sti][1], total_time, list_of_lists[0])
            results.append(result)

            for i_res in range(len(results)):
                if i_res == 0:
                    results[i_res].relative = 0
                else:
                    results[i_res].relative = (results[i_res].duration - results[0].duration)/results[0].duration


            # Sort results by duration
            results.sort(key=lambda x: x.duration, reverse=False)


        for r in results:
            print(r.name)
            print('{0:.6f}'.format(r.duration))
            print('{}{}'.format(int(round(r.relative, 2)),'%'))
            print('First 10: {}'.format(', '.join(str(v) for v in r.nums[:10])))
            print('Last 10: {}'.format(', '.join(str(v) for v in r.nums[-10:])))
            print()

### Main runner ###
with open('output.txt', 'w') as f:
    orig_stdout = sys.stdout
    sys.stdout = f
    if __name__ == '__main__':
        main()
    sys.stdout = orig_stdout

# if __name__ == '__main__':
#     main()
