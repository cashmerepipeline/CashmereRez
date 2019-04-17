# -*- coding: utf-8 -*-

name = 'MGTools'

version = '2.0'

description = 'modeling env'

tools = []

requires = []

def commands():
    import os
    import os
    base_path = os.path.join(getenv("MAYA_MODDULE_PATH"), "MGTools", 'mel')
    env.MG_TOOL_PATH = base_path+'/MGTools'
    env.PYTHONPATH.append(base_path+'/scripts')
    env.PYTHONPATH.append(base_path)
    env.MAYA_SCRIPT_PATH.append(base_path+'/scripts')
    env.MAYA_SCRIPT_PATH.append(base_path)




