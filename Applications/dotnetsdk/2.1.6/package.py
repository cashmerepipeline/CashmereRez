# -*- coding: utf-8 -*-

name = 'dotnetsdk'

version = '2.1.6'

author = ['microsoft']

tools = ["dotnet"]

requires = [] 

variants = [
            ['platform-windows'],
             
            ]



def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]

    env.PATH.append(os.path.join(applications_path, "dotnetsdk", "%s"%version).replace('/', os.sep))



