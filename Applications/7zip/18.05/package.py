# -*- coding: utf-8 -*-
name = '7zip'
version = '18.05'
author = ['7zip']
tools = []
requires = []
variants = []


def commands():
    import os
    import sys
    # env.PATH.prepend("C:/Program Files/Autodesk/Maya2016/bin")
    applications_path = os.environ["APPLICATIONS_PATH"]

    zip_path = os.path.join(applications_path, "7zip", "%s"%version).replace("/", os.sep)
    
    # env.PYTHONPATH.append(os.path.join(7zip_path, "lib", "python").replace("/", os.sep))
   
    env.PATH.append(os.path.join(zip_path).replace("/", os.sep))
    
    # if sys.platform.startswith("win32"):
    #     env.PATH.append(os.path.join(7zip_path, "lib").replace("/", os.sep))
    #     env.INCLUDE.append(os.path.join(7zip_path, "include").replace("/", os.sep))
    #     env.LIB.append(os.path.join(7zip_path, "lib").replace("/", os.sep))
    #
    # if sys.platform.startswith("linux"):
    #     env.LD_LIBRARY_PATH.append(os.path.join(7zip_path, "lib").replace("/", os.sep))
    #     env.LD_LIBRARY_PATH.append(os.path.join(7zip_path, "bin").replace("/", os.sep))
    #


