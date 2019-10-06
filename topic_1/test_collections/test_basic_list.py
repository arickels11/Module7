import unittest
from unittest.mock import patch
from topic_1.fun_with_collections import basic_list


class MyTestCase(unittest.TestCase):
    @patch(basic_list.get_input, return_value='11')
    def test_list(self, input):
        self.assertEqual(basic_list.get_input, [11, 11, 11])


if __name__ == '__main__':
    unittest.main()
