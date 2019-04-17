# -*- coding: utf-8 -*-
name = 'ocaml'
version = '4.02.1'
author = ['ocaml']

requires = []
variants = []



def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]

    ocaml_path = os.path.join(develop_path, "ocaml", "%s" % version).replace('/', os.sep)

    env.PATH.append(os.path.join(ocaml_path, "bin").replace('/', os.sep))
    # OCAMLC
    # OCAMLFIND
    # OCAMLOPT
    # OCAML_LIB
   
