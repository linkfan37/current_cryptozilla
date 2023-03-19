import bpy
import json


assetname=""
exchangewith=""

#reading json File
for i in range(1,1000):
    data = {}
    with open('Z:\\home\\flo\\projekt\\nft\\test\\'+str(i)+'.json', 'r') as infile:
                data = json.load(infile)
    
    #reloading model
    bpy.ops.import_scene.gltf(filepath="Z:\\home\\flo\\projekt\\new\\exchange_blender\\zilla10k.gltf", files=[{"name":"zilla10k.gltf", "name":"zilla10k.gltf"}], loglevel=50)
    
    if "Head in Keys"
    for key in data.keys():
        # loading head of json
        if key == "Head":
            exchangewith = "Zilla_head-Mesh"
            assetname = data["Head"]
            bpy.ops.import_scene.gltf(filepath="Z:\\home\\flo\\projekt\\new\\exchange_blender\\asset_gltfs\\Head\\"+assetname+".gltf", files=[{"name":assetname+".gltf", "name":assetname+".gltf"}], loglevel=50)
        if key == "Mouth":
            print("Mouth")
            continue
        if key == "Body":
            print("Body")
            continue
        if key == "Eyes":
            print("Eyes")
            continue
        if key == "Background":
            print("Background")
            continue
        if key == "Skin":
            print("Skin")
            continue
        
        objs = bpy.context.selected_objects[:]#selected objects
        myob = objs[0]
        assetmesh = objs[0].data
        for o in objs:
            assetmesh = o.data


        scene = bpy.context.scene
        tmp = scene.objects[0]

                
        for obj in scene.objects:
            mesh = obj.data
            #print(mesh)
            if mesh != None:#exchange the old mesh with the new one
                if  exchangewith in mesh.name and tmp != None:
                    obj.data = assetmesh
                    #obj.location = tmp.location
                    
        bpy.ops.object.delete()
        #delete selected
        infile.close()

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.gltf(filepath="Z:\\home\\flo\\projekt\\new\\exchange_blender\\asset_gltfs\\"+str(i)+".gltf",export_format='GLTF_EMBEDDED')
    bpy.ops.object.delete() # delete all of the meshes and nodes

    bpy.ops.outliner.orphans_purge()# purge orphans so name is always without XXX

    print("finished")

#https://blender.stackexchange.com/questions/24133/modify-obj-after-import-using-python"""