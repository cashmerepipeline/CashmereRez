# -*- coding: utf-8 -*-

name = u'pyyaml'

version = '4.01'

description = \
    """
    yaml file parser
    """

variants = [['platform-windows']]

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyyaml", "%s"%version).replace("/", os.sep)
    
    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))
