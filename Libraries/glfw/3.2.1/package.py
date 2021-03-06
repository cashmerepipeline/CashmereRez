# -*- coding: utf-8 -*-

name = u'glfw'

version = '3.2.1'

description = \
    """
    glfw library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    glfw_path = os.path.join(cpp_libs_path, "glfw", "%s"%version)
    glfw_path = glfw_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(glfw_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(glfw_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(glfw_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(glfw_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glfw_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glfw_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glfw_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glfw_path, 'tbb', "vc14").replace("/", os.sep))

