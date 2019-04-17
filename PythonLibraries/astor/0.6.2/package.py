# -*- coding: utf-8 -*-

name = u'astor'

version = '0.1.12'

description = \
    """
    astor library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    astor_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "astor", "%s"%version)

    # env.PATH.append(os.path.join(astor_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(astor_libs_path, 'lib'))
