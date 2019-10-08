import unittest
from topic_1.fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    def test_search_list_in(self):
        self.assertEqual(3, sort_and_search_list.search_list([1, 4, 6, 8, 10], 8))

    def test_search_list_not(self):
        self.assertEqual(-1, sort_and_search_list.search_list([1, 4, 6, 8, 10], 7))


if __name__ == '__main__':
    unittest.main()
