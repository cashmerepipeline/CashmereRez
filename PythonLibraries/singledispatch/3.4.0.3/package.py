# -*- coding: utf-8 -*-

name = u'singledispatch'

version = '3.4.0.3'

description = \
    """
    singledispatch library 
    """

requires = ["six"]

variants = []

def commands():
    import os

    singledispatch_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "singledispatch", "%s"%version)

    # env.PATH.append(os.path.join(    singledispatch_libs_path, 'lib'))
    # env.PATH.append(os.path.join(    singledispatch_libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(singledispatch_libs_path, 'lib'))
