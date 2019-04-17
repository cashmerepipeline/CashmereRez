# -*- coding: utf-8 -*-

name = 'powershell'

version = '6.0.2'

author = ['microsoft']

tools = ["pwsh"]

requires = [] 

variants = [
            ['platform-windows'],
             
            ]



def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]

    env.PATH.append(os.path.join(applications_path, "powershell", "%s"%version).replace('/', os.sep))



