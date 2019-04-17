# -*- coding: utf-8 -*-
name = 'httrack'
version = '3.49.2'
author = ['httrack']
tools = []
requires = []
variants = []


def commands():
    import os
    import sys
    # env.PATH.prepend("C:/Program Files/Autodesk/Maya2016/bin")
    applications_path = os.environ["APPLICATIONS_PATH"]

    httrack_path = os.path.join(applications_path, "httrack", "%s"%version).replace("/", os.sep)
   
    env.PATH.append(os.path.join(httrack_path).replace("/", os.sep))
    
    # if sys.platform.startswith("win32"):
    #     env.PATH.append(os.path.join(httrack_path, "lib").replace("/", os.sep))
    #     env.INCLUDE.append(os.path.join(httrack_path, "include").replace("/", os.sep))
    #     env.LIB.append(os.path.join(httrack_path, "lib").replace("/", os.sep))
    #
    # if sys.platform.startswith("linux"):
    #     env.LD_LIBRARY_PATH.append(os.path.join(httrack_path, "lib").replace("/", os.sep))
    #     env.LD_LIBRARY_PATH.append(os.path.join(httrack_path, "bin").replace("/", os.sep))
    #


