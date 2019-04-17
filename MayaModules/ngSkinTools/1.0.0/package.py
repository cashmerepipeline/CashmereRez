name = 'ngSkinTools'

version = '1.0.0'

authors = ["YanGang"]

description = "ngSkinTools"

tools = []

requires = []


def commands():
    import os
    base_path = os.path.join(
        getenv("MAYA_MODDULE_PATH"), "ngSkinTools", 'python')

    env.MAYA_PLUG_IN_PATH.append(os.path.join(
        base_path, "plug-ins", 'maya-2016'))
    env.XBMLANGPATH.append(os.path.join(base_path, "icons"))
    env.PYTHONPATH.append(base_path)
