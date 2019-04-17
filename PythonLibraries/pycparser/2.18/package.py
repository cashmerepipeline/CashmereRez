# -*- coding: utf-8 -*-

name = u'pycparser'

version = '2.18'

description = \
    """
    pycparser libraries
    """

requires = []

variants = []

def commands():
    import os

    pycparser_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pycparser", "%s"%version)

    # env.PATH.append(os.path.join(pycparser_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(pycparser_libs_path, 'lib'))
