# -*- coding: utf-8 -*-
name = 'llvm'
version = '5.0.1'
author = ['llvm']

requires = []
variants = []



def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]

    llvm_path = os.path.join(develop_path, "llvm", "%s" % version).replace('/', os.sep)

    env.LLVM_DIR = os.path.join(llvm_path, 'lib', 'cmake', 'llvm').replace('/', os.sep)
    env.PATH.append(os.path.join(llvm_path, "bin").replace('/', os.sep))
    
    env.INCLUDE.append(os.path.join(llvm_path, "include").replace('/', os.sep))
    env.LIB.append(os.path.join(llvm_path, "lib").replace('/', os.sep))
   

