# -*- coding: utf-8 -*-

name = u'protobuf'

version = '3.5.2'

description = \
    """
    protobuf library 
    """

requires = ["six",
            "libprotobuf-3.5.2"]

variants = []

def commands():
    import os
    
    protobuf_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "protobuf", "%s"%version)

    # env.PATH.append(os.path.join(protobuf_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(protobuf_libs_path, 'lib'))
