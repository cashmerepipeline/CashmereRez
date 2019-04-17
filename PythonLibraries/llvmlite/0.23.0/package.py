# -*- coding: utf-8 -*-

name = u'llvmlite'

version = '0.23.0'

description = \
    """
    numba library 
    """

requires = ["enum"]

variants = []

def commands():
    import os
    
    llvmlite_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "llvmlite", "%s"%version)

    env.PATH.append(os.path.join(llvmlite_libs_path, 'llvmlite', 'binding').replace("/", os.sep))
    # env.PATH.append(os.path.join(llvmlite_libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(llvmlite_libs_path, 'lib'))
