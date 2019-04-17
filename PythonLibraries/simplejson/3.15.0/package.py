# -*- coding: utf-8 -*-

name = u'simplejson'

version = '3.15.0'

description = \
    """
    Simple, fast, extensible JSON encoder/decoder for Python
    """

variants = []

requires = ['boost' ]

def commands():
    import os

    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "simplejson", "%s" % version)
    env.PYTHONPATH.append(os.path.join(libs_path, "lib").replace("/", os.sep))


