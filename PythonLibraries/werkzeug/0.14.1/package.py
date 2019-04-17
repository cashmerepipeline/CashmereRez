# -*- coding: utf-8 -*-

name = u'werkzeug'

version = '0.14.1'

description = \
    """
    werkzeug library 
    """

requires = []

variants = []


def commands():
    import os

    werkzeug_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "werkzeug", "%s" % version)

    # env.PATH.append(os.path.join(werkzeug_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(werkzeug_libs_path, 'lib'))
