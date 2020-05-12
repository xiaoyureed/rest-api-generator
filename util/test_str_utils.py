import util.str_utils as strutils
import unittest


class TestStrUtils(unittest.TestCase):

    def test_camel_format(self):
        result = strutils.camel_format('test_test_test')
        print(result)

    def test_blank_strict(self):
        result = strutils.blank_strict('   ')
        print(result)
