# -*- coding: utf-8 -*-

name = u'timecode'

version = '1.2.0'

description = \
    """
    timecode library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    typing_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "timecode", "%s"%version)

    # env.PATH.append(os.path.join(typing_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(typing_libs_path, 'lib'))
