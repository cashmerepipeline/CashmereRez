# -*- coding: utf-8 -*-

name = u'colorama'

version = '0.3.9'

description = \
    """
    coloraman library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    colorama_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "colorama", "%s"%version)

    # env.PATH.append(os.path.join(colorama_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(colorama_libs_path, 'lib'))
    
