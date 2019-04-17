# -*- coding: utf-8 -*-

name = 'compositioncfg'

version = '0.0.1'

description = 'Composition Config'

authors = ['YanGang']

tools = []

requires = []

def commands():
    import os

    configs_path = os.environ["COMPSITION_CONFIGS_PATH"]
    compositon_configs_path = os.path.join(configs_path, "compositioncfg", "%s" % version).replace("/", os.sep)
