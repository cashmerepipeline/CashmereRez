# -*- coding: utf-8 -*-

name = u'enum'

version = '2.10'

description = \
    """
    enum libraries
    """

requires = []

variants = []

def commands():
    import os

    enum_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "enum", "%s"%version)

    # env.PATH.append(os.path.join(enum_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(enum_libs_path, 'lib'))
