# -*- coding: utf-8 -*-

name = u'pyzmq'

version = '17.1.0'

description = \
    """
    zeromq python binding
    """

requires = ['python-2.7' ]

variants = []

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyzmq", "%s" % version)

    env.PATH.append(os.path.join(libs_path, 'lib'))
    env.PATH.append(os.path.join(libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'))
