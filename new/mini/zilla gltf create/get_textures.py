import urllib.request
import get_uri_dict
def get_textures():
    print("Begining downloading of the textures")

    path = "/home/flo/projekt/new/mini/zilla gltf create/stantard_skins2/"
    assets =get_uri_dict.getfiles("/home/flo/projekt/new/mini/zilla gltf create/gltf in/","*.gltf")

    uris = get_uri_dict.geturis(assets)
    print('Beginning file download with urllib2...')
    for key in uris.keys():
        urllib.request.urlretrieve(uris[key], path+key+".png")