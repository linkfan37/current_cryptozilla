import get_textures
import change_color
import exchangeimage
import create_color_variation_gltf

print('GLTF CREATION START')
gltfdtocreate = exchangeimage.listcolor("/home/flo/projekt/new/zilla gltf create/gltf in/")
for g in gltfdtocreate:
    g = g.replace("/home/flo/projekt/new/zilla gltf create/gltf in/","")
    print(g+"\n")
    ret = get_textures.fetch(g)
    change_color.change_col()
    exchangeimage.exchange()
    create_color_variation_gltf.creategltfs(g)