# -*- coding: utf-8 -*-

name = u'typing'

version = '3.6.4'

description = \
    """
    typing library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    typing_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "typing", "%s"%version)

    # env.PATH.append(os.path.join(typing_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(typing_libs_path, 'lib'))
