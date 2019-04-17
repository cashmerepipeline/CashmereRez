# -*- coding: utf-8 -*-

name = u'gast'

version = '2.6.11'

description = \
    """
    gast library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    gast_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "gast", "%s"%version)

    # env.PATH.append(os.path.join(gast_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(gast_libs_path, 'lib'))
