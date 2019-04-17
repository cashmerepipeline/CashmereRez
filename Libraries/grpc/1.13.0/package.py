# -*- coding: utf-8 -*-

name = u'grpc'

version = '1.13.0'

description = \
    """
    grpc library 
    """

requires = ["libprotobuf"]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    grpc_path = os.path.join(cpp_libs_path, "grpc", "%s"%version)
    grpc_path = grpc_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(grpc_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(grpc_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(grpc_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(grpc_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(grpc_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(grpc_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(grpc_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(grpc_path, 'tbb', "vc14").replace("/", os.sep))

