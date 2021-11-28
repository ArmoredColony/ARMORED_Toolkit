import bpy
import os

from . import addon


class BlenderPaths():
    config       = bpy.utils.user_resource('CONFIG', create=True)

    scripts      = bpy.utils.user_resource('SCRIPTS', create=True)
    addons       = bpy.utils.user_resource('SCRIPTS', path='addons', create=True)
    startup      = bpy.utils.user_resource('SCRIPTS', path='startup', create=True)
    themes       = bpy.utils.user_resource('SCRIPTS', path=os.path.join('presets', 'interface_theme'), create=True)

    datafiles    = bpy.utils.user_resource('DATAFILES', create=True)
    matcaps      = bpy.utils.user_resource('DATAFILES', path=os.path.join('studiolights', 'matcap'), create=True)
    hdri         = bpy.utils.user_resource('DATAFILES', path=os.path.join('studiolights', 'world'), create=True)
    studiolights = bpy.utils.user_resource('DATAFILES', path=os.path.join('studiolights', 'studio'), create=True)
    


class AddonPaths():
    resources = os.path.join(addon.path(), 'resources')

    matcaps      = os.path.join(resources, 'matcaps')
    hdri         = os.path.join(resources, 'hdri')
    studiolights = os.path.join(resources, 'studiolights')
    themes       = os.path.join(resources, 'themes')
    materials    = os.path.join(resources, 'materials')

    operators    = os.path.join(addon.path(), 'operators')
    keymaps      = os.path.join(addon.path(), 'customize', 'keymaps.py')