# -*- coding: utf-8 -*-
name = 'cmake'
version = '3.10.2'
author = ['cmake']
variants = []



def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    cmake_path = os.path.join(develop_path, "cmake", "%s" % version).replace("/", os.sep)
    env.PATH.prepend(os.path.join(cmake_path, "bin").replace("/", os.sep))



