# -*- coding: utf-8 -*-

name = 'python'

version = 'intel2.7'

author = ['python']

tools = ["python"]

requires = [] 

variants = [ ]



def commands():
    import os
    import sys

    applications_path = os.environ["APPLICATIONS_PATH"]

    python_path = os.path.join(applications_path, "python", "%s"%version).replace("/", os.sep)
    
    if sys.platform.startswith("win32"):
        env.PATH.append(python_path)
        env.PATH.append(os.path.join(python_path, "Scripts").replace('/', os.sep))
        env.PATH.append(os.path.join(python_path, "bin").replace('/', os.sep))

        env.INCLUDE.append(os.path.join(python_path, "include").replace('/', os.sep))
        env.INCLUDE.append(os.path.join(python_path, "Library", "include").replace('/', os.sep))
        
        env.LIB.append(os.path.join(python_path, "libs").replace('/', os.sep))
        env.LIB.append(os.path.join(python_path, "Library", "lib").replace('/', os.sep))
