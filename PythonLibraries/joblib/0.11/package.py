# -*- coding: utf-8 -*-

name = u'joblib'

version = '0.11'

description = \
    """
    joblib library 
    """

requires = [ ]

variants = []

def commands():
    import os
    
    joblib_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "joblib", "%s"%version)

    # env.PATH.append(os.path.join(joblib_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(joblib_libs_path, 'lib'))
