import bpy
import random

class OT_Render_Shelf(bpy.types.Operator):
    bl_idname = "object.render_shelf"
    bl_label = "Render"
    bl_description = "Render image"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        for i in range(bpy.context.scene.how_much_renders):
            bpy.ops.render.render(use_viewport=True)
            bpy.data.images['Render Result'].save_render(filepath=f"{bpy.data.scenes['Scene'].render.filepath}/{i}.png")
        return {"FINISHED"}


class OT_Generate_Shelf(bpy.types.Operator):
    bl_idname = "object.generate_shelf"
    bl_label = "Generate"
    bl_description = "You can use this button to generate the random shelf!"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        spawners_collection = bpy.data.collections.get("Spawners")
        assets_collection = bpy.data.collections.get("Assets")
        generated_collection = bpy.data.collections.get("Generated")

        for obj in generated_collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)

        print("GENERATED COLLECTION HAS BEEN CLEANED!!!",len(generated_collection.objects))

        for obj in spawners_collection.objects:
            random_item = assets_collection.objects[random.randint(0, len(assets_collection.objects) - 1)]
            new_obj = random_item.copy()
            new_obj.data = random_item.data.copy()
            new_obj.location = obj.location
            generated_collection.objects.link(new_obj)

            # Add Array modifier to the new object
            array_modifier = new_obj.modifiers.new(name="Array", type='ARRAY')
            array_modifier.relative_offset_displace = (0, 1.1, 0.0)  # 1.2x szerokości obiektu
            array_modifier.count = 2  # Number of copies

        return {"FINISHED"}

classes = [
    OT_Generate_Shelf,
    OT_Render_Shelf
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)