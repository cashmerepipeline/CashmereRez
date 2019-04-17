# -*- coding: utf-8 -*-

name = u'pluggy'

version = '0.6.0'

description = \
    """
    pluggyn library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    pluggy_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pluggy", "%s"%version)

    # env.PATH.append(os.path.join(pluggy_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(pluggy_libs_path, 'lib'))
