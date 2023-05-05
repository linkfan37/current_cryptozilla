from pygltflib import GLTF2
from pygltflib.utils import ImageFormat, Image
import os
import json

def listcolor(dirName):
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    #list of names
    listofcolor = []
    # Iterate over all the entries
    for entry in listOfFile:
        #create full path
        fullPath = os.path.join(dirName, entry)
        listofcolor.append(fullPath)
          
    return listofcolor

def checkpart(part):
    # names in the given directory 
    tmp = part.split('.')
    return tmp[0]

def createUri(dirName):
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    #list of names
    dictUris = {}
    #partlist = ["right_arm_3","left_leg_3","right_leg_2","left_leg_1","tail_4","head_top","right_arm_2","tail_3","right_arm_1","Body_Center","mouth","right_leg_1","left_arm_3","left_arm_1","tail_1","left_leg_2","left_arm_2","tail_2","right_leg_3"]
    # Iterate over all the entries
    i = 0
    for entry in listOfFile:
        #create full path
        if not '.json' in entry:
            fullPath = os.path.join(dirName, entry)
            part = checkpart(entry)
            gltf = GLTF2()
            image = Image()
            image.uri = fullPath
            gltf.images.append(image)
            gltf.convert_images(ImageFormat.DATAURI)
            gltf.images[0].uri  # will now be something like "data:image/png;base64,iVBORw0KGg..."
            gltf.images[0].name  # will be myfile.png
            #print(gltf.images[0].uri)
            #print(fullPath," = ")
            #print(fullPath," = ",partlist[i])
            dictUris[part]=gltf.images[0].uri
            i=i+1
        
          
    return dictUris

"""
gltf = GLTF2()
image = Image()
image.uri = "E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/Cream_image2.png"
gltf.images.append(image)
gltf.convert_images(ImageFormat.DATAURI)
gltf.images[0].uri  # will now be something like "data:image/png;base64,iVBORw0KGg..."
gltf.images[0].name  # will be myfile.png
print(gltf.images[0].uri)
"""
def exchange():
    print('SKIN COLOR EXCHANGE')
    #partlist = []
    #colorlist = ["Cream","Crocodile","Dark_Cyan","Dark_Pink","Dark_Purple","Fire","Grayscale","Huntergreen","Independance","KellyGreen","Lightorange","Lightpurple","Orange","Palegreen","Persian","Pidgeonblue","Pink","Red","Violet"]
    colordirlist = listcolor("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/")
    #print(colordirlist)
    i = 0

    colorlist= ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green","og"]

    for color in colordirlist:
        if '.py' not in color:
            uridir = createUri(color)
            color2 = color.replace("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/","")
            jsonpath = os.path.join(color, color2+".json")
            with open(jsonpath, 'w') as outfile:
                json.dump(uridir,outfile,indent=2)
            #print(color)
            i=i+1


    """
    testpath = os.path.join(dirName, "test.json")
        with open(testpath, 'w') as outfile:
            json.dump(l,outfile,indent=2)
    """