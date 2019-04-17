# -*- coding: utf-8 -*-

name = u'alembic'

version = '2.12.0'

description = \
    """
    alembic library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    alembic_path = os.path.join(cpp_libs_path, "alembic", "%s"%version)
    alembic_path = alembic_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(alembic_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(alembic_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(alembic_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(alembic_path, 'bin').replace("/", os.sep))


