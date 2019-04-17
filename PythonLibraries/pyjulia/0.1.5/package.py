# -*- coding: utf-8 -*-

name = u'pyjulia'

version = '0.1.5'

description = \
    """
    pyjulia 
    """

variants = [['platform-windows']]

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyjulia", "%s"%version).replace("/", os.sep)
    env.PATH.append(os.path.join(libs_path, 'lib', 'julia', 'fake-julia').replace("/", os.sep))
    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))
