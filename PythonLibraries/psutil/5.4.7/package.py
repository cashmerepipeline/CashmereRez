# -*- coding: utf-8 -*-

name = u'psutil'

version = '5.4.7'

description = \
    """
    yaml file parser
    """

variants = [['platform-windows']]

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "psutil", "%s"%version).replace("/", os.sep)
    
    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))
