import unittest
from topic_4.array_files import sort_and_search_array
import array as arr


class MyTestCase(unittest.TestCase):  # test for item found in array
    def test_search_array_in(self):
        self.assertEqual(4, sort_and_search_array.search_array([1, 2, 3, 5, 4, 6], 4))

    def test_search_array_not_in(self):  # test for item not found in array
        self.assertEqual(-1, sort_and_search_array.search_array([1, 2, 3, 5, 4, 6], 7))

    def test_sort_array(self):  # test sort function
        self.assertEqual([1, 2, 3, 4, 5, 6], sort_and_search_array.sort_array([1, 2, 3, 5, 4, 6]))


if __name__ == '__main__':
    unittest.main()
