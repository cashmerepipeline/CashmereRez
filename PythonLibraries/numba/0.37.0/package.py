# -*- coding: utf-8 -*-

name = u'numba'

version = '0.37.0'

description = \
    """
    numba library 
    """

requires = ["numpy",
            "llvmlite",
            "singledispatch",
            "enum",
            "funcsigs",
            "llvmlite",
            "singledispatch"]

variants = []

def commands():
    import os
    
    numba_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "numba", "%s"%version)

    # env.PATH.append(os.path.join(numba_libs_path, 'lib'))
    env.PATH.append(os.path.join(numba_libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(numba_libs_path, 'lib'))
