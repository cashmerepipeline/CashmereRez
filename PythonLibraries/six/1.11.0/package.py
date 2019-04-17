# -*- coding: utf-8 -*-

name = u'six'

version = '1.11.0'

description = \
    """
    six library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    six_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "six", "%s"%version)

    # env.PATH.append(os.path.join(six_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(six_libs_path, 'lib'))
