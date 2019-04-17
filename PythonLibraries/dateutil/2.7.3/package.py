# -*- coding: utf-8 -*-

name = u'dateutil'

version = '2.7.3'

description = \
    """
    dateutil library 
    """

requires = []

variants = []


def commands():
    import os

    dateutil_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "dateutil", "%s" % version)

    # env.PATH.append(os.path.join(dateutil_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(dateutil_libs_path, 'lib'))
