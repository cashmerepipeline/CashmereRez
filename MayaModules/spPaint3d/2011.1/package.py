# -*- coding: utf-8 -*-

name = 'spPaint3d'

version = '2011.1'

description = 'modeling env'

authors = []

tools = []

requires = []

def commands():
    import os
    base_path = os.path.join(getenv("MAYA_MODDULE_PATH"), "spPaint3d", '2011.1')
    env.PYTHONPATH.append(base_path)
    env.XBMLANGPATH.append(base_path+'/spPaint3d/icons')




