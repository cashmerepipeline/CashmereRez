# -*- coding: utf-8 -*-

name = 'msys2'

version = '1.0.0'

author = ['msys2']

tools = ["msys2"]

requires = [] 

variants = [ ]



def commands():
    import os
    import sys

    applications_path = os.environ["APPLICATIONS_PATH"]

    msys2_path = os.path.join(applications_path, "msys2", "%s"%version).replace("/", os.sep)
    
    if sys.platform.startswith("win32"):
        env.PATH.append(msys2_path)
        env.PATH.append(os.path.join(msys2_path, "usr", "bin").replace('/', os.sep))

        env.INCLUDE.append(os.path.join(msys2_path, "include").replace('/', os.sep))
        # env.INCLUDE.append(os.path.join(msys2_path, "Library", "include").replace('/', os.sep))
        
        env.LIB.append(os.path.join(msys2_path, "libs").replace('/', os.sep))
        # env.LIB.append(os.path.join(msys2_path, "Library", "lib").replace('/', os.sep))




