# -*- coding: utf-8 -*-
name = 'perl'
version = '5.20.2'
author = ['perl']

requires = []
variants = []



def commands():
    import os
    develop_path = os.environ["APPLICATIONS_PATH"]
    perl_path = os.path.join(develop_path, "perl", "%s" % version).replace('/', os.sep)

    env.PATH.append(os.path.join(perl_path, "bin").replace('/', os.sep))
       

