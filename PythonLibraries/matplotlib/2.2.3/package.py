# -*- coding: utf-8 -*-

name = u'matplotlib'

version = '2.2.3'

description = \
    """
    matplotlib library 
    """

requires = ["cycler",
            "backports",
            "dateutil",
            "kiwisolver",
            "pyparsing",
            "pytz",
            "six",
            "numpy",
            "freetype"
            ]

variants = []


def commands():
    import os

    matplotlib_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "matplotlib", "%s" % version)

    # env.PATH.append(os.path.join(matplotlib_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(matplotlib_libs_path, 'lib'))
