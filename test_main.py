import os
import unittest
import main


class TestMain(unittest.TestCase):

    def test_query_columns(self):
        columns = main.query_columns()
        print(columns)

    def test_render(self):
        rendered = main.render('controller.tpl', name='xiao')
        self.assertEqual(rendered, 'hello, xiao')

    def test_write(self):
        main.write(os.path.abspath('.') + '/out/controller.text', 'hello xxx world.\r\nxiao')

    def test_clean(self):
        main.clean_out()
