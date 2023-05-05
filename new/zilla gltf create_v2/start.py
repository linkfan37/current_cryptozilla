import get_textures
import change_color
import exchangeimage
import create_color_variation_gltf
import time

print('GLTF CREATION START')
paths=exchangeimage.listcolor("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/gltf in/")
for p in paths:
    bodies=exchangeimage.listcolor(p)
    for b in bodies:
        #print(b+"/standart.gltf")
        ret = get_textures.fetch(b+"/standart.gltf")
        gltfdtocreate = exchangeimage.listcolor(b)
        change_color.change_col()
        exchangeimage.exchange()
        for g in gltfdtocreate:#
            g = g.replace("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/gltf in/","")
            print(g+"\n")
           #time.sleep(5)
            create_color_variation_gltf.creategltfs(g)