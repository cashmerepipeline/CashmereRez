# -*- coding: utf-8 -*-

name = 'riggingcfg'

version = '0.0.1'

description = 'rigging'

authors = ['YanGang']

tools = []

requires = []

def commands():
    import os

    configs_path = os.environ["RIGGIN_CONFIGS_PATH"]
    anim_configs_path = os.path.join(configs_path, "animtioncfg", "%s" % version).replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(anim_configs_path, 'scripts').replace("/", os.sep))
    env.MAYA_SCRIPT_PATH.append(os.path.join(anim_configs_path, 'scripts').replace("/", os.sep))




