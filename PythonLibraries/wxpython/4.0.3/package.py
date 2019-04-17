# -*- coding: utf-8 -*-

name = u'wxpython'

version = '4.0.3'

description = \
    """
    wxpython libraries
    """

requires = []

variants = []

def commands():
    import os

    wxpython_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "wxpython", "%s" % version)

    # env.PATH.append(os.path.join(wxpython_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(wxpython_libs_path, 'lib'))
