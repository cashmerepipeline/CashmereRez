# -*- coding: utf-8 -*-

name = u'funcsigs'

version = '1.0.2'

description = \
    """
    funcsigsn library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    funcsigs_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "funcsigs", "%s"%version)

    # env.PATH.append(os.path.join(funcsigs_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(funcsigs_libs_path, 'lib'))
