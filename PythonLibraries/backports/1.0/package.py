# -*- coding: utf-8 -*-

name = u'backports'

version = '1.0'

description = \
    """
    backports library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    backports_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "backports", "%s"%version)

    # env.PATH.append(os.path.join(backports_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(backports_libs_path, 'lib'))
