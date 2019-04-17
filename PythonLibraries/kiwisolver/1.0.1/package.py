# -*- coding: utf-8 -*-

name = u'kiwisolver'

version = '1.0.1'

description = \
    """
    kiwisolver library 
    """

requires = []

variants = []


def commands():
    import os

    kiwisolver_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "kiwisolver", "%s" % version)

    # env.PATH.append(os.path.join(kiwisolver_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(kiwisolver_libs_path, 'lib'))
