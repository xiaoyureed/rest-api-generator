import os
import unittest
import main


class TestMain(unittest.TestCase):

    def test(self):
        # io/github/xiaoyureed 不要用 '/' 开头
        join = os.path.join('./out', 'io/github/xiaoyureed', 'xy', 'z')
        print(join)
        # ./out/io/github/xiaoyureed

    def test_mkdir(self):
        os.makedirs('./out/io/github/xiaoyureed')

    def test_query_columns(self):
        columns = main.query_columns()
        print(columns)
        # [('id', 'integer', None, True), ('name', 'text', 'product name', True),
        # ('price', 'numeric', 'product price\n', True),
        # ('create_date', 'timestamp without time zone', 'create date', True)]

    def test_render(self):
        rendered = main.render('controller.tpl', name='xiao')
        self.assertEqual(rendered, 'hello, xiao')

    def test_write(self):
        main.write(os.path.abspath('.') + '/out/controller.text', 'hello xxx world.\r\nxiao')

    def test_clean(self):
        main.clean_out()

    def test_generate_po(self):
        col_list = [('id', 'integer', None, True), ('name', 'text', 'product name', True),
                    ('price', 'numeric', 'product price\n', True),
                    ('create_date', 'timestamp without time zone', 'create date', True)]

        main.generate_po(col_list)

    def test_generate_mapper(self):
        main.generate_mapper()

    def test_generate_dao(self):
        main.generate_dao()

    def test_generate_mapper_xml(self):
        col_list = [('id', 'integer', None, True), ('name', 'text', 'product name', True),
                    ('price', 'numeric', 'product price\n', True),
                    ('create_date', 'timestamp without time zone', 'create date', True)]
        main.generate_mapper_xml(col_list)

    def test_generate_service(self):
        main.generate_service()

    def test_generate_controller(self):
        main.generate_controller()
