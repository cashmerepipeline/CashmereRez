# -*- coding: utf-8 -*-

name = 'dotnetruntime'

version = '2.0.5'

author = ['microsoft']

tools = ["dotnet"]

requires = [] 

variants = [
            ['platform-windows'],
             
            ]



def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]

    env.PATH.append(os.path.join(applications_path, "dotnetruntime", "%s"%version).replace('/', os.sep))



