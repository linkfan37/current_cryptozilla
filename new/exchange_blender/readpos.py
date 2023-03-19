import bpy
import json
import os
from os import path
from mathutils import *
from math import *

skinpath = "Z:\\home\\flo\\projekt\\new\\exchange_blender\\asset_gltfs\\"


bpy.ops.import_scene.gltf(filepath=skinpath+"test"+".gltf", files=[{"name":"test"+".gltf", "name":"test"+".gltf"}], loglevel=50)
bpy.ops.object.select_all(action="DESELECT")
loc = bpy.data.objects["Eyes-Local"].location

print(loc)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
