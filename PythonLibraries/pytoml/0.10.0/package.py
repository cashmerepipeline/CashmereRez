# -*- coding: utf-8 -*-

name = u'pytoml'

version = '0.10.0'

description = \
    """
    pytoml library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    pytoml_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pytoml", "%s"%version)

    # env.PATH.append(os.path.join(pytoml_libs_path, 'Scripts')).replace('/', os.sep)

    env.PYTHONPATH.append(os.path.join(pytoml_libs_path, 'lib'))
