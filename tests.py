import unittest
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selection_sort import selectionSort
from native_sort import nativeSort
from quick_sort import quickSort

# python3 -m unittest tests.py
class SortTesting(unittest.TestCase):
    def test_create_array(self):
        arr = [1,3,2,5,7,8,9,4,3,2,14,46,2,4,1234,23,4511,24,1234,234,52,534645,67,45687,4578]
        return arr

    def test_create_array2(self):
        arr2 = [1,3,2,5,7,8,9,4,3,2,14,46,2,4,1234,23,4511,24,1234,234,52,534645,67,45687,4578,2,3,4,24,345,6,4567,2345,234,52,345,2345,2345,2345,2345,2345,123,5]
        return arr2



    # BUBBLE SORT
    def test_bubbleSort_array(self):
        arr = self.test_create_array()
        sorted_arr = bubbleSort(arr)

        self.assertEqual(sorted_arr[0], 1)

    def test_bubbleSort_array_last_val(self):
        arr = self.test_create_array()
        sorted_arr = bubbleSort(arr)

        self.assertEqual(sorted_arr[3], 2)

    def test_bubbleSort_fail(self):
        arr = self.test_create_array()
        sorted_arr = bubbleSort(arr)

        self.assertEqual(sorted_arr[7], 1)



    # SELECTION SORT
    def test_selectionSort_array(self):
        arr = self.test_create_array()
        sorted_arr = selectionSort(arr)

        self.assertEqual(sorted_arr[0], 1)

    def test_selectionSort_array_last_val(self):
        arr = self.test_create_array()
        sorted_arr = selectionSort(arr)

        self.assertEqual(sorted_arr[3], 2)

    def test_selectionSort_fail(self):
        arr = self.test_create_array()
        sorted_arr = selectionSort(arr)

        self.assertEqual(sorted_arr[7], 1)


    # INSERTION SORT
    def test_insertionSort_array(self):
        arr = self.test_create_array()
        sorted_arr = insertionSort(arr)

        self.assertEqual(sorted_arr[0], 1)

    def test_insertionSort_array_last_val(self):
        arr = self.test_create_array()
        sorted_arr = insertionSort(arr)

        self.assertEqual(sorted_arr[3], 2)

    def test_insertionSort_fail(self):
        arr = self.test_create_array()
        sorted_arr = insertionSort(arr)

        self.assertEqual(sorted_arr[7], 1)



    # NATIVE SORT
    def test_nativeSort_array(self):
        arr = self.test_create_array()
        sorted_arr = bubbleSort(arr)

        self.assertEqual(sorted_arr[0], 1)

    def test_nativeSort_array_last_val(self):
        arr = self.test_create_array()
        sorted_arr = bubbleSort(arr)

        self.assertEqual(sorted_arr[3], 2)

    def test_nativeSort_fail(self):
        arr = self.test_create_array()
        sorted_arr = insertionSort(arr)

        self.assertEqual(sorted_arr[7], 1)


    # QUICK SORT
    def test_quickSort_array(self):
        arr = self.test_create_array()
        sorted_arr = quickSort(arr)

        self.assertEqual(sorted_arr[0], 1)

    def test_quickSort_array_last_val(self):
        arr = self.test_create_array()
        sorted_arr = quickSort(arr)

        self.assertEqual(sorted_arr[3], 2)

    def test_quickSort_fail(self):
        arr = self.test_create_array()
        sorted_arr = insertionSort(arr)

        self.assertEqual(sorted_arr[7], 1)
