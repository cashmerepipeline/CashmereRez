# -*- coding: utf-8 -*-

name = u'sklearn'

version = '0.20'

description = \
    """
    sklearn libraries
    """

requires = []

variants = []

def commands():
    import os

    sklearn_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "sklearn", "%s"%version)

    # env.PATH.append(os.path.join(sklearn_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(sklearn_libs_path, 'lib'))
    # env.PATH.append(os.path.join(sklearn_libs_path, 'Scripts'))
