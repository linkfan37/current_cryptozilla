import bpy
import json
import os
from os import path
from mathutils import *
from math import *

assetpath = "Z:\\home\\flo\\projekt\\new\\exchange_blender_copy\\asset_gltfs\\heads_new\\"
skinpath = "Z:\\home\\flo\\projekt\\new\\exchange_blender_copy\\asset_gltfs\\"

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

assetname=""
exchangewith=""
#reading json File
for i in range(1001,1040):
    print("I: ",i)
    #if i == 666 or i > 990:
     #   continue 
    data = {}
    with open("Z:\\home\\flo\\projekt\\new\\exchange_blender_copy\\meta\\"+str(i)+'.json', 'r') as infile:
                data = json.load(infile)
    #reloading model
    exists = 0
    print("DATA",data)
    bpy.ops.import_scene.gltf(filepath=skinpath+"standart"+".gltf", files=[{"name":"standart"+".gltf", "name":"standart"+".gltf"}], loglevel=50)
    
    
    
    for key in data.keys():
        # loading head of json
        #if key == "Mouth":
        #    print("Mouth")
        #    continue
        #if key == "Body":
        #    print("Body")
        #    exchangewith = "Body-Local"
        #    assetname = data["Body"]
        #    bpy.ops.import_scene.gltf(filepath=assetpath+data["Body"]+"\\"+data["Skin"]+"\\"+data["Body"]+".gltf", files=[{"name":data["Body"]+".gltf", "name":data["Body"]+".gltf"}], loglevel=50)
        #if key == "Background":
        #    print("Background")
        #    continue
        #if key == "Skin":
        #    continue
        if key == "Head":
            if data["Head"] != "" and data["Head"] != "skull":
                print("Head:",data["Head"])
                exchangewith = "Skull-Local"
                assetname = data["Head"]
                bpy.ops.import_scene.gltf(filepath=assetpath+data["Head"]+".gltf", files=[{"name":data["Head"]+".gltf", "name":data["Head"]+".gltf"}], loglevel=50)
                #bpy.ops.import_scene.gltf(filepath=assetpath+assetname+"\\"+data["Skin"]+"\\"+assetname+".gltf", files=[{"name":assetname+".gltf", "name":assetname+".gltf"}], loglevel=50)
                #exchange_mesh(exchangewith)
                #bpy.ops.object.delete()
                exchange_mesh(exchangewith)
                bpy.ops.object.delete()
            #quit()
        #if key == "Eyes":
            #    continue
       
        #delete selected
    infile.close()

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.gltf(filepath="Z:\\home\\flo\\projekt\\new\\exchange_blender_copy\\asset_gltfs\\out\\"+str(i)+".gltf",export_format='GLTF_EMBEDDED')
    bpy.ops.object.delete() # delete all of the meshes and nodes

    bpy.ops.outliner.orphans_purge()# purge orphans so name is always without XXX

    print("finished")

#https://blender.stackexchange.com/questions/24133/modify-obj-after-import-using-python"""