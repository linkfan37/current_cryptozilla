import os
mypath = "/home/flo/projekt/new/zilla gltf create_v2/gltf out/"
color = ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green","og"]
options = ["Skin_Body_Ananas","Skin_Body"]
bodies= ['zombie (1)','zombie (2)','zombie (3)','canon hand','tentacle hand',
    'cyborg (1)','cyborg (2)','cyborg (3)',
    'stegosaurus (tail)','stegosaurus (body)','stegosaurus (full)',
    'pants',
    'hawaii flower necklace',
    'beads necklace',
    'mermaid bra',
    'blue dragon tattoo','red dragon tattoo','standart'
]
for col in color:
    for o in options:
        os.mkdir(mypath+col+"_"+o)
        for b in bodies:
            os.mkdir(mypath+col+"_"+o+"/"+b)
    