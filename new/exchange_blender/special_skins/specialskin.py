# -*- coding: utf-8 -*-
from PIL import Image as Image1
from pygltflib import GLTF2
from pygltflib.utils import ImageFormat, Image
import os
import json


assetname1= "Body.png"
assetname2= "angle halo shade.png"
assetnames = [assetname1]
asset = assetname1.replace('.png','')
for assetname in assetnames:
    image = Image1.open('/home/flo/projekt/new/exchange_blender/special_skins/' + assetname)
    colormask = Image1.open('/home/flo/projekt/new/exchange_blender/special_skins/' + "body_try.png")
    #print(image)
    #print(image.mode)
    rgba=image.convert("RGBA")
    datas = rgba.getdata()
    rgba2 = colormask.convert("RGBA")
    datas2 = rgba2.getdata()
    zip_ob = (datas,datas2)
    new_color = []
    #print(zip_ob)
    for original, maskc in zip(*zip_ob):
        print(original)
        print(maskc)
        if(original[0] == 86 and original[1]==82 and original[2]==159 and original[3]==255): #normal skin //piink normal
            new_color.append(maskc)
        elif(original[0] == 79 and original[1]==72 and original[2]==148 and original[3]==255):#darker skin //normal-20
            new_color.append(maskc)
        elif(original[0] == 69 and original[1]==201 and original[2]==186 and original[3]==255):#belly
            new_color.append(maskc)
        elif(original[0] == 67 and original[1]==94 and original[2]==187 and original[3]==255):#berfore belly
            new_color.append(maskc)
        elif(original[0] == 234 and original[1]==219 and original[2]==206 and original[3]==255):#theeth
            new_color.append(original)
        
        elif(original[0] == 0 and original[1]==0 and original[2]==0 and original[3]==0):#transparent
            new_color.append(original)
        elif(original[0] == 222 and original[1]==87 and original[2]==230 and original[3]==255):#topspikes
            new_color.append(maskc)
        elif(original[0] == 77 and original[1]==32 and original[2]==104 and original[3]==255):#bottomspikes
            new_color.append(maskc)
        elif(original[0] == 90 and original[1]==47 and original[2]==123 and original[3]==255):#also bottomspikes? lol
            new_color.append(maskc)
        elif(original[0] == 36 and original[1]==30 and original[2]==23 and original[3]==255):# nearly black
            new_color.append(original)
        elif(original[0] == 105 and original[1]==22 and original[2]==22 and original[3]==255):# mouth intern
            new_color.append(original)
        else:
            new_color.append(original)
            print(original)
            

    rgba.putdata(new_color)
    rgba.save("/home/flo/projekt/new/exchange_blender/special_skins/test/"+ assetname, "PNG")