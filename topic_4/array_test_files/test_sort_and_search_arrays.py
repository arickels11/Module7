import unittest
from topic_4.array_files import sort_and_search_array
import array as arr


class MyTestCase(unittest.TestCase):
    def test_search_array_in(self):
        self.assertEqual(3, sort_and_search_array.search_array([1, 2, 3, 5, 4, 6], 4))

    def test_search_array_not_in(self):
        self.assertEqual(-1, sort_and_search_array.search_array([1, 2, 3, 5, 4, 6], 7))


if __name__ == '__main__':
    unittest.main()
