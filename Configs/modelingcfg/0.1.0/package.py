# -*- coding: utf-8 -*-

name = 'producercfg'

version = '0.0.1'

description = 'producer cfg'

authors = ['YanGang']

tools = []

requires = [
    'maya',
    'workflow',
    'pyside'
]

def commands():
    # pass
    import os

    configs_path = os.environ["CONFIGS_PATH"]
    mdl_configs_path = os.path.join(configs_path, "animtioncfg", "%s" % version).replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(mdl_configs_path, 'scripts').replace("/", os.sep))
    env.MAYA_SCRIPT_PATH.append(os.path.join(mdl_configs_path, 'scripts').replace("/", os.sep))




