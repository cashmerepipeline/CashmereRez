# -*- coding: utf-8 -*-

name = u'jedi'

version = '0.13.1'

description = \
    """
    jedi library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    jedi_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "jedi", "%s"%version)

    # env.PATH.append(os.path.join(jedi_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(jedi_libs_path, 'lib'))
