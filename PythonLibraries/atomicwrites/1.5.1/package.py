# -*- coding: utf-8 -*-

name = u'atomicwrites'

version = '2.6.11'

description = \
    """
    atomicwrites library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    atomicwrites_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "atomicwrites", "%s"%version)

    # env.PATH.append(os.path.join(atomicwrites_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(atomicwrites_libs_path, 'lib'))
