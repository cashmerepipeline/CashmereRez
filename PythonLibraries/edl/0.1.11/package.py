# -*- coding: utf-8 -*-

name = u'edl'

version = '0.1.11'

description = \
    """
    edl library 
    """

requires = ["timecode"]

variants = []

def commands():
    import os
    
    typing_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "edl", "%s"%version)

    # env.PATH.append(os.path.join(typing_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(typing_libs_path, 'lib'))
