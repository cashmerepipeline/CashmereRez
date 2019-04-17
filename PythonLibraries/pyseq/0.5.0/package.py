# -*- coding: utf-8 -*-

name = u'pyseq'

version = '0.5.0'

description = \
    """
    sequence files 
    """

variants = [['platform-windows']]

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyseq", "%s"%version)
    
    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))


