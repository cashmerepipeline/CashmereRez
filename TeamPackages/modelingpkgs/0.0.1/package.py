# -*- coding: utf-8 -*-

name = 'modelingpkgs'

version = '0.0.1'

description = 'Modeling Packages'

authors = ['YanGang']

tools = []

requires = []

def commands():
    import os
    
    packages_path = os.path.join(getenv("TEAM_PACKAGES_PATH"), "modelingpkgs")

    env.PATH.append(os.path.join(packages_path, 'bin'))

    env.PYTHONPATH.append(os.path.join(packages_path,'python'))

    env.MAYA_SCRIPT_PATH.append(os.path.join(packages_path, 'scripts'))
    env.MAYA_PLUG_IN_PATH.append(os.path.join(packages_path,'plug-ins'))
    env.XBMLANGPATH.append(os.path.join(packages_path, 'icons'))





