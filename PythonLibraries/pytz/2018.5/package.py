# -*- coding: utf-8 -*-

name = u'pytz'

version = '2018.5'

description = \
    """
    pytz library 
    """

requires = []

variants = []


def commands():
    import os

    pytz_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pytz", "%s" % version)

    # env.PATH.append(os.path.join(pytz_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(pytz_libs_path, 'lib'))
