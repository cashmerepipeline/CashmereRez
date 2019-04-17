name = 'camera'

version = '0.1.0'

authors = [
    "YanGang",
    "YanGang"
]

description = \
    """
    rigged ready camera
    """

tools = []

requires = ['maya-2016']



def commands():
    import os

    env.RIGGED_CAMERA.set(os.path.join("{this.root}", "cameras"))

