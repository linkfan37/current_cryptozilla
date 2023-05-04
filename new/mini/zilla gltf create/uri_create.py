from pygltflib import GLTF2
from pygltflib.utils import ImageFormat, Image
import os
import json

def createUri(dirName):

    gltf = GLTF2()
    image = Image()
    image.uri = dirName
    gltf.images.append(image)
    gltf.convert_images(ImageFormat.DATAURI)
    gltf.images[0].uri  # will now be something like "data:image/png;base64,iVBORw0KGg..."
    gltf.images[0].name  # will be myfile.png
    #print(gltf.images[0].uri)
    #print(fullPath," = ")
    #print(fullPath," = ",partlist[i])
    uri=gltf.images[0].uri
        
          
    return uri
