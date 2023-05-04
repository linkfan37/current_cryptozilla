import glob, os

def geturis(assetlist): 
    #/////////////URI READ/////////////
    print('└[uri read]')
    uris = {}
    for asset in assetlist:
        uri_reader = open('/home/flo/projekt/new/mini/zilla gltf create/gltf in/'+asset, 'r')
        

        for line_num, line in enumerate(uri_reader.readlines()):
            #print(line_num)

            if '"},' in line:
                line = str(line.replace('{"uri": "','').replace('"},','').strip())
            else:
                line = str(line.replace('{"uri": "','').replace('"}','').strip())
            
            #print(line)
            asset = asset.replace(".gltf","")
            
            if line_num == 2 : uris[asset]=line
            if line_num == 3 : uris[asset+" shade"]=line
            if line_num>40:
                break
        uri_reader.close()
    return uris


def getfiles (path,filter):
    gltfs= []

    os.chdir(path)
    for file in glob.glob(filter):
        gltfs.append(file)
    return gltfs