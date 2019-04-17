# -*- coding: utf-8 -*-

name = u'cython'

version = '0.28.1'

description = \
    """
    cython
    """

requires = ["maya"]

variants = []

def commands():
    import os
    import sys
    
    python_libs_path = getenv("PYTHON_LIBS_PATH")

    cython_path = os.path.join(python_libs_path, "cython", "%s"%version)
    cython_path = cython_path.replace("/", os.sep)

    env.PATH.prepend(os.path.join(cython_path, 'Scripts'))
    env.PYTHONPATH.prepend(os.path.join(cython_path, 'lib'))

