# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/12
@Author      : dosea
@File        : setup.py
@Description : 
"""

from setuptools import setup, find_packages


setup(
        name='my_package',     # 包名字
        version='1.0',   # 包版本
        description='',   # 简单描述
        author='dosea',  # 作者
        author_email='doosea@163.com',  # 作者邮箱
        url='https://github.com/doosea/mypackage.git',      # 包的主页
        packages=find_packages()                # 包
)