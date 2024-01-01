import unittest
from unittest.mock import patch
from io import StringIO
from ccwc import (open_file_and_count_bytes, open_file_and_count_lines,
                  open_file_and_count_words, open_file_and_count_chars)


class TestWCTool(unittest.TestCase):
    def setUp(self):
        pass

    @patch('builtins.open', return_value=StringIO("Line 1\nLine 2\nLine 3"))
    def test_open_file_and_count_lines(self, filename):
        result = open_file_and_count_lines(filename)
        self.assertEqual(result, 3)

    @patch('builtins.open', return_value=StringIO("This is a test"))
    def test_open_file_and_count_words(self, filename):
        result = open_file_and_count_words(filename)
        self.assertEqual(result, 4)

    @patch('builtins.open', return_value=StringIO("Test content"))
    def test_open_file_and_count_chars(self, filename):
        result = open_file_and_count_chars(filename)
        self.assertEqual(result, 12)
