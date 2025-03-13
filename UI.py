# Panel to jest miejsce na UI w którym trzymamy przyciski, pola tekstowe, itp.
import bpy 
from . import random_shelf

class Panel_random_shelf(bpy.types.Panel):
    bl_idname = "OBJECT_PT_Panel_random_shelf"
    bl_label = "Random Shelf"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.operator('object.generate_shelf', text='Generate', icon='MESH_CUBE')
        layout.separator()
        layout.prop(context.scene, 'how_much_renders')
        layout.operator('object.render_shelf', text='Render Shelf')

classes = [
    Panel_random_shelf
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.how_much_renders = bpy.props.IntProperty(name="how_much_renders", default=1)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

        