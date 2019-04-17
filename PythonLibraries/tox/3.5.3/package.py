# -*- coding: utf-8 -*-

name = u'tox'

version = '3.6.4'

description = \
    """
    tox library 
    """

requires = ['pytoml',
            'filelock',
            'six',
            'pluggy',
            'py']

variants = []

def commands():
    import os
    
    tox_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "tox", "%s"%version)

    env.PATH.append(os.path.join(tox_libs_path, 'Scripts').replace("/", os.sep))

    env.PYTHONPATH.append(os.path.join(tox_libs_path, 'lib'))
