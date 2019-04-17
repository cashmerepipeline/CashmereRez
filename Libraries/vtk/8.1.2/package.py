# -*- coding: utf-8 -*-
name = 'vtk'
version = '8.1.2'
author = ['Pixar']
tools = []
requires = []
variants = []


def commands():
    import os
    import sys
    # env.PATH.prepend("C:/Program Files/Autodesk/Maya2016/bin")
    applications_path = os.environ["APPLICATIONS_PATH"]

    vtk_path = os.path.join(applications_path, "vtk", "%s"%version).replace("/", os.sep)

    env.VTK_DIR = os.path.join(vtk_path, "lib", "cmake", "vtk-8.1").replace("/", os.sep)
    
    env.PYTHONPATH.append(os.path.join(vtk_path, "lib", "python").replace("/", os.sep))
   
    env.PATH.append(os.path.join(vtk_path, "bin").replace("/", os.sep))
    
    if sys.platform.startswith("win32"):
        # env.PATH.append(os.path.join(vtk_path, "lib").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(vtk_path, "include").replace("/", os.sep))
        env.LIB.append(os.path.join(vtk_path, "lib").replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(vtk_path, "lib").replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(vtk_path, "bin").replace("/", os.sep))    
   

