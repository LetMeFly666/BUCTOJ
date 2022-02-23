'''
Author: LetMeFly
Date: 2022-01-25 17:46:23
LastEditors: LetMeFly
LastEditTime: 2022-02-23 14:47:20
'''
from setuptools import find_packages
from distutils.core import setup

with open("README.rst", "r", encoding='utf-8') as f:
    long_description = f.read()

"""
python setup.py sdist bdist_wheel
twine upload dist/*
"""

print("Hello From BUCTOJ")
version = '0.0.18'

setup(name = 'BUCTOJ',  # 包名
    version = version,  # 版本号
    description='用Python玩转北化OJ平台',
    long_description = long_description,
    author = 'LetMeFly',
    author_email='Tisfy@qq.com',
    url = 'https://github.com/LetMeFly666/BUCTOJ',
    project_urls={
        "Bug Tracker": "https://github.com/LetMeFly666/BUCTOJ/issues",
        "在线文档": "https://buctoj.readthedocs.io",
    },
    install_requires=[
        'requests>=1.0.0',
        'lxml>=2.0',
        'beautifulsoup4>=4.0.1'
    ],
    license='Apache License',
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ],
)
