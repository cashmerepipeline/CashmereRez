# -*- coding: utf-8 -*-

name = u'pyopengl'

version = '3.1.0'

description = \
    """
    opengl python binding
    """

requires = []

variants = []

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyopengl", "%s"%version)
    
    # env.PATH.append(os.path.join(libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'))
