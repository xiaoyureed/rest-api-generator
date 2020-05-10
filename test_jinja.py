from jinja2 import Environment, PackageLoader


def jinja():
    env = Environment(loader=PackageLoader('template', ''))
    tpl = env.get_template('controller.tpl')
    rendered = tpl.render(name='xiaoyu')
    print(rendered)


if __name__ == '__main__':
    import sys
    import os

    # 不适用于 命令行程序,
    print(sys.argv)  # ['D:/repo/repo_github/shared_already/rest-api-generator/test_jinja.py']
    # 获得的是当前执行脚本的位置
    # 若在命令行, 打印的是 'py xxx'命令中的 xxx
    print(sys.argv[0])  # D:/repo/repo_github/shared_already/rest-api-generator/test_jinja.py

    # python 查找库的路径, 第一个是当前项目路径
    print(sys.path)
    print(sys.path[0])  # D:\repo\repo_github\shared_already\rest-api-generator

    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，
    # 则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    cur_path = sys.path[0]
    if os.path.isdir(cur_path):
        print('current project dir: [{}]'.format(cur_path))
    elif os.path.isfile(cur_path):
        dirname = os.path.dirname(cur_path)
        print('current project dir: [{}]'.format(dirname))

    # 当前工作目录
    # 若要改变当前工作路径，可以用：os.chdir(path)
    print(os.getcwd())
    print(os.path.abspath(os.curdir))
    print(os.curdir)  # 相对路径
    print(os.path.abspath('.'))
    # 父目录
    print(os.path.abspath('..'))
