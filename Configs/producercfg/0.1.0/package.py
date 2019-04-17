# -*- coding: utf-8 -*-

name = 'producercfg'

version = '0.0.1'

description = 'producer cfg'

authors = ['YanGang']

tools = []

requires = []

def commands():
    # pass
    import os

    configs_path = os.environ["PRODUCER_CONFIGS_PATH"]
    prod_configs_path = os.path.join(configs_path, "animtioncfg", "%s" % version).replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(prod_configs_path, 'scripts').replace("/", os.sep))
