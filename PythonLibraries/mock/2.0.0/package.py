# -*- coding: utf-8 -*-

name = u'mock'

version = '2.0.0'

description = \
    """
    mock library 
    """

requires = ["funcsigs",
            "pbr",
            "six"]

variants = []

def commands():
    import os
    
    mock_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "mock", "%s"%version)

    # env.PATH.append(os.path.join(mock_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(mock_libs_path, 'lib'))
