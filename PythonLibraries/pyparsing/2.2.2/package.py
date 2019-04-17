# -*- coding: utf-8 -*-

name = u'pyparsing'

version = '2.2.2'

description = \
    """
    pyparsing library 
    """

requires = []

variants = []


def commands():
    import os

    pyparsing_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyparsing", "%s" % version)

    # env.PATH.append(os.path.join(pyparsing_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(pyparsing_libs_path, 'lib'))
