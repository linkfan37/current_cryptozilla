import urllib.request
import get_uri_dict 
def fetch(gltf_in):
    print("Begining downloading of the textures")
    path = "E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/stantard_skins2/"
    uris = get_uri_dict.geturis(gltf_in)
    #print(uris)
    print('Beginning file download with urllib2...')
    for key in uris.keys():
        urllib.request.urlretrieve(uris[key], path+key+".png")
    return 1
#fetch()