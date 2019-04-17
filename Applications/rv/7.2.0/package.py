name = "rv"

version = "7.2.0"

authors = [
    "rv"
]

description = \
    """
    rv
    """

# tools = [
    # "maya"
# ]

requires = []



variants = [["platform-windows"],["platform-linux"]]

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    env.PATH.append(os.path.join(applications_path, "rv", "%s"%version).replace("/", os.sep))
