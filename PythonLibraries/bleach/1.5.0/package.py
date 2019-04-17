# -*- coding: utf-8 -*-

name = u'bleach'

version = '1.5.0'

description = \
    """
    bleach library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    bleach_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "bleach", "%s"%version)

    # env.PATH.append(os.path.join(bleach_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(bleach_libs_path, 'lib'))
