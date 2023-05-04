from pygltflib import GLTF2

# convert gltf to glb
gltf = GLTF2().load("/home/flo/projekt/new/test2.gltf")
gltf.save("/home/flo/projekt/new/test.glb")