# -*- coding: utf-8 -*-

name = 'arnold'

version = '5.0.0'

author = ['solidangle']

tools = []

requires = []

variants = [
    ['platform-windows'],
    
]




def commands():
    """   """
    import os

    env.solidangle_LICENSE.set("5053@rlm.cashmere.com")

    module_path = getenv("MAYA_MODDULE_PATH")
    arnold_module_path = os.path.join(module_path, "solidangle/mtoadeploy/2017".replace('/', os.sep))

    env.MAYA_MODULE_PATH.append(arnold_module_path)

    env.PATH.append(os.path.join(arnold_module_path, "bin"))
    env.PATH.append(os.path.join(arnold_module_path, "plug-ins"))

    env.LD_LIBRARY_PATH.append(os.path.join(arnold_module_path, "bin"))
    env.LD_LIBRARY_PATH.append(os.path.join(arnold_module_path, "plug-ins"))

    # env.THIS_MODULES_DIR.set("{this.root}/modules")

    # modules_dir = expandvars("{this.root}/modules")
    # module_list = os.listdir(modules_dir)
    # for module in module_list:
    #     env.MAYA_MODULE_PATH.append(os.path.join(modules_dir, module))

    # print(getenv("MAYA_MODULE_PATH"))
    # unsetenv("THIS_MODULES_DIR")
