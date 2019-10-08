import unittest
from unittest.mock import patch
import topic_1.fun_with_collections.basic_list as basic_list
import topic_2.fun_with_collections.basic_list_exception as basic_list_exception


class TestList(unittest.TestCase):
    @patch('topic_1.fun_with_collections.basic_list.get_input', return_value='11')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [11, 11, 11])

    @patch('topic_2.fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()

    @patch('topic_2.fun_with_collections.basic_list_exception.get_input', return_value='-1')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()

    @patch('topic_2.fun_with_collections.basic_list_exception.get_input', return_value='51')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


if __name__ == '__main__':
    unittest.main()
