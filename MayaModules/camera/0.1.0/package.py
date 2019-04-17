name = 'camera'

version = '0.1.0'

authors = ["YanGang"]

description = "rigged camera"

tools = []

requires = []

def commands():
    import os

    env.RIGGED_CAMERA.set(os.path.join("{this.root}", "cameras"))

