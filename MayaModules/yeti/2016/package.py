# -*- coding: utf-8 -*-

name = 'yeti'

version = '5.0.0'

author = ['yeti']

tools = []

requires = []

variants = [
    ['platform-windows'],
    
]




def commands():
    """   """
    import os

    env.yeti_LICENSE.set("5053@rlm.cashmere.com")

    module_path = getenv("MAYA_MODDULE_PATH")
    yeti_module_path = os.path.join(module_path, "yeti/2016".replace('/', os.sep))

    env.MAYA_MODULE_PATH.append(yeti_module_path)

    env.PATH.append(os.path.join(yeti_module_path, "yeti/bin".replace('/', os.sep)))
    env.PATH.append(os.path.join(yeti_module_path, "yeti/plug-ins".replace('/', os.sep)))

    env.LD_LIBRARY_PATH.append(os.path.join(yeti_module_path, "yeti/bin".replace('/', os.sep)))
    env.LD_LIBRARY_PATH.append(os.path.join(yeti_module_path, "yeti/bin".replace('/', os.sep)))

