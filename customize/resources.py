import bpy
import os

from .. utils import (
    addon,
    files,
    paths,
)

class Resources():
    SOURCE_PATH = NotImplemented
    TARGET_PATH = NotImplemented

    @classmethod
    def load(cls):
        files.copy_files(cls.SOURCE_PATH, cls.TARGET_PATH)

    @classmethod
    def unload(cls):
        files.delete_files(os.listdir(cls.SOURCE_PATH), cls.TARGET_PATH)


class StudioResources(Resources):
    @classmethod
    def load(cls):
        super().load()
        bpy.context.preferences.studio_lights.refresh()

    @classmethod
    def unload(cls):
        super().unload()
        bpy.context.preferences.studio_lights.refresh()


# Use upercase names for classes that will be called by updating their correspoding 
# property in the addon preferences (prop: studio_lights class_name: STUDIO_LIGHTS).

class THEMES(Resources):
    SOURCE_PATH = paths.AddonPaths.themes
    TARGET_PATH = paths.BlenderPaths.themes


class MATCAPS(StudioResources):
    SOURCE_PATH = paths.AddonPaths.matcaps
    TARGET_PATH = paths.BlenderPaths.matcaps


class HDRIS(StudioResources):
    SOURCE_PATH = paths.AddonPaths.hdri
    TARGET_PATH = paths.BlenderPaths.hdri


class STUDIO_LIGHTS(StudioResources):
    SOURCE_PATH = paths.AddonPaths.studiolights
    TARGET_PATH = paths.BlenderPaths.studiolights


def register():
    prefs = addon.prefs()

    MATCAPS.load()       if prefs.matcaps       else MATCAPS.unload()
    HDRIS.load()         if prefs.hdris         else HDRIS.unload()
    STUDIO_LIGHTS.load() if prefs.studio_lights else STUDIO_LIGHTS.unload()
    # THEMES.load()       if prefs.themes        else THEMES.unload()


def unregister():
    if isinstance(bpy.context.space_data, bpy.types.SpacePreferences):
        MATCAPS.unload()
        HDRIS.unload()
        STUDIO_LIGHTS.unload()
        # THEMES.unload()