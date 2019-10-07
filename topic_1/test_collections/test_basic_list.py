import unittest
from unittest.mock import patch
import topic_1.fun_with_collections.basic_list as basic_list


class TestList(unittest.TestCase):
    @patch('topic_1.fun_with_collections.basic_list.get_input', return_value='11')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [11, 11, 11])
