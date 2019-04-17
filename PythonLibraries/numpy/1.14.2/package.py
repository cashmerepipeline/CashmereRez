# -*- coding: utf-8 -*-

name = u'numpy'

version = '1.14.2'

description = \
    """
    numpy library 
    """

requires = ["mkl" ]

variants = []

def commands():
    import os
    
    numpy_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "numpy", "%s"%version)

    env.PATH.append(os.path.join(numpy_libs_path, 'lib'))
    env.PATH.append(os.path.join(numpy_libs_path, 'lib/numpy/core'.replace('/', os.sep)))
    env.PATH.append(os.path.join(numpy_libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(numpy_libs_path, 'lib'))
