# -*- coding: utf-8 -*-

name = 'nuke'

version = '10.5.3'

author = ['The Foundry']

tools = ['Nuke10.5']

# requires = ["nukeplugins-10.5",
            # "ofxplugins"]

variants = []



def commands():
    """   """
    import os

    env.REZ_NUKE_VERSION.set("10.5") 
    env.foundry_LICENSE.set("5053@rlm.cashmere.com")

    applications_path = os.environ["APPLICATIONS_PATH"]
    nuke_root = os.path.join(applications_path, "nuke", "%s"%version).replace("/", os.sep)
    # env.NUKE_LOCATION.set(os.path.join(root_path, 'nuke'))
    env.NUKE_LOCATION.set(nuke_root)

    # nuke plugins dir
    # env.NUKE_PATH.append()

    # env.NUKE_TEMP_DIR.set()
    # env.OFX_PLUGIN_PATH.append()
    # env.NUKE_INTERACTIVE.append

    # env.NUKE_DISK_CACHE.set()
    # env.NUKE_DISK_CACHE_GB.set()
    # work on linux
    # env.NUKE_EXR_TEMP_DIR.set()
    
    # init.py and menu.py locations
    # env.STARTUP_PYTHON_PATH

    env.PATH.append(nuke_root)
    env.PATH.append(os.path.join(nuke_root, "plugins").replace("/", os.sep))

    env.PATH.append(os.path.join(nuke_root, "qtplugins/accessible").replace("/", os.sep))
    env.PATH.append(os.path.join(nuke_root, "qtplugins/codecs").replace("/", os.sep))
    env.PATH.append(os.path.join(nuke_root, "qtplugins/designer").replace("/", os.sep))
    env.PATH.append(os.path.join(nuke_root, "qtplugins/graphicssystems").replace("/", os.sep))
    env.PATH.append(os.path.join(nuke_root, "qtplugins/iconengines").replace("/", os.sep))
    env.PATH.append(os.path.join(nuke_root, "qtplugins/imageformats").replace("/", os.sep))
    env.PATH.append(os.path.join(nuke_root, "qtplugins/sqldrivers").replace("/", os.sep))

    # alias have problem, use the bat files
    # alias("nuke", "Nuke10.5")
    # alias("nukex", "Nuke10.5 --nukex")
    # alias("nukes", "Nuke10.5 --studio")
    # alias("nukestudio", "Nuke10.5 --studio")
    # alias("hiero", "Nuke10.5 --hiero")
    # alias("hierop", "Nuke10.5 --player")
    # alias("hieroplayer", "Nuke10.5 --player")

    env.LD_LIBRARY_PATH.prepend(nuke_root)
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/accessible"))
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/codecs"))
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/designer"))
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/graphicssystems"))
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/iconengines"))
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/imageformats"))
    env.LD_LIBRARY_PATH.prepend(os.path.join(nuke_root, "qtplugins/sqldrivers"))

    env.PYTHONPATH.append(os.path.join(nuke_root, 'pythonextensions/site-packages').replace("/", os.sep))
