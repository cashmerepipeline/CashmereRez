# -*- coding: utf-8 -*-

name = u'py'

version = '1.7.0'

description = \
    """
    py library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    py_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "py", "%s"%version)

    # env.PATH.append(os.path.join(py_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(py_libs_path, 'lib'))
