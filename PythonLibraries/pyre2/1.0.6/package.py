# -*- coding: utf-8 -*-

name = u'pyre2'

version = '1.0.6'

description = \
    """
    pyre2 
    """

variants = [['platform-windows']]

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyre2", "%s"%version).replace("/", os.sep)
    
    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))
