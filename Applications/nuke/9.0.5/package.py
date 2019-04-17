# -*- coding: utf-8 -*-

name = 'nuke'

version = '9.0.5'

author = ['The Foundry']

# tools = ['Nuke9.0']

# requires = ["nukeplugins-9.0",
            # "ofxplugins"]

variants = []



def commands():
    """   """
    # import os

    # env.REZ_NUKE_VERSION.set("9.0") 
    # env.foundry_LICENSE.set("5053@rlm.cashmere.com")

    # root_path = expandvars('{this.root}')
    
    # env.NUKE_LOCATION.set(os.path.join(root_path, 'nuke'))

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
    
    
    env.PATH.append('C:/Program Files/Nuke9.0v5')
    env.PATH.append(this.root)
    # env.PATH.append("{this.root}/nuke".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/plugins".replace("/", os.sep))

    # env.PATH.append("{this.root}/nuke/qtplugins/accessible".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/qtplugins/codecs".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/qtplugins/designer".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/qtplugins/graphicssystems".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/qtplugins/iconengines".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/qtplugins/imageformats".replace("/", os.sep))
    # env.PATH.append("{this.root}/nuke/qtplugins/sqldrivers".replace("/", os.sep))

    # alias have problem, use the bat files
    # alias("nuke", "Nuke10.5")
    # alias("nukex", "Nuke10.5 --nukex")
    # alias("nukes", "Nuke10.5 --studio")
    # alias("nukestudio", "Nuke10.5 --studio")
    # alias("hiero", "Nuke10.5 --hiero")
    # alias("hierop", "Nuke10.5 --player")
    # alias("hieroplayer", "Nuke10.5 --player")

    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/accessible")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/codecs")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/designer")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/graphicssystems")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/iconengines")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/imageformats")
    # env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/sqldrivers")

    # env.PYTHONPATH.append('{this.root}/nuke/pythonextensions/site-packages'.replace("/", os.sep))
