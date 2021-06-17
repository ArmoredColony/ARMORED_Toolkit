import bpy
import os
import contextlib

from bpy.app import handlers

from .. utils import addon


debug = False


@handlers.persistent
def apply_delay(*args):
    apply_system_preferences()
    handlers.load_post.remove(apply_delay)


@handlers.persistent
def reset_delay(*args):
    reset_system_preferences()
    handlers.load_post.remove(reset_delay)


def apply_system_preferences():
    bpy.context.preferences.view.show_splash = False
    bpy.context.preferences.view.show_tooltips_python = True
    bpy.context.preferences.view.show_developer_ui = True
    # bpy.context.preferences.view.smooth_view = 100
    bpy.context.preferences.inputs.drag_threshold_mouse = 1
    bpy.context.preferences.inputs.invert_mouse_zoom = True
    bpy.context.preferences.edit.undo_steps = 90

    if debug: 
        print('ENABLED Armored Preferences')


def reset_system_preferences():
    bpy.context.preferences.view.show_splash = True
    bpy.context.preferences.view.show_tooltips_python = False
    bpy.context.preferences.view.show_developer_ui = False
    # bpy.context.preferences.view.smooth_view = 200
    bpy.context.preferences.inputs.drag_threshold_mouse = 3
    bpy.context.preferences.inputs.invert_mouse_zoom = False
    bpy.context.preferences.edit.undo_steps = 32

    if debug: 
        print('RESET System Preferences.')


def register():
    # from .. utils import addon

    state = addon.preferences().system_preferences

    if state:
        handlers.load_post.append(apply_delay)
    else:
        handlers.load_post.append(reset_delay)


def unregister():
    if isinstance(bpy.context.space_data, bpy.types.SpacePreferences):
        reset_system_preferences()
        
        if debug: 
            print('Reset System Preferences because addon was Disabled')