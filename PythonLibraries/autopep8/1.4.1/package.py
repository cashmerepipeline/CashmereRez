# -*- coding: utf-8 -*-

name = u'autopep8'

version = '1.4.1'

description = \
    """
    autopep8 library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    autopep8_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "autopep8", "%s"%version)

    env.PATH.append(os.path.join(autopep8_libs_path, 'Scripts').replace("/", os.sep))

    env.PYTHONPATH.append(os.path.join(autopep8_libs_path, 'lib'))
