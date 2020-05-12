# -*- coding:utf-8 -*-

"""string utils"""


def camel_format(target: str) -> str:
    """转为驼峰命名"""

    if '_' not in target:
        return target

    # map(fuc, ite), 将 fuc 作用到 ite 中的每个 item 上
    join = "".join(map(lambda x: x.capitalize(), target.split('_')))
    # 首字符需要小写
    return join[0].lower() + join[1:]


def blank_strict(content: str) -> bool:
    """严格判空"""
    if content is None:
        return True
    if content.strip() == '':
        return True
    return False


def not_blank_strict(content: str) -> bool:
    return not blank_strict(content)

