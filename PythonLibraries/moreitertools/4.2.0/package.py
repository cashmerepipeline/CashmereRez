# -*- coding: utf-8 -*-

name = u'moreitertools'

version = '4.2.0'

description = \
    """
    moreitertoolsn library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    moreitertools_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "moreitertools", "%s"%version)

    # env.PATH.append(os.path.join(moreitertools_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(moreitertools_libs_path, 'lib'))
