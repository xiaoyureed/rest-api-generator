#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""generate crud api
目前仅适配了 postgres
"""
import os
import re
from jinja2 import PackageLoader, Environment
import psycopg2 as pg
import logging

import util.str_utils as strutils

logging.basicConfig(level=logging.INFO)

global_config = {
    # package name
    'base_package': 'io.github.xiaoyureed.demo',
    'domain': 'product',
    'table_name': 'product',
    # db connection info
    'host': 'localhost',
    'port': '5432',
    'database': 'dbtest',
    'user': 'xy',
    'password': 'xy123'
}


def query_columns() -> list:
    """
    query db columns

    :return:  column list, element is a tuple
    """
    conn = pg.connect(database=global_config.get('database'),
                      user=global_config.get('user'),
                      password=global_config.get('password'),
                      host=global_config.get('host'), port=global_config.get('port'))
    # 指针
    cur = conn.cursor()
    # https://blog.csdn.net/weixin_38924323/article/details/80982760
    cur.execute('''SELECT 
                a.attname                             as name,
                format_type(a.atttypid, a.atttypmod)  as type,
                col_description(a.attrelid, a.attnum) as comment,
                a.attnotnull                          as notnull
                FROM pg_class as c,
                pg_attribute as a
                where c.relname = '{table_name}'
                and a.attrelid = c.oid
                and a.attnum > 0'''.format(table_name=global_config.get('table_name')))
    result = cur.fetchall()
    if len(result) == 0:
        logging.error('>>> invalid table_name')
    return result


def render(tpl_name, **kwargs):
    """
    render template

    :param tpl_name: template name
    :param kwargs: args
    :return: rendered content
    """

    # param1: package name,
    # param2: tpl dir,
    # 还有 FileSystemLoader
    env = Environment(loader=PackageLoader('template', ''))
    tpl = env.get_template(tpl_name)

    result = tpl.render(kwargs)
    if strutils.blank_strict(result):
        logging.error('>>> invalid template name')
    return result


def write(file_path, content):
    """
    write to file

    :param file_path: file path
    :param content: content
    :return:
    """
    if os.path.exists(file_path):
        logging.info('>>> file [{}] already exists, skip'.format(file_path))
        return

    # check if the folder exists
    dir_path = os.path.split(file_path)[0]
    if not os.path.exists(dir_path):
        # create folder, mkdir 只能创建一层目录, makedirs 可以创建多层级目录
        os.makedirs(dir_path)
        logging.info('>>> dir [{}] doesn\'t exist, now create it'.format(dir_path))

    # open input stream, specify the line Separator
    with open(file_path, 'w') as f:
        f.write(dos2unix(content))
        logging.info('>>> generate file [{}]'.format(file_path))


def dos2unix(dos_content: str) -> str:
    """
    convert dos content to unix content

    :param dos_content: dos content
    :return: unix content
    """
    return dos_content.replace('\r\n', '\n')


def clean_out(out_dir='out'):
    """
    clean out dir

    :param out_dir: output directory, default to 'out'
    :return:
    """

    for root, dir_names, file_names in os.walk(out_dir, topdown=False):
        for name in dir_names:
            os.rmdir(os.path.join(root, name))
        for name in file_names:
            os.remove(os.path.join(root, name))


def generate_po(columns: list) -> None:
    """
    generate po

    :param columns: database columns,
        like this: [('id', 'integer', None, True), ('name', 'text', 'product name', True), ...]
    :return: None
    """

    # 类全名, 用于生成 import
    # 空set 只能使用 set(), {} 是用来创建空 dict 的
    full_type_names = set()

    # column-type dict, 用于生成 field, 不能用 type 作为 key, 因为可能存在相同类型的 db column 可能类型相同
    col_type_dict = {}

    for col in columns:
        # 只有 BigDecimal, Date 需要显式引入, 其他基本类型都默认导入了
        col_type = col[1]
        if 'numeric' in col_type:
            full_type_names.add('java.math.BigDecimal')
        elif 'timestamp' in col_type:
            full_type_names.add('java.util.Date')

        #################

        col_name = col[0]
        col_name = strutils.camel_format(col_name)
        if 'bigint' in col_type:
            col_type_dict[col_name] = 'Long'
        elif 'integer' in col_type:
            col_type_dict[col_name] = 'Long'  # 数据库 中的 integer 类型也使用  java 的 Long 类型
        elif 'text' in col_type or 'character' in col_type:
            col_type_dict[col_name] = 'String'
        elif 'jsonb' in col_type:
            col_type_dict[col_name] = 'Object'
        elif 'smallint' in col_type:
            col_type_dict[col_name] = 'Short'
        elif 'timestamp' in col_type:
            col_type_dict[col_name] = 'Date'
        elif 'numeric' in col_type:
            col_type_dict[col_name] = 'BigDecimal'
        else:
            logging.error('>>> unknown column type [{}]'.format(col_type))

    path = os.path.join(os.path.abspath('out'),
                        global_config.get('base_package').replace('.', '/'),
                        # 不要用 '/' 开头
                        'pojo/po', global_config.get('domain').capitalize() + '.java')

    rendered = render('po.tpl', base_package=global_config.get('base_package'), full_type_names=full_type_names,
                      domain=global_config.get('domain'), col_type_dict=col_type_dict)
    write(path, rendered)


def generate_mapper() -> None:
    path = os.path.join(os.path.abspath('out'),
                        global_config.get('base_package').replace('.', '/'),
                        'dao/mapper', global_config.get('domain').capitalize() + 'Mapper.java')
    write(path, render('mapper.tpl', base_package=global_config.get('base_package'),
                       domain=global_config.get('domain'), ))


def generate_dao():
    path = os.path.join('out', global_config.get('base_package').replace('.', '/'),
                        'dao', global_config.get('domain').capitalize() + 'Dao.java')
    write(path, render('dao.tpl', base_package=global_config.get('base_package'),
                       domain=global_config.get('domain')))


def generate_mapper_xml(columns: list):
    path = os.path.join('out', 'mapper', global_config.get('domain').capitalize() + 'Mapper.xml')
    result_map = list()
    result_map_jsonb = list()  # jsonb 单独拿出来, 在模板中处理 typeHandler
    base_column_list = ''
    for col in columns:
        col_name = col[0]
        col_type = col[1]
        if '.' not in col_name:
            to_add = {'column': col_name,
                      'property': strutils.camel_format(col_name)}
            if 'bigint' in col_type:
                to_add['jdbc_type'] = 'BIGINT'
            elif 'text' in col_type or 'character' in col_type:
                to_add['jdbc_type'] = 'VARCHAR'
            elif 'numeric' in col_type:
                to_add['jdbc_type'] = 'NUMERIC'
            elif 'jsonb' in col_type:
                to_add['jdbc_type'] = 'OTHER'
                to_add['type_handler'] = 'com.pingan.imp.sme.utils.JsonTypeHandler'
            elif 'smallint' in col_type:
                to_add['jdbc_type'] = 'SMALLINT'
            elif 'timestamp' in col_type:
                to_add['jdbc_type'] = 'TIMESTAMP'

            if 'type_handler' in to_add:
                result_map_jsonb.append(to_add)
            else:
                result_map.append(to_add)
            base_column_list += col_name + ','

    render_str = render('mapper.xml.tpl', base_package=global_config.get('base_package'),
                        domain=global_config.get('domain'),
                        result_map=result_map,
                        result_map_jsonb=result_map_jsonb,
                        base_column_list=base_column_list[:-1],
                        table_name=global_config.get('table_name'))
    # TODO
    # jinja2 doesn't support #{{{...}}},
    pattern = re.compile(r'(\[)(.*?)(\])')
    sub = pattern.sub(r'{\2}', render_str, )
    write(path, sub)


def generate_service():
    path = os.path.join('out', global_config.get('base_package').replace('.', '/'),
                        'service/impl', global_config.get('domain').capitalize() + 'ServiceImpl.java')
    write(path, render('service.tpl',
                       base_package=global_config.get('base_package'),
                       domain=global_config.get('domain')))


def generate_controller():
    path = os.path.join('out', global_config.get('base_package').replace('.', '/'),
                        'controller', global_config.get('domain').capitalize() + 'Controller.java')
    write(path, render('controller.tpl',
                       base_package=global_config.get('base_package'),
                       domain=global_config.get('domain')))


def generate_all():
    cols = query_columns()
    generate_po(cols)
    generate_mapper()
    generate_dao()
    generate_mapper_xml(cols)
    generate_service()
    generate_controller()


if __name__ == '__main__':
    generate_all()

# def postgres_demo():
#     import psycopg2 as pg
#     import pandas as pd

#     conn = pg.connect(database='sat_sme', user='sat_data',
#                       password='paic1234', host='10.59.97.10', port='5432')
#     cur = conn.cursor()
#     cur.execute('select * from sme_application_file limit 3')
#     result = cur.fetchall()
#     print(result)
#     df = pd.DataFrame(result)
#     print(df)
#     desc = cur.description
#     print(desc[0][1])  # type_code
#     print(dir(pg.extensions.Column.type_code))
#     cur.close()
#     conn.close()
