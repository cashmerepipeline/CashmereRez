# -*- coding: utf-8 -*-

name = 'lightingcfg'

version = '0.0.1'

description = 'lightin configs'

authors = ['YanGang']

tools = []

requires = []

def commands():
    import os

    configs_path = os.environ["CONFIGS_PATH"]
    light_configs_path = os.path.join(configs_path, "lightingcfg", "%s" % version).replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(light_configs_path, 'scripts').replace("/", os.sep))
    env.MAYA_SCRIPT_PATH.append(os.path.join(light_configs_path, 'scripts').replace("/", os.sep))
