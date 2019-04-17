# -*- coding: utf-8 -*-

name = u'absl'

version = '0.1.12'

description = \
    """
    absl library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    absl_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "absl", "%s"%version)

    # env.PATH.append(os.path.join(absl_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(absl_libs_path, 'lib'))
