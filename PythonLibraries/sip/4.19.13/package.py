# -*- coding: utf-8 -*-

name = u'sip'

version = '4.19.13'

description = \
    """
    sip library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    sip_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "sip", "%s"%version).replace("/", os.sep)

    env.PATH.append(sip_libs_path)
    # env.PATH.append(os.path.join(sip_libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(sip_libs_path, 'lib'))

    if sys.platform.startswith("win32"):
        # env.PATH.append(os.path.join(sip_libs_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(sip_libs_path, 'include').replace("/", os.sep))
        # env.LIB.append(os.path.join(sip_libs_path, 'lib').replace("/", os.sep))
