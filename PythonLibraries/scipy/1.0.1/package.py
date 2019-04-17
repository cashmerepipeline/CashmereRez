# -*- coding: utf-8 -*-

name = u'scipy'

version = '1.0.1'

description = \
    """
    scipy libraries
    """

requires = ['numpy']

variants = []

def commands():
    import os

    scipy_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "scipy", "%s" % version)

    # env.PATH.append(os.path.join(scipy_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(scipy_libs_path, 'lib'))
