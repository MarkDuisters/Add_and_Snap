#Addon metadata
bl_info = {
    "name": "Add and Snap Objects",
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Mark duisters",
    "version": (1, 0, 0),
    "description": "Adds and snaps an object to the last selected object",
    "location": "View3D > UI > Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
}


import bpy
from bpy.types import Panel, Operator

class OBJECT_OT_add_and_snap(Operator):
    bl_idname = "object.add_and_snap"
    bl_label = "Add"
    
    object_type: bpy.props.StringProperty()
    
    def execute(self, context):
        # Store the active object
        active_obj = context.view_layer.objects.active
        
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # the new object based on the type
        if self.object_type == 'CUBE':
            bpy.ops.mesh.primitive_cube_add()
        elif self.object_type == 'SPHERE':
            bpy.ops.mesh.primitive_uv_sphere_add()
        elif self.object_type == 'CYLINDER':
            bpy.ops.mesh.primitive_cylinder_add()
        elif self.object_type == 'CONE':
            bpy.ops.mesh.primitive_cone_add()
        elif self.object_type == 'TORUS':
            bpy.ops.mesh.primitive_torus_add()
        elif self.object_type == 'PLANE':
            bpy.ops.mesh.primitive_plane_add()
        elif self.object_type == 'LIGHT_POINT':
            bpy.ops.object.light_add(type='POINT')
        elif self.object_type == 'LIGHT_SUN':
            bpy.ops.object.light_add(type='SUN')
        elif self.object_type == 'LIGHT_SPOT':
            bpy.ops.object.light_add(type='SPOT')
        elif self.object_type == 'LIGHT_AREA':
            bpy.ops.object.light_add(type='AREA')
        
        # Get the newly created object
        new_obj = context.view_layer.objects.active
        
        # Select both the active object and the new object
        active_obj.select_set(True)
        new_obj.select_set(True)
        
        # Make the previously active object active again
        context.view_layer.objects.active = active_obj
        
        # Snap the new object to the active object
        bpy.ops.view3d.snap_selected_to_active()
        
        return {"FINISHED"}

class OBJECT_PT_OBJECT_OT_add_and_snap(Panel):
    bl_idname = "OBJECT_PT_OBJECT_OT_add_and_snap_panel"
    bl_label = "Add 'n Snap"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools"
    bl_context = "objectmode"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        layout.separator()
        
        layout.label(text="Mesh:")
        layout.operator("object.add_and_snap", text="Cube", icon="MESH_CUBE").object_type = 'CUBE'
        layout.operator("object.add_and_snap", text="Sphere", icon="MESH_UVSPHERE").object_type = 'SPHERE'
        layout.operator("object.add_and_snap", text="Cylinder", icon="MESH_CYLINDER").object_type = 'CYLINDER'
        layout.operator("object.add_and_snap", text="Cone", icon="MESH_CONE").object_type = 'CONE'
        layout.operator("object.add_and_snap", text="Torus", icon="MESH_TORUS").object_type = 'TORUS'
        layout.operator("object.add_and_snap", text="Plane", icon="MESH_PLANE").object_type = 'PLANE'
        
        layout.separator()
        layout.label(text="Light:")
        layout.operator("object.add_and_snap", text="Point Light", icon="LIGHT_POINT").object_type = 'LIGHT_POINT'
        layout.operator("object.add_and_snap", text="Sun Light", icon="LIGHT_SUN").object_type = 'LIGHT_SUN'
        layout.operator("object.add_and_snap", text="Spot Light", icon="LIGHT_SPOT").object_type = 'LIGHT_SPOT'
        layout.operator("object.add_and_snap", text="Area Light", icon="LIGHT_AREA").object_type = 'LIGHT_AREA'

def register():
    bpy.utils.register_class(OBJECT_OT_add_and_snap)
    bpy.utils.register_class(OBJECT_PT_OBJECT_OT_add_and_snap)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_and_snap)
    bpy.utils.unregister_class(OBJECT_PT_OBJECT_OT_add_and_snap)

if __name__ == "__main__":
    register()
