# -*- coding: utf-8 -*-
name = 'sppas'
version = '1.9.7'
author = ['sppas']
variants = []

requires = ["python-intel2",
            "julius",
            "wxpython-3"]



def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    env.SPPAS_BIN = os.path.join(develop_path, "sppas", "%s" % version, "sppas", "bin").replace("/", os.sep)
    env.PATH.prepend(os.path.join(develop_path, "sppas", "%s" % version).replace("/", os.sep))

