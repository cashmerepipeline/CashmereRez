# -*- coding: utf-8 -*-

name = u'future'

version = '0.17.1'

description = \
    """
    future libraries
    """

requires = []

variants = []

def commands():
    import os

    futures_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "future", "%s"%version)

    # env.PATH.append(os.path.join(futures_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(futures_libs_path, 'lib'))
    env.PATH.append(os.path.join(futures_libs_path, 'Scripts').replace("/", os.sep))
