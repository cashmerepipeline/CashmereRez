# -*- coding: utf-8 -*-

name = 'julia'

version = '1.0.0'

author = ['julia']

tools = ["julia"]

requires = [] 

variants = [ ]



def commands():
    import os
    import sys

    applications_path = os.environ["APPLICATIONS_PATH"]

    julia_path = os.path.join(applications_path, "julia", "%s"%version).replace("/", os.sep)
    env.JULIA_DIR = os.path.join(julia_path, "bin")
    
    if sys.platform.startswith("win32"):
        env.PATH.append(julia_path)
        env.PATH.append(os.path.join(julia_path, "bin").replace('/', os.sep))

        env.INCLUDE.append(os.path.join(julia_path, "include").replace('/', os.sep))
        # env.INCLUDE.append(os.path.join(julia_path, "Library", "include").replace('/', os.sep))
        
        env.LIB.append(os.path.join(julia_path, "lib").replace('/', os.sep))
        # env.LIB.append(os.path.join(julia_path, "Library", "lib").replace('/', os.sep))
