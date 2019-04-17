# -*- coding: utf-8 -*-

name = u'argparse'

version = '1.4.0'

description = \
    """
    argparse libraries
    """

requires = []

variants = []

def commands():
    import os

    argparse_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "argparse", "%s"%version)

    # env.PATH.append(os.path.join(argparse_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(argparse_libs_path, 'lib'))
