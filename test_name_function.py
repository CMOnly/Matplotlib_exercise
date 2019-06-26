import unittest
from name_function import get_formateed_name


class NameTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        """can handle some name like zhao mei?"""
        formatted_name = get_formateed_name("zhao","meiqiu")
        self.assertEqual(formatted_name,'Zhao Meiqiu')


unittest.main()
