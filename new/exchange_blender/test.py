import bpy
import json
import os
from os import path
from mathutils import *
from math import *

assetpath = "Z:\\home\\flo\\projekt\\new\\exchange_blender\\asset_gltfs\\Assets\\"
skinpath = "Z:\\home\\flo\\projekt\\new\\exchange_blender\\asset_gltfs\\Assets\\Skin\\"

def exchange_mesh(exchangewith):
    objs = bpy.context.selected_objects[:]#selected objects
    myob = objs[0]
    assetmesh = objs[0].data
    

    scene = bpy.context.scene
    tmp = scene.objects[0]
    myfun = bpy.data.objects["Skull-Global"]

            
    for obj in scene.objects:
        mesh = obj.data
        #print(mesh)
        if mesh != None:#exchange the old mesh with the new one
            if  exchangewith in obj.name and tmp != None:
                obj.data = assetmesh
                myfun = obj
                #obj.location = tmp.location
    if exchangewith == "Eyes-Local":
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects["Eyes-Local"].select_set(True)
        print("LÖ CURSOR",bpy.context.scene.cursor.location)
        bpy.context.scene.cursor.location = Vector((-0.0033, -7.9903, 0.0480)) + Vector ((0.0000, 0.0000, 10.3609)) + Vector((0.0000, -23.2482, 27.2410))+ Vector((0.0000, 0.0000, 31.4330))
        print("LÖ EYES:",bpy.context.scene.cursor.location,"=",(Vector(myfun.location)[0]+Vector(myob.location)[0],Vector(myfun.location)[1]+Vector(myob.location)[1], Vector(myfun.location)[2]+Vector(myob.location)[2]))
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                override = bpy.context.copy()
                override['area'] = area
                override['region'] = area.regions[4]
                bpy.ops.view3d.snap_selected_to_cursor(override,use_offset=True)
        bpy.ops.object.select_all(action="DESELECT")
        #bpy.context.active_object.select_set(False)
        myob.select_set(True)
        objs = bpy.context.selected_objects[:]
        
    return

def head_and_eyes(tmp):
    assetname = tmp
    testpath = assetpath+data["Head"]+"\\"+data["Skin"]+"\\"+data["Head"]+"_"+data["Eyes"]+".gltf"
    if path.exists(testpath):
        print("HELL")
        bpy.ops.import_scene.gltf(filepath=assetpath+data["Head"]+"\\"+data["Skin"]+"\\"+data["Head"]+"_"+data["Eyes"]+".gltf", files=[{"name":data["Head"]+"_"+data["Eyes"]+".gltf", "name":data["Head"]+"_"+data["Eyes"]+".gltf"}], loglevel=50)
        #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+data["Skin"]+"\\"+data["Head"]+"_"+data["Eyes"]+".gltf", files=[{"name":data["Head"]+"_"+data["Eyes"]+".gltf", "name":data["Head"]+"_"+data["Eyes"]+".gltf"}], loglevel=50)
        exchangewith = "Skull-Local"
    else:
        exchangewith = "Skull-Local"
        assetname = data["Head"]
        print(data["Head"])
        bpy.ops.import_scene.gltf(filepath=assetpath+data["Head"]+"\\"+data["Skin"]+"\\"+data["Head"]+".gltf", files=[{"name":data["Head"]+".gltf", "name":data["Head"]+".gltf"}], loglevel=50)
        #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+data["Skin"]+"\\"+assetname+".gltf", files=[{"name":assetname+".gltf", "name":assetname+".gltf"}], loglevel=50)
    
    exchange_mesh(exchangewith)            
    bpy.ops.object.delete()
    #delete selected
    
    
    #eyes shaped for head
    testpath = assetpath+data["Eyes"]+"\\"+data["Eyes"]+"_"+data["Head"]+".gltf"
    if path.exists(testpath):
        bpy.ops.import_scene.gltf(filepath=assetpath+data["Eyes"]+"\\"+data["Eyes"]+"_"+data["Head"]+".gltf", files=[{"name":data["Eyes"]+"_"+data["Head"]+".gltf", "name":data["Eyes"]+"_"+data["Head"]+".gltf"}], loglevel=50)
        #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+data["Eyes"]+"_"+data["Head"]+".gltf", files=[{"name":data["Eyes"]+"_"+data["Head"]+".gltf", "name":data["Eyes"]+"_"+data["Head"]+".gltf"}], loglevel=50)
        exchangewith = "Eyes-Local"
    else:
        exchangewith = "Eyes-Local"
        assetname = data["Eyes"]
        bpy.ops.import_scene.gltf(filepath=assetpath+data["Eyes"]+"\\"+data["Eyes"]+".gltf", files=[{"name":data["Eyes"]+".gltf", "name":data["Eyes"]+".gltf"}], loglevel=50)
        #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+assetname+".gltf", files=[{"name":assetname+".gltf", "name":assetname+".gltf"}], loglevel=50)

    exchange_mesh(exchangewith)
    bpy.ops.object.delete()
    return

assetname=""
exchangewith=""
#reading json File
for i in range(50,70):
    print("I: ",i)
    if i == 666 or i > 990:
        continue 
    data = {}
    with open("Z:\\home\\flo\\projekt\\nft\\test\\"+str(i)+'.json', 'r') as infile:
                data = json.load(infile)
    #reloading model
    exists = 0
    bpy.ops.import_scene.gltf(filepath=skinpath+data["Skin"]+".gltf", files=[{"name":data["Skin"]+".gltf", "name":data["Skin"]+".gltf"}], loglevel=50)
    #head shaped for eyes
    if "Head" in data.keys() and "Eyes" in data.keys():
        head_and_eyes(assetname)
    elif "Head" in data.keys():
        exchangewith = "Skull-Local"
        assetname = data["Head"]
        bpy.ops.import_scene.gltf(filepath=assetpath+data["Head"]+"\\"+data["Skin"]+"\\"+data["Head"]+".gltf", files=[{"name":data["Head"]+".gltf", "name":data["Head"]+".gltf"}], loglevel=50)
        #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+data["Skin"]+"\\"+assetname+".gltf", files=[{"name":assetname+".gltf", "name":assetname+".gltf"}], loglevel=50)
        exchange_mesh(exchangewith)
        bpy.ops.object.delete()
    elif "Eyes" in data.keys():
        exchangewith = "Eyes-Local"
        assetname = data["Eyes"]
        bpy.ops.import_scene.gltf(filepath=assetpath+data["Eyes"]+"\\"+data["Eyes"]+".gltf", files=[{"name":data["Eyes"]+".gltf", "name":data["Eyes"]+".gltf"}], loglevel=50)
        #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+assetname+".gltf", files=[{"name":assetname+".gltf", "name":assetname+".gltf"}], loglevel=50)
        exchange_mesh(exchangewith)
        bpy.ops.object.delete()
    if "Eyes" not in data.keys():
        print("empty")
        exchangewith = "Eyes-Local"
        bpy.ops.import_scene.gltf(filepath=assetpath+"empty.gltf", files=[{"name":"empty.gltf", "name":"empty.gltf"}], loglevel=50)
        exchange_mesh(exchangewith)
        bpy.ops.object.delete()
    #delete selected
    
    
    
    for key in data.keys():
        # loading head of json
        if key == "Mouth":
            print("Mouth")
            continue
        if key == "Body":
            print("Body")
            exchangewith = "Body-Local"
            assetname = data["Body"]
            bpy.ops.import_scene.gltf(filepath=assetpath+data["Body"]+"\\"+data["Skin"]+"\\"+data["Body"]+".gltf", files=[{"name":data["Body"]+".gltf", "name":data["Body"]+".gltf"}], loglevel=50)
        if key == "Background":
            print("Background")
            continue
        if key == "Skin":
            continue
        if key == "Head":
            continue
        if key == "Eyes":
            continue
        
        exchange_mesh(exchangewith)
        bpy.ops.object.delete()
        #delete selected
    infile.close()

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.gltf(filepath="Z:\\home\\flo\\projekt\\new\\exchange_blender\\asset_gltfs\\out\\"+str(i)+".gltf",export_format='GLTF_EMBEDDED')
    bpy.ops.object.delete() # delete all of the meshes and nodes

    bpy.ops.outliner.orphans_purge()# purge orphans so name is always without XXX

    print("finished")

#https://blender.stackexchange.com/questions/24133/modify-obj-after-import-using-python"""