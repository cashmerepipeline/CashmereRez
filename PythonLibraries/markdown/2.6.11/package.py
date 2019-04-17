# -*- coding: utf-8 -*-

name = u'markdown'

version = '2.6.11'

description = \
    """
    markdown library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    markdown_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "markdown", "%s"%version)

    # env.PATH.append(os.path.join(markdown_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(markdown_libs_path, 'lib'))
