# -*- coding: utf-8 -*-

name = u'termcolor'

version = '1.1.0'

description = \
    """
    termcolor library 
    """

requires = []

variants = []


def commands():
    import os

    termcolor_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "termcolor", "%s" % version)

    # env.PATH.append(os.path.join(termcolor_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(termcolor_libs_path, 'lib'))
