# -*- coding: utf-8 -*-

name = 'golaem'

version = '5.3.0'

author = ['golaem']

tools = []

requires = []

variants = [
    ['platform-windows'],
    
]




def commands():
    """   """
    import os

    env.golaem_LICENSE.set("5053@rlm.cashmere.com")

    module_path = getenv("MAYA_MODDULE_PATH")
    golaem_module_path = os.path.join(module_path, "golaem/2016")

    env.MAYA_MODULE_PATH.append(golaem_module_path)

    env.PATH.append(os.path.join(golaem_module_path, "bin"))
    env.PATH.append(os.path.join(golaem_module_path, "plug-ins"))
    env.PATH.append(os.path.join(golaem_module_path, "procedurals"))

    env.LD_LIBRARY_PATH.append(os.path.join(golaem_module_path, "bin"))
    env.LD_LIBRARY_PATH.append(os.path.join(golaem_module_path, "plug-ins"))
    env.LD_LIBRARY_PATH.append(os.path.join(golaem_module_path, "procedurals"))