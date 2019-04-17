# -*- coding: utf-8 -*-

name = u'coverage'

version = '1.10.0'

description = \
    """
    coverage library 
    """

requires = ["six",
            "enum",
            "cython",
            "protobuf"]

variants = []

def commands():
    import os
    
    coverage_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "coverage", "%s"%version)

    env.PATH.append(os.path.join(coverage_libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(coverage_libs_path, 'lib'))
