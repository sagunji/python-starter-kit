# coding: utf-8

from setuptools import setup, find_packages


NAME = "python-starter-kit"
VERSION = "1.0.0"
MODULES = ["mylibrary"]
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = open("requirements.txt").readlines()

setup(
    name=NAME,
    version=VERSION,
    description="Simple kit to get you starter with python",
    author_email="karanjit.sagun01@gmail.com",
    url="https://github.com/sagunji/python-starter-kit.git",
    py_modules=MODULES,
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "mylibrary = mylibrary.cli:main",
            "check-case-conflict = pre_commit_hooks.check_case_conflict:main",
            "check-docstring-first = pre_commit_hooks.check_docstring_first:main",
            "check-yaml = pre_commit_hooks.check_yaml:check_yaml",
        ]
    },
)
