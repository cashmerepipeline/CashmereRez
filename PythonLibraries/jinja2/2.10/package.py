# -*- coding: utf-8 -*-

name = u'jinja2'

version = '2.10'

description = \
    """
    jinja2 libraries
    """

requires = []

variants = []

def commands():
    import os

    jinja2_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "jinja2", "%s"%version)

    # env.PATH.append(os.path.join(jinja2_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(jinja2_libs_path, 'lib'))
