# -*- coding: utf-8 -*-

name = u'isort'

version = '4.3.4'

description = \
    """
    isort library 
    """

requires = ["futures"]

variants = []

def commands():
    import os
    
    isort_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "isort", "%s"%version)

    # env.PATH.append(os.path.join(isort_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(isort_libs_path, 'lib'))
