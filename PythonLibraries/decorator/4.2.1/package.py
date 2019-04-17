# -*- coding: utf-8 -*-

name = u'decorator'

version = '4.2.1'

description = \
    """
    decorator library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    decorator_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "decorator", "%s"%version)

    # env.PATH.append(os.path.join(decorator_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(decorator_libs_path, 'lib'))
