# v1.5

import bpy
import os
# from .. utils.preferences import get_prefs
# from .. utils.update_preference


maya_navigation_keymaps = []
loop_selection_keymaps = []
deselect_with_ctrl_keymaps = []
transform_with_gizmos_keymaps = []
smart_tab_keymaps = []
sculpting_setup_keymaps = []
operator_shortcuts_keymaps = []

wm = bpy.context.window_manager
kc = wm.keyconfigs.addon


def kmi_props(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
        
    except AttributeError:
        print(f'Warning: property {attr} not found in keymap item {kmi_props.__class__.__name__}')

    except Exception as e:
        print(f'Warning: {e}')


def create_kmi(idname, key, event, ctrl=False, alt=False, shift=False):
    kmi = km.keymap_items.new(idname, key, event, ctrl=ctrl, alt=alt, shift=shift)
    keymap_list.append((km, kmi))

    return kmi


def register_maya_navigation():
    global km, keymap_list
    keymap_list = maya_navigation_keymaps

    km = kc.keymaps.new('3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False)

    create_kmi('view3d.rotate', 'LEFTMOUSE',   'CLICK_DRAG', alt=True)
    create_kmi('view3d.move',   'MIDDLEMOUSE', 'PRESS', alt=True)
    create_kmi('view3d.zoom',   'RIGHTMOUSE',  'PRESS', alt=True)

    # print('ENABLED Maya Navigation')


def register_loop_selection():
    global km, keymap_list
    keymap_list = loop_selection_keymaps

    km = kc.keymaps.new(name='Mesh')

    # Loop Select
    kmi = create_kmi('mesh.loop_select', 'LEFTMOUSE', 'DOUBLE_CLICK')
    kmi_props(kmi.properties, 'extend',   False)
    kmi_props(kmi.properties, 'deselect', False)
    kmi_props(kmi.properties, 'toggle',   False)

    # Loop Select ADD
    kmi = create_kmi('mesh.loop_select', 'LEFTMOUSE', 'DOUBLE_CLICK', shift=True)
    kmi_props(kmi.properties, 'extend',   True)
    kmi_props(kmi.properties, 'deselect', False)
    kmi_props(kmi.properties, 'toggle',   False)

    # Loop Select REMOVE
    kmi = create_kmi('mesh.loop_select', 'LEFTMOUSE', 'DOUBLE_CLICK', ctrl=True)
    kmi_props(kmi.properties, 'extend',   False)
    kmi_props(kmi.properties, 'deselect', True)
    kmi_props(kmi.properties, 'toggle',   False)

    # print('ENABLED Select Loops with Double CLick')

    
def register_deselect_with_ctrl():
    global km, keymap_list
    keymap_list = deselect_with_ctrl_keymaps

    km = kc.keymaps.new(name='Object Mode')
    create_kmi('armored.deselect', 'LEFTMOUSE', 'CLICK', ctrl=True)

    km = kc.keymaps.new(name='Mesh')
    create_kmi('armored.deselect', 'LEFTMOUSE', 'CLICK', ctrl=True)

    km = kc.keymaps.new('Curve', space_type='EMPTY', region_type='WINDOW', modal=False)
    create_kmi('armored.deselect', 'LEFTMOUSE', 'CLICK', ctrl=True)

    # print('ENABLED Deselect with Ctrl')


def register_transform_with_gizmos():
    global km, keymap_list
    keymap_list = transform_with_gizmos_keymaps

    km = kc.keymaps.new('3D View Generic', space_type='VIEW_3D', region_type='WINDOW', modal=False)
    # create_kmi('wm.tool_set_by_id', 'G', 'PRESS').properties.name = 'builtin.move'
    # create_kmi('wm.tool_set_by_id', 'R', 'PRESS').properties.name = 'builtin.rotate'
    # create_kmi('wm.tool_set_by_id', 'S', 'PRESS').properties.name = 'builtin.scale'
    # create_kmi('view3d.armored_toggle_transform_tool', 'G', 'PRESS').properties.tool = 'builtin.move'
    create_kmi('view3d.armored_toggle_transform_tool', 'R', 'PRESS').properties.tool = 'builtin.rotate'
    create_kmi('view3d.armored_toggle_transform_tool', 'S', 'PRESS').properties.tool = 'builtin.scale'

    # print('ENABLED Transform with Gizmos')


def register_smart_tab():
    global km, keymap_list
    keymap_list = smart_tab_keymaps

    km = kc.keymaps.new('Object Non-modal')
    create_kmi('armored.mode_toggle', 'TAB', 'PRESS')

    # print('ENABLED Smart TAB')


def register_sculpting_setup():
    global km, keymap_list
    keymap_list = sculpting_setup_keymaps

    km = kc.keymaps.new(name='Sculpt')

    create_kmi('view3d.view_center_pick', 'F', 'PRESS', alt=True)
    create_kmi('view3d.view_center_pick', 'C', 'PRESS')
    # create_kmi('view3d.view_center_pick', 'SPACE', 'PRESS')
    create_kmi('view3d.armored_smart_subdivide', 'D', 'PRESS', ctrl=True)
    # create_kmi('transform.translate', 'G', 'PRESS')
    # create_kmi('view3d.armored_toggle_transform_tool', 'W', 'PRESS').properties.tool = 'builtin.move'

    # Invert brush stroke (set to ALT instead of CTRL)
    create_kmi('sculpt.brush_stroke', 'LEFTMOUSE', 'PRESS', alt=True).properties.mode = 'INVERT'

    # BRUSHES
    create_kmi('wm.tool_set_by_id', 'ONE',   'PRESS'          ).properties.name = 'builtin_brush.Clay Strips'
    create_kmi('wm.tool_set_by_id', 'ONE',   'PRESS', alt=True).properties.name = 'builtin_brush.Clay'

    create_kmi('wm.tool_set_by_id', 'TWO',   'PRESS'          ).properties.name = 'builtin_brush.Draw Sharp'
    create_kmi('wm.tool_set_by_id', 'TWO',   'PRESS', alt=True).properties.name = 'builtin_brush.Draw'

    create_kmi('wm.tool_set_by_id', 'THREE', 'PRESS'          ).properties.name = 'builtin_brush.Scrape'
    create_kmi('wm.tool_set_by_id', 'THREE', 'PRESS', alt=True).properties.name = 'builtin_brush.Flatten'

    create_kmi('wm.tool_set_by_id', 'FOUR',  'PRESS'          ).properties.name = 'builtin_brush.Grab'
    create_kmi('wm.tool_set_by_id', 'FOUR',  'PRESS', alt=True).properties.name = 'builtin_brush.Snake Hook'

    create_kmi('wm.tool_set_by_id', 'FIVE',  'PRESS'          ).properties.name = 'builtin_brush.Crease'
    create_kmi('wm.tool_set_by_id', 'FIVE',  'PRESS', alt=True).properties.name = 'builtin_brush.Inflate'

    create_kmi('wm.context_toggle',  'W', 'PRESS', shift=True).properties.data_path = 'space_data.overlay.show_wireframes'


def register_operator_shortcuts():
    global km, keymap_list
    keymap_list = operator_shortcuts_keymaps

    def global_focus_key():
        create_kmi('mesh.armored_focus', 'F','PRESS')

    def Global_Keys():
        create_kmi('screen.userpref_show', 'COMMA', 'PRESS', ctrl=True)

    km = kc.keymaps.new('Window', space_type='EMPTY', region_type='WINDOW', modal=False)
    create_kmi('script.reload', 'F5', 'PRESS')


    # Generic (doesn't work unless separate from 3D View)
    km = kc.keymaps.new('3D View Generic', space_type='VIEW_3D', region_type='WINDOW', modal=False)
    create_kmi('screen.redo_last', 'T', 'PRESS')


    km = kc.keymaps.new('3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False)
    Global_Keys()

    create_kmi('view3d.zoom_border', 'F',            'PRESS', ctrl=True, shift=True)
    create_kmi('view3d.zoom_border', 'BUTTON4MOUSE', 'PRESS')

    # create_kmi('wm.tool_set_by_id', 'Q', 'PRESS')        .properties.name = 'builtin.select_box'
    create_kmi('view3d.armored_paint_select', 'Q', 'PRESS') # Tapping this will activate select_box instead.
    create_kmi('wm.call_menu_pie', 'Q', 'DOUBLE_CLICK') .properties.name = 'ARMORED_MT_PIE_select'

    create_kmi('wm.context_toggle',  'W', 'PRESS', shift=True).properties.data_path = 'space_data.overlay.show_wireframes'
    create_kmi('wm.context_toggle',  'W', 'PRESS', alt=True  ).properties.data_path = 'space_data.overlay.show_overlays'

    create_kmi('view3d.armored_toggle_transform_tool', 'W', 'PRESS').properties.tool = 'builtin.move'
    # create_kmi('view3d.armored_toggle_transform_tool', 'S', 'PRESS').properties.tool = 'builtin.scale'
    # create_kmi('view3d.armored_toggle_transform_tool', 'R', 'PRESS').properties.tool = 'builtin.rotate'

    create_kmi('view3d.armored_open_most_recent',  'R', 'PRESS', alt=True,  shift=True)
    create_kmi('view3d.armored_autosmooth',        'A', 'PRESS', ctrl=True, shift=True)
    create_kmi('object.armored_rest_on_ground',    'R', 'PRESS', ctrl=True)

    create_kmi('view3d.armored_toggle_cavity',     'C', 'PRESS', alt=True)
    create_kmi('view3d.armored_cycle_cavity_type', 'C', 'PRESS', alt=True, shift=True)
    create_kmi('view3d.armored_smart_loopcut',     'C', 'PRESS')
    # create_kmi('view3d.armored_subdivide',         'D', 'PRESS', ctrl=True)
    create_kmi('view3d.armored_smart_subdivide',         'D', 'PRESS', ctrl=True)

    create_kmi('view3d.armored_single_subdivision_level', 'PAGE_UP',   'PRESS').properties.action = 'INCREASE'
    create_kmi('view3d.armored_single_subdivision_level', 'PAGE_DOWN', 'PRESS').properties.action = 'DECREASE'
    

    km = kc.keymaps.new(name='Object Mode')
    Global_Keys()
    global_focus_key()

    create_kmi('object.delete', 'X', 'PRESS').properties.confirm = False

    kmi = create_kmi('object.move_to_collection', 'N', 'PRESS', shift=True)
    kmi_props(kmi.properties, 'collection_index', 0)
    kmi_props(kmi.properties, 'is_new', True)


    km = kc.keymaps.new(name='Mesh')
    Global_Keys()
    global_focus_key()

    create_kmi('mesh.faces_select_linked_flat', 'F', 'PRESS', shift=True)
    create_kmi('mesh.edge_face_add',            'F', 'PRESS', alt=True)
    create_kmi('mesh.f2',                       'F', 'PRESS', alt=True) # Same keymap as above, but seems to take prio if f2 is installed and viceversa.

    create_kmi('mesh.armored_extract',    'E', 'PRESS', ctrl=True, shift=True)
    create_kmi('mesh.armored_duplicate',  'D', 'PRESS', ctrl=True, shift=True)

    create_kmi('transform.shrink_fatten', 'S', 'PRESS', alt=True).properties.use_even_offset = True
    
    create_kmi('mesh.armored_select_adjacent',  'HOME',         'PRESS', shift=True)
    create_kmi('mesh.armored_select_adjacent',  'WHEELUPMOUSE', 'PRESS', ctrl=True, shift=True)

    create_kmi('mesh.armored_fast_bevel', 'B', 'PRESS')
    create_kmi('mesh.bridge_edge_loops',  'B', 'PRESS', shift=True)

    create_kmi('object.armored_rest_on_ground', 'R', 'PRESS', ctrl=True)
    create_kmi('mesh.loop_multi_select',        'R', 'PRESS', alt=True).properties.ring = True # Fallback for the next entry.
    create_kmi('mesh.armored_select_edge_ring', 'R', 'PRESS', alt=True) 

    create_kmi('mesh.armored_connect',     'C',    'PRESS', shift=True)
    create_kmi('mesh.armored_align_verts', 'V',    'PRESS', shift=True)

    create_kmi('mesh.armored_crease', 'BUTTON5MOUSE', 'PRESS', shift=True).properties.crease_mode = 'CREASE'
    create_kmi('mesh.armored_crease', 'BUTTON4MOUSE', 'PRESS', shift=True).properties.crease_mode = 'UNCREASE'
    create_kmi('mesh.armored_crease', 'NUMPAD_PLUS',  'PRESS', shift=True).properties.crease_mode = 'CREASE'
    create_kmi('mesh.armored_crease', 'NUMPAD_MINUS', 'PRESS', shift=True).properties.crease_mode = 'UNCREASE'

    create_kmi('mesh.select_linked_pick', 'LEFTMOUSE', 'DOUBLE_CLICK', alt=True )           .properties.deselect = False
    create_kmi('mesh.select_linked_pick', 'LEFTMOUSE', 'DOUBLE_CLICK', alt=True, shift=True).properties.deselect = True
    
    create_kmi('mesh.select_more','WHEELUPMOUSE',   'PRESS', shift=True)
    create_kmi('mesh.select_less','WHEELDOWNMOUSE', 'PRESS', shift=True)

    create_kmi('mesh.region_to_loop', 'FIVE',         'PRESS', alt=True)
    create_kmi('mesh.region_to_loop', 'BUTTON5MOUSE', 'PRESS')

    create_kmi('mesh.armored_subd_toggle', 'ONE',   'PRESS', alt=True).properties.mode = 'OFF'
    create_kmi('mesh.armored_subd_toggle', 'TWO',   'PRESS', alt=True).properties.mode = 'HYBRID'
    create_kmi('mesh.armored_subd_toggle', 'THREE', 'PRESS', alt=True).properties.mode = 'FULL'

    create_kmi('mesh.armored_center_vertices', 'X', 'PRESS', ctrl=True, alt=True).properties.axis = 'X'
    create_kmi('mesh.armored_center_vertices', 'Y', 'PRESS', ctrl=True, alt=True).properties.axis = 'Y'
    create_kmi('mesh.armored_center_vertices', 'Z', 'PRESS', ctrl=True, alt=True).properties.axis = 'Z'

    # SubD Hotkeys for Edit Mode
    create_kmi('object.subdivision_set', 'ZERO',  'PRESS', ctrl=True).properties.level = 0
    create_kmi('object.subdivision_set', 'ONE',   'PRESS', ctrl=True).properties.level = 1
    create_kmi('object.subdivision_set', 'TWO',   'PRESS', ctrl=True).properties.level = 2
    create_kmi('object.subdivision_set', 'THREE', 'PRESS', ctrl=True).properties.level = 3
    create_kmi('object.subdivision_set', 'FOUR',  'PRESS', ctrl=True).properties.level = 4
    create_kmi('object.subdivision_set', 'FIVE',  'PRESS', ctrl=True).properties.level = 5
    create_kmi('object.subdivision_set', 'SIX',   'PRESS', ctrl=True).properties.level = 6
    create_kmi('object.subdivision_set', 'SEVEN', 'PRESS', ctrl=True).properties.level = 7
    create_kmi('object.subdivision_set', 'EIGHT', 'PRESS', ctrl=True).properties.level = 8
    create_kmi('object.subdivision_set', 'NINE',  'PRESS', ctrl=True).properties.level = 9


    km = kc.keymaps.new('Curve', space_type='EMPTY', region_type='WINDOW', modal=False)
    Global_Keys()
    global_focus_key()

    create_kmi('curve.shortest_path_pick', 'LEFTMOUSE', 'PRESS', ctrl=True, shift=True)
    # create_kmi('curve.draw', 'LEFTMOUSE', 'PRESS', alt=True)


# Property Editor
    # km = kc.keymaps.new('Property Editor', space_type='PROPERTIES', region_type='WINDOW', modal=False)

    # Works for other key combos, like CTRL+Shift, but not for Shift Only.
    # create_kmi('screen.space_context_cycle', 'WHEELUPMOUSE',   'PRESS', shift=True).properties.direction = 'PREV'
    # create_kmi('screen.space_context_cycle', 'WHEELDOWNMOUSE', 'PRESS', shift=True).properties.direction = 'NEXT'


    km = kc.keymaps.new('Window', space_type='EMPTY', region_type='WINDOW', modal=False)
    Global_Keys()
    # create_kmi('wm.search_menu', 'SPACE', 'PRESS')
    

    km = kc.keymaps.new('Outliner', space_type='OUTLINER', region_type='WINDOW', modal=False)
    Global_Keys()
    create_kmi('outliner.show_active', 'F', 'PRESS', ctrl=True, shift=True)

    # print('ENABLED Operator Keymaps')


def unregister_keymaps(prop):
    listname = prop + '_keymaps'
    keymaps_list = eval(prop + '_keymaps')
    name = prop.replace('_', ' ').title()

    # print(f'Unregistering {name} Keymaps >>')
    
    for km, kmi in keymaps_list:
        # print(f'    unregistered: {kmi}')
        try:
            km.keymap_items.remove(kmi)
        except RuntimeError as e:
            pass
            # print(f'ARMORED Toolkit [INFO]: Probably an F2 Exception')

    keymaps_list.clear()

    # print(f'DISABLED {name}')


def register():
    '''Not sure if loading properties from config.ini file automatically triggers their update function
    and registration, but I still have to check them anyway in case some properties have not been
    written to config.ini in the first place'''

    from .. utils import addon 
    addon.load_config()

    if  addon.preferences().maya_navigation:
        register_maya_navigation()

    if addon.preferences().loop_selection:
        register_loop_selection()
        
    if addon.preferences().deselect_with_ctrl:
        register_deselect_with_ctrl()

    if addon.preferences().transform_with_gizmos:
        register_transform_with_gizmos()

    if addon.preferences().smart_tab:
        register_smart_tab()

    if addon.preferences().sculpting_setup:
        register_sculpting_setup()

    if addon.preferences().operator_shortcuts:
        register_operator_shortcuts()


def unregister():
    # Just Unregister everything. This works because unregister_keymaps() is based on keymap lists.
    # If the keymaps are disabled the lists will be empty, so nothing will be done.
    
    unregister_keymaps('maya_navigation')
    unregister_keymaps('loop_selection')
    unregister_keymaps('deselect_with_ctrl')
    unregister_keymaps('transform_with_gizmos')
    unregister_keymaps('smart_tab')
    unregister_keymaps('sculpting_setup')
    unregister_keymaps('operator_shortcuts')