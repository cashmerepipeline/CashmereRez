# -*- coding: utf-8 -*-
name = 'ffmpeg'
version = '4.1'
author = ['ffmpeg']
tools = []
requires = []
variants = []


def commands():
    import os
    import sys
    # env.PATH.prepend("C:/Program Files/Autodesk/Maya2016/bin")
    applications_path = os.environ["APPLICATIONS_PATH"]

    ffmpeg_path = os.path.join(applications_path, "ffmpeg", "%s"%version).replace("/", os.sep)
    
    # env.PYTHONPATH.append(os.path.join(ffmpeg_path, "lib", "python").replace("/", os.sep))
   
    env.PATH.append(os.path.join(ffmpeg_path, "bin").replace("/", os.sep))
    
    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(ffmpeg_path, "lib").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(ffmpeg_path, "include").replace("/", os.sep))
        env.LIB.append(os.path.join(ffmpeg_path, "lib").replace("/", os.sep))
    #
    # if sys.platform.startswith("linux"):
    #     env.LD_LIBRARY_PATH.append(os.path.join(ffmpeg_path, "lib").replace("/", os.sep))
    #     env.LD_LIBRARY_PATH.append(os.path.join(ffmpeg_path, "bin").replace("/", os.sep))
    #

