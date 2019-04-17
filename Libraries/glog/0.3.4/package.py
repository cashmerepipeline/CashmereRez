# -*- coding: utf-8 -*-

name = u'glog'

version = '2.2.1'

description = \
    """
    glog library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    glog_path = os.path.join(cpp_libs_path, "glog", "%s"%version)
    glog_path = glog_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(glog_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(glog_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(glog_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(glog_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glog_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glog_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glog_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(glog_path, 'tbb', "vc14").replace("/", os.sep))

