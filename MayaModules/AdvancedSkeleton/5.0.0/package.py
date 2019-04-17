name = 'AdvancedSkeleton'

version = '5.0.0'

authors = ["AdvancedSkeleton"]

description = ""

tools = []

requires = []

def commands():
    import os
    module_path = os.path.join(
        getenv("MAYA_MODDULE_PATH"), "AdvancedSkeleton", 'python')
    env.PYTHONPATH.append(module_path)
    env.XBMLANGPATH.append(module_path+'/AdvancedSkeleton/icons')
