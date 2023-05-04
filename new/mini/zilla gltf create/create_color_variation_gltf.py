import json
from alive_progress import alive_bar
import get_uri_dict
import uri_create
def create():
    print('CREATE COLOR VARIATIONS')
    assets = get_uri_dict.getfiles("/home/flo/projekt/new/mini/zilla gltf create/gltf in/","*.gltf")
    #og missing
    color = ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green"]

    #/////////////URI READ/////////////
    print('└[uri read]')
    for asset in assets:
        uri_reader = open('/home/flo/projekt/new/mini/zilla gltf create/gltf in/'+asset, 'r')

        for line_num, line in enumerate(uri_reader.readlines()):
            #print(line_num)

            if '"},' in line:
                line = str(line.replace('{"uri": "','').replace('"},','').strip())
            else:
                line = str(line.replace('{"uri": "','').replace('"}','').strip())
            
            #print(line)
            
            if line_num == 2 : normal=line
            if line_num == 3 : shade=line

            if line_num>6:
                break

        uri_reader.close()

        #for skin in skins:
        print('└[skin replace]')
        
        name = ""
        name = asset.replace(".gltf","")
        for col in color:
        
            f = open('/home/flo/projekt/new//mini/zilla gltf create/gltf in/'+asset, 'r')
            f2= ""
            if "_" not in name:
                f2 = open('/home/flo/projekt/new/mini/zilla gltf create/gltf out/'+col+"_"+name+'.gltf', 'w')
            else:
                f2 = open('/home/flo/projekt/new/mini/zilla gltf create/gltf out/'+col+"_"+name+'.gltf', 'w')
            while True:
                line = f.readline()
                if normal in line:
                    line = line.replace(normal,uri_create.createUri("/home/flo/projekt/new/mini/zilla gltf create/skins/"+col+"/"+col+"_"+asset.replace(".gltf",".png")))
                if shade in line:
                    line = line.replace(shade,uri_create.createUri("/home/flo/projekt/new/mini/zilla gltf create/skins/"+col+"/"+col+"_"+asset.replace(".gltf"," shade.png")))

                if not line:
                    break
                f2.write(line)
            f.close()
            f2.close()
