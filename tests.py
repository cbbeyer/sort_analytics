import unittest
from bubble_sort import bubbleSort
from worddata import WordData
from insertion_sort import insertionSort
from selection_sort import selectionSort
from merge_api import merge_lists
from main_api import print_words

# python3 -m unittest tests.py
class SortTesting(unittest.TestCase):
    def test_create_WordData_array(self):
        words = []
        w1 = WordData('1 Nephi', 'm', 7, 7)
        words.append(w1)
        w1 = WordData('1 Nephi', 'd', 3, 3)
        words.append(w1)
        w1 = WordData('1 Nephi', 'a', 1, 1)
        words.append(w1)
        w1 = WordData('1 Nephi', 'e', 4, 4)
        words.append(w1)
        w1 = WordData('1 Nephi', 'h', 6, 6)
        words.append(w1)
        w1 = WordData('1 Nephi', 'i', 6, 6)
        words.append(w1)
        w1 = WordData('1 Nephi', 'k', 6, 6)
        words.append(w1)
        w1 = WordData('1 Nephi', 'c', 2, 2)
        words.append(w1)

        return words

    def test_create_WordData_array2(self):
        words2 = []

        w1 = WordData('4 Nephi', 'b', 1, 1)
        words2.append(w1)
        w1 = WordData('4 Nephi', 'o', 9, 9)
        words2.append(w1)
        w1 = WordData('1 Nephi', 'j', 6, 6)
        words2.append(w1)
        w1 = WordData('1 Nephi', 'g', 6, 6)
        words2.append(w1)
        w1 = WordData('4 Nephi', 'n', 8, 8)
        words2.append(w1)
        w1 = WordData('4 Nephi', 'l', 7, 7)
        words2.append(w1)
        w1 = WordData('4 Nephi', 'f', 5, 5)
        words2.append(w1)

        return words2


    # BUBBLE SORT
    def test_bubbleSort_array(self):
        words = self.test_create_WordData_array()
        sorted_words = bubbleSort(words)

        self.assertEqual(sorted_words[0].word, 'a')

    def test_bubbleSort_array_last_val(self):
        words = self.test_create_WordData_array()
        sorted_words = bubbleSort(words)

        self.assertEqual(sorted_words[7].word, 'm')

    def test_bubbleSort_fail(self):
        words = self.test_create_WordData_array()
        sorted_words = bubbleSort(words)

        self.assertEqual(sorted_words[7].word, 'h')



    # SELECTION SORT
    def test_selectionSort_array(self):
        words = self.test_create_WordData_array()
        sorted_words = selectionSort(words)

        self.assertEqual(sorted_words[0].word, 'a')

    def test_selectionSort_array_last_val(self):
        words = self.test_create_WordData_array()
        sorted_words = selectionSort(words)

        self.assertEqual(sorted_words[7].word, 'm')

    def test_selectionSort_fail(self):
        words = self.test_create_WordData_array()
        sorted_words = selectionSort(words)

        self.assertEqual(sorted_words[7].word, 'l')



    # INSERTION SORT
    def test_insertionSort_array(self):
        words = self.test_create_WordData_array()
        sorted_words = insertionSort(words)

        self.assertEqual(sorted_words[0].word, 'a')

    def test_insertionSort_array_last_val(self):
        words = self.test_create_WordData_array()
        sorted_words = insertionSort(words)

        self.assertEqual(sorted_words[7].word, 'm')

    def test_insertionSort_fail(self):
        words = self.test_create_WordData_array()
        sorted_words = insertionSort(words)

        self.assertEqual(sorted_words[7].word, 'f')

    # MERGING TWO LISTS TOGETHER
    def test_merge_two_lists(self):
        words = self.test_create_WordData_array()
        words2 = self.test_create_WordData_array2()

        sorted_words = selectionSort(words)
        sorted_words2 = selectionSort(words2)

        merged_list = merge_lists(sorted_words, sorted_words2)

        self.assertEqual(merged_list[1].word, 'b')

    def test_merge_two_lists_last_val_fail(self):
        words = self.test_create_WordData_array()
        words2 = self.test_create_WordData_array2()

        sorted_words = selectionSort(words)
        sorted_words2 = selectionSort(words2)

        merged_list = merge_lists(sorted_words, sorted_words2)

        self.assertEqual(merged_list[14].word, 'l')

    def test_merge_two_lists_first_val(self):
        words = self.test_create_WordData_array()
        words2 = self.test_create_WordData_array2()

        sorted_words = selectionSort(words)
        sorted_words2 = selectionSort(words2)

        merged_list = merge_lists(sorted_words, sorted_words2)

        self.assertEqual(merged_list[14].word, 'o')



    # CREATING WORD DATA object
    def test_create_wordData_object(self):
        word_data = WordData('1 Nephi', 'the', '209', '5')

        self.assertEqual(word_data.book, '1 Nephi')
