name = 'assetlibrarypkgs'

version = '0.0.1'

authors = [    "YanGang"]

description = \
    """
    assetlibrarypkgs
    """

tools = []

requires = []

def commands():
    import os
    
    packages_path = os.path.join(getenv("TEAM_PACKAGES_PATH"), "assetlibrarypkgs")

    env.PATH.append(os.path.join(packages_path, 'bin'))

    env.PYTHONPATH.append(os.path.join(packages_path,'python'))

    env.MAYA_SCRIPT_PATH.append(os.path.join(packages_path, 'scripts'))
    env.MAYA_PLUG_IN_PATH.append(os.path.join(packages_path,'plug-ins'))
    env.XBMLANGPATH.append(os.path.join(packages_path, 'icons'))

