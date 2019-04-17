# -*- coding: utf-8 -*-

name = u'cuda'

version = '9.1'

description = \
    """
    cuda library 
    """

requires = [ ]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("APPLICATIONS_PATH")

    cuda_path = os.path.join(cpp_libs_path, "cuda", "%s"%version)
    cuda_path = cuda_path.replace("/", os.sep)

    env.CUDA_PATH = cuda_path
    env.CUDA_PATH_V9_1 = cuda_path

    env.CUDNN_INCLUDE_VERSION = 7.1
    # env.CUDA_SDK_ROOT_DIR = cuda_path
    # env.CUDA_TOOLKIT_ROOT_DIR = cuda_path

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(cuda_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(cuda_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(cuda_path, 'lib', 'x64').replace("/", os.sep))

    # if sys.platform.startswith("linux"):
    #     env.LD_LIBRARY_PATH.append(os.path.join(7zip_path, "lib").replace("/", os.sep))
    #     env.LD_LIBRARY_PATH.append(os.path.join(7zip_path, "bin").replace("/", os.sep))
    #

