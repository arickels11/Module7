import unittest
from topic_4.array_files import sort_and_search_array
import array as arr


class MyTestCase(unittest.TestCase):  # test for item found in array
    def test_search_array_in(self):
        tarray = arr.array('d', [1, 2, 3, 5, 4, 6])
        self.assertEqual(4, sort_and_search_array.search_array(tarray, 4))

    def test_search_array_not_in(self):  # test for item not found in array
        tarray = arr.array('d', [1, 2, 3, 5, 4, 6])
        self.assertEqual(-1, sort_and_search_array.search_array(tarray, 7))

    def test_sort_array(self):  # test sort function
        tarray = arr.array('d', [1, 2, 3, 5, 4, 6])
        self.assertEqual(('d', [1, 2, 3, 4, 5, 6]), sort_and_search_array.sort_array(tarray))


if __name__ == '__main__':
    unittest.main()
