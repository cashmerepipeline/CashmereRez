# -*- coding: utf-8 -*-

name = u'attrs'

version = '2.6.11'

description = \
    """
    attrsn library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    attrs_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "attrs", "%s"%version)

    # env.PATH.append(os.path.join(attrs_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(attrs_libs_path, 'lib'))
