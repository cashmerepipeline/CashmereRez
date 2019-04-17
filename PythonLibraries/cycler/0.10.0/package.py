# -*- coding: utf-8 -*-

name = u'cycler'

version = '0.10.0'

description = \
    """
    cycler library 
    """

requires = []

variants = []


def commands():
    import os

    cycler_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "cycler", "%s" % version)

    # env.PATH.append(os.path.join(cycler_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(cycler_libs_path, 'lib'))
