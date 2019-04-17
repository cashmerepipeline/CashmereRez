# -*- coding: utf-8 -*-

name = u'grpcio'

version = '1.13.0'

description = \
    """
    grpcio library 
    """

requires = ["enum",
            "cares",
            "protobuf",
            "libprotobuf"
            ]

variants = []

def commands():
    import os
    
    grpcio_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "grpcio", "%s"%version)

    # env.PATH.append(os.path.join(grpcio_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(grpcio_libs_path, 'lib'))
