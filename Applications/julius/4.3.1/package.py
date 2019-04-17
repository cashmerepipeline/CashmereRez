# -*- coding: utf-8 -*-
name = 'julius'
version = '4.3.1'
author = ['julius']
tools = []
requires = []
variants = []


def commands():
    import os
    import sys
    # env.PATH.prepend("C:/Program Files/Autodesk/Maya2016/bin")
    applications_path = os.environ["APPLICATIONS_PATH"]

    julius_path = os.path.join(applications_path, "julius", "%s"%version).replace("/", os.sep)
    
    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(julius_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(julius_path, "include").replace("/", os.sep))
        env.LIB.append(os.path.join(julius_path, "lib").replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(julius_path, "lib").replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(julius_path, "bin").replace("/", os.sep))    
   

