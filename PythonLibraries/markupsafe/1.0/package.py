# -*- coding: utf-8 -*-

name = u'markupsafe'

version = '1.0'

description = \
    """
    markupsafe libraries
    """

requires = []

variants = []

def commands():
    import os

    markupsafe_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "markupsafe", "%s"%version)

    # env.PATH.append(os.path.join(markupsafe_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(markupsafe_libs_path, 'lib'))
