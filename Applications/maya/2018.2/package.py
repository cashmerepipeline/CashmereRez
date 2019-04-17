# -*- coding: utf-8 -*-
name = 'maya'
version = '2018.2'
author = ['Autodesk']
tools = ['maya', 'mayapy', 'designer']
requires = []
variants = []

def commands():
    import os
    import sys
    
    applications_path = os.environ["APPLICATIONS_PATH"]

    maya_path = os.path.join(applications_path, "maya", "%s"%version).replace("/", os.sep)

    env.REZ_MAYA_VERSION.set("2018")
    env.MAYA_LOCATION.set(maya_path)
    env.MAYA_DISABLE_CIP.set("1")

    env.QT_QPA_PLATFORM_PLUGIN_PATH = os.path.join(maya_path, "qt-plugins", "platforms").replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(maya_path, "Python", "Lib", "site-packages").replace("/", os.sep))
    if sys.platform.startswith("win32"):
        env.PATH.append(maya_path)
        env.PATH.append((maya_path +'/bin').replace("/", os.sep))
        env.PATH.append((maya_path +'/plug-ins/bifrost/bin').replace("/", os.sep))
        env.PATH.append((maya_path +'/plug-ins/xgen/bin').replace("/", os.sep))
        env.PATH.append((maya_path +'/plug-ins/substance/bin').replace("/", os.sep))

        env.INCLUDE.append(os.path.join(maya_path, 'include').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(maya_path, 'include', "python2.7").replace("/", os.sep))
        env.LIB.append(os.path.join(maya_path, 'lib').replace("/", os.sep))

    else:
        env.LD_LIBRARY_PATH.prepend((maya_path +'/bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.prepend((maya_path +'/plug-ins/bifrost/bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.prepend((maya_path +'/plug-ins/xgen/bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.prepend((maya_path +'/plug-ins/substance/bin').replace("/", os.sep))
        env.PYTHONPATH.append((maya_path +'/plug-ins/xgen/scripts').replace("/", os.sep))s


