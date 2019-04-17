# -*- coding: utf-8 -*-

name = 'animationcfg'

version = '0.0.1'

description = 'Animation Config'

authors = ['YanGang']

tools = []

requires = []

def commands():
    import os

    configs_path = os.environ["ANIMAITION_CONFIGS_PATH"]
    animation_configs_path = os.path.join(configs_path, "animtioncfg", "%s"%version).replace("/", os.sep)
