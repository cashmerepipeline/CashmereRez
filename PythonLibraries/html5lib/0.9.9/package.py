# -*- coding: utf-8 -*-

name = u'html5lib'

version = '0.9.9'

description = \
    """
    html5lib library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    html5lib_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "html5lib", "%s"%version)

    # env.PATH.append(os.path.join(html5lib_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(html5lib_libs_path, 'lib'))
