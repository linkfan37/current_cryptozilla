import bpy

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.render.image_settings.file_format='PNG'
scene.render.filepath='C:\\Users\\flori\\Desktop\\blender.png'
bpy.ops.render.render(write_still=1)
