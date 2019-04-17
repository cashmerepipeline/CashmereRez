# -*- coding: utf-8 -*-

name = u'astroid'

version = '1.6.2'

description = \
    """
    
    """

variants = []

requires = ['enum']

def commands():
    import os

    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "astroid", "%s" % version)
    env.PYTHONPATH.append(os.path.join(libs_path, "lib").replace("/", os.sep))


