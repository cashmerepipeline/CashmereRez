# -*- coding: utf-8 -*-

name = u'pbr'

version = '3.1.1'

description = \
    """
    pbr library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    pbr_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pbr", "%s"%version)

    # env.PATH.append(os.path.join(pbr_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(pbr_libs_path, 'lib'))
