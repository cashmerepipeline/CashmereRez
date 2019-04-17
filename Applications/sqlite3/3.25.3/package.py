# -*- coding: utf-8 -*-
name = 'sqlite3'
version = '2018.2'
author = ['sqlite']
tools = []
requires = []
variants = []


def commands():
    import os
    import sys
    # env.PATH.prepend("C:/Program Files/Autodesk/Maya2016/bin")
    applications_path = os.environ["APPLICATIONS_PATH"]

    sqlite3_path = os.path.join(applications_path, "sqlite3", "%s"%version).replace("/", os.sep)
   
    env.PATH.append(os.path.join(sqlite3_path, "bin").replace("/", os.sep))
    
    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(sqlite3_path, "lib").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(sqlite3_path, "include").replace("/", os.sep))
        env.LIB.append(os.path.join(sqlite3_path, "lib").replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(sqlite3_path, "lib").replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(sqlite3_path, "bin").replace("/", os.sep))    
   

