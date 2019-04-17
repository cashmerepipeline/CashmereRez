# -*- coding: utf-8 -*-

name = u'pytest'

version = '1.5.7'

description = \
    """
    pytest 
    """

requires = ['six',
            'atomicwrites',
            'attrs',
            'colorama',
            'funcsigs',
            'moreitertools',
            'pluggy',
            'py']

variants = []

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pytest", "%s"%version).replace("/", os.sep)

    env.PATH.append(libs_path)
    env.PATH.append(os.path.join(libs_path, 'Scripts').replace("/", os.sep))

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))

