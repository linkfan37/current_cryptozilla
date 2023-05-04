import get_textures
import change_color
import exchangeimage
import create_color_variation_gltf

print('GLTF CREATION START')
paths=exchangeimage.listcolor("/home/flo/projekt/new/zilla gltf create_v2/gltf in/")
for p in paths:
    bodies=exchangeimage.listcolor(p)
    for b in bodies:
        #print(b+"/standart.gltf")
        ret = get_textures.fetch(b+"/standart.gltf")
        gltfdtocreate = exchangeimage.listcolor(b)
        for g in gltfdtocreate:#
            g = g.replace("/home/flo/projekt/new/zilla gltf create_v2/gltf in/","")
            print(g+"\n")
            change_color.change_col()
            exchangeimage.exchange()
            create_color_variation_gltf.creategltfs(g)