from pygltflib import GLTF2
from pygltflib.utils import ImageFormat, Image
import os
import json

fullPath = os.path.join("/home/flo/projekt/new/exchange_blender/special_skins/test/Body_Center.png")
gltf = GLTF2()
image = Image()
image.uri = fullPath
gltf.images.append(image)
gltf.convert_images(ImageFormat.DATAURI)
gltf.images[0].uri  # will now be something like "data:image/png;base64,iVBORw0KGg..."
gltf.images[0].name  # will be myfile.png
print(gltf.images[0].uri)