# -*- coding: utf-8 -*-

name = u'futures'

version = '3.2.0'

description = \
    """
    futures libraries
    """

requires = []

variants = []

def commands():
    import os

    futures_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "futures", "%s"%version)

    # env.PATH.append(os.path.join(futures_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(futures_libs_path, 'lib'))
