# -*- coding: utf-8 -*-

name = u'filelock'

version = '0.10.0'

description = \
    """
    filelock library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    filelock_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "filelock", "%s"%version)

    # env.PATH.append(os.path.join(filelock_libs_path, 'Scripts').replace('/', os.sep))

    env.PYTHONPATH.append(os.path.join(filelock_libs_path, 'lib'))
