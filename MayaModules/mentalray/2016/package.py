name = "mentalray"

version = "2016"

authors = [
    "Autodesk"
]

description = \
    """
    mentalray
    """

requires = []



variants = [["platform-windows"], ["platform-linux"]]
def commands():
    root_path = "W:/SoftwareRepo/MayaModules/mentalray/2016"
    env.MENTALRAY_LOCATION = root_path
    env.PATH.append(root_path+"/bin")
    env.MENTALRAY_BIN_LOCATION = root_path+"/bin"
    env.MENTALRAY_SHADERS_LOCATION = root_path+"/shaders"
    env.MENTALRAY_INCLUDE_LOCATION = root_path+"/shaders/include"
    env.MI_CUSTOM_SHADER_PATH = root_path+"/shaders/include"
    env.IMF_PLUG_IN_PATH.append(root_path+"/bin/image")
    env.MAYA_PLUG_IN_PATH.append(root_path+"/plug-ins")
    env.MAYA_PLUG_IN_RESOURCE_PATH.append(root_path+"/resources")
    env.MAYA_RENDER_DESC_PATH.append(root_path+"/rendererDesc")
    env.MAYA_SCRIPT_PATH.append(root_path+"/scripts/AETemplates")
    env.MAYA_SCRIPT_PATH.append(root_path+"/scripts/mentalray")
    env.MAYA_SCRIPT_PATH.append(root_path+"/scripts/unsupported")
    env.MAYA_SCRIPT_PATH.append(root_path+"/scripts")
    
    env.MAYA_PRESET_PATH.append(root_path+"/presets/attrPresets")
    env.MAYA_PRESET_PATH.append(root_path+"/presets/attrPresets/mia_material")
    env.MAYA_PRESET_PATH.append(root_path+"/presets/attrPresets/mia_material_x")
    env.MAYA_PRESET_PATH.append(root_path+"/presets/attrPresets/mia_material_x_passes")
    env.MAYA_PRESET_PATH.append(root_path+"/presets")
    
    env.XBMLANGPATH.append(root_path+"/icons")
    
    env.PYTHONPATH.append(root_path+"/scripts/AETemplates")
    env.PYTHONPATH.append(root_path+"/scripts/mentalray")
    env.PYTHONPATH.append(root_path+"/scripts/unsupported")
    env.PYTHONPATH.append(root_path+"/scripts")

    
