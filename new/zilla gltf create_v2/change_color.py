# -*- coding: utf-8 -*-
from tracemalloc import start
from PIL import Image
import gc
def change_col():
    print('SKIN COLOR CHANGE')

    List=["body_center.png","head_top.png","left_arm_1.png","left_arm_2.png","left_arm_3.png","left_leg_1.png","left_leg_2.png","left_leg_3.png","mouth.png","right_arm_1.png","right_arm_2.png","right_arm_3.png","right_leg_1.png","right_leg_2.png","right_leg_3.png","tail_1.png","tail_2.png","tail_3.png","tail_4.png","shade_body.png","shade_head.png","shade_tail_1.png","shade_tail_2.png","shade_tail_3.png","shade_tail_4.png"]

    for part in List:
        print('\r└[read given img data] of '+ part, end='')
        image = Image.open('E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/stantard_skins2/' + part)
        #print(image)
        #print(image.mode)
        rgba=image.convert("RGBA")
        datas = rgba.getdata()
        
        og = []
        DarkPink = []
        Pink = []
        Cream = []
        Crocodile = []
        DarkCyan = []
        DarkPurple = []
        Fire=[]
        Grayscale=[]
        HunterGreen =[]
        Independance_blue = []
        Kelly_green = []
        Light_orange = []
        Light_purple=[]
        Orange = []
        Pale_Green = []
        Persian = []
        Pidgeon_Blue = []
        Red = []
        Violet = []
        Blue = []
        #print(datas)
        for item in datas:
            if(item[0] == 86 and item[1]==82 and item[2]==159 and item[3]==255): #normal skin //piink normal
                DarkPink.append((255, 85, 170, 255))
                Pink.append((255,127,170,255))
                Cream.append((224,177,175,255))
                Crocodile.append((87,86,59,255))
                DarkCyan.append((0,85,85,255))
                DarkPurple.append((85,85,170,255))
                Fire.append((170,85,85,255))
                Grayscale.append((105,105,105,255))
                HunterGreen.append((85,170,85,255))
                Independance_blue.append((101,85,116,255))
                Kelly_green.append((0,170,0,255))
                Light_orange.append((255,170,0,255))
                Light_purple.append((170,85,255,255))
                Orange.append((255,149,0,255))
                Pale_Green.append((85,255,170,255))
                Persian.append((0,170,170,255))
                Pidgeon_Blue.append((85,93,116,255))
                Red.append((170,0,0,255))
                Violet.append((85,85,170,255))
                Blue.append((85,85,255,255))
                og.append((85,95,120,255))
            elif(item[0] == 79 and item[1]==72 and item[2]==148 and item[3]==255):#darker skin //normal-20
                DarkPink.append((235, 65, 150, 255))
                Pink.append((235,107,150,255))
                Cream.append((204,157,155,255))
                Crocodile.append((67,66,39,255))
                DarkCyan.append((0,65,65,255))
                DarkPurple.append((65,65,150,255))
                Fire.append((150,65,65,255))
                Grayscale.append((85,85,85,255))
                HunterGreen.append((65,150,65,255))
                Independance_blue.append((81,65,96,255))
                Kelly_green.append((0,150,0,255))
                Light_orange.append((235,150,0,255))
                Light_purple.append((150,65,235,255))
                Orange.append((235,129,0,255))
                Pale_Green.append((65,235,150,255))
                Persian.append((0,150,150,255))
                Pidgeon_Blue.append((65,73,96,255))
                Red.append((150,0,0,255))
                Violet.append((65,65,150,255))
                Blue.append((75,75,245,255))
                og.append((75,85,110,255))
            elif(item[0] == 69 and item[1]==201 and item[2]==186 and item[3]==255):#belly
                DarkPink.append((255, 218, 236, 255))
                Pink.append((255,255,255,255))
                Cream.append((255,255,255,255))
                Crocodile.append((255,170,221,255))
                DarkCyan.append((170,255,170,255))
                DarkPurple.append((255,255,170,255))
                Fire.append((255,255,85,255))
                Grayscale.append((255,255,255,255))
                HunterGreen.append((255,255,255,255))
                Independance_blue.append((170,255,255,255))
                Kelly_green.append((255,255,170,255))
                Light_orange.append((255,255,170,255))
                Light_purple.append((255,255,170,255))
                Orange.append((255,255,170,255))
                Pale_Green.append((255,255,255,255))
                Persian.append((255,255,170,255))
                Pidgeon_Blue.append((255,255,170,255))
                Red.append((255,170,85,255))
                Violet.append((170,255,255,255))
                Blue.append((186,255,210,255))
                og.append((255,255,255,255))
            elif(item[0] == 67 and item[1]==94 and item[2]==187 and item[3]==255):#berfore belly
                DarkPink.append((255, 170, 170, 255))
                Pink.append((255,212,170,255))
                Cream.append((255,242,219,255))
                Crocodile.append((224,164,159,255))
                DarkCyan.append((0,176,147,255))
                DarkPurple.append((255,170,255,255))
                Fire.append((255,217,0,255))
                Grayscale.append((222,222,222,255))
                HunterGreen.append((255,255,170,255))
                Independance_blue.append((159,180,224,255))
                Kelly_green.append((187,239,0,255))
                Light_orange.append((255,255,0,255))
                Light_purple.append((224,194,255,255))
                Orange.append((255,227,118,255))
                Pale_Green.append((255,255,187,255))
                Persian.append((85,255,170,255))
                Pidgeon_Blue.append((159,224,218,255))
                Red.append((255,110,110,255))
                Violet.append((85,164,170,255))
                Blue.append((138,212,255,255))
                og.append((159,177,224,255))
            elif(item[0] == 234 and item[1]==219 and item[2]==206 and item[3]==255):#theeth
                DarkPink.append(item)
                Pink.append(item)
                Cream.append(item)
                Crocodile.append(item)
                DarkCyan.append(item)
                DarkPurple.append(item)
                Fire.append(item)
                Grayscale.append((item))
                HunterGreen.append(item)
                Independance_blue.append(item)
                Kelly_green.append(item)
                Light_orange.append(item)
                Light_purple.append(item)
                Orange.append(item)
                Pale_Green.append(item)
                Persian.append(item)
                Pidgeon_Blue.append(item)
                Red.append(item)
                Violet.append(item)
                Blue.append(item)
                og.append(item)
            elif(item[0] == 0 and item[1]==0 and item[2]==0 and item[3]==0):#transparent
                DarkPink.append(item)
                Pink.append(item)
                Cream.append(item)
                Crocodile.append(item)
                DarkCyan.append(item)
                DarkPurple.append(item)
                Fire.append(item)
                Grayscale.append(item)
                HunterGreen.append(item)
                Independance_blue.append(item)
                Kelly_green.append(item)
                Light_orange.append(item)
                Light_purple.append(item)
                Orange.append(item)
                Pale_Green.append(item)
                Persian.append(item)
                Pidgeon_Blue.append(item)
                Red.append(item)
                Violet.append(item)
                Blue.append(item)
                og.append(item)
            elif(item[0] == 222 and item[1]==87 and item[2]==230 and item[3]==255):#topspikes
                DarkPink.append((0, 170, 85, 255))
                Pink.append((152,106,170,255))
                Cream.append((255,175,85,255))
                Crocodile.append((170,91,85,255))
                DarkCyan.append((255,170,0,255))
                DarkPurple.append((88,43,185,255))
                Fire.append((85,85,170,255))
                Grayscale.append((99,99,99,255))
                HunterGreen.append((0,115,85,255))
                Independance_blue.append((85,113,170,255))
                Kelly_green.append((0,85,85,255))
                Light_orange.append((255,170,0,255))
                Light_purple.append((0,142,85,255))
                Orange.append((0,170,255,255))
                Pale_Green.append((255,168,151,255))
                Persian.append((170,85,85,255))
                Red.append((255,135,0,255))
                Pidgeon_Blue.append((120,240,228,255))
                Violet.append((170,0,170,255))
                Blue.append((168,64,113,255))
                og.append((58,109,170,255))
            elif(item[0] == 77 and item[1]==32 and item[2]==104 and item[3]==255):#bottomspikes
                DarkPink.append((0, 102, 85, 255))
                Pink.append((86,84,170,255))
                Cream.append((255,85,85,255))
                Crocodile.append((87,86,59,255))
                DarkCyan.append((255,85,0,255))
                DarkPurple.append((85,0,85,255))
                Fire.append((85,0,170,255))
                Grayscale.append((64,64,64,255))
                HunterGreen.append((0,85,85,255))
                Independance_blue.append((66,88,132,255))
                Kelly_green.append((0,106,0,255))
                Light_orange.append((170,85,0,255))
                Light_purple.append((0,85,85,255))
                Orange.append((0,85,255,255))
                Pale_Green.append((255,85,170,255))
                Persian.append((85,85,85,255))
                Pidgeon_Blue.append((66,132,125,255))
                Red.append((255,85,0,255))
                Violet.append((85,0,170,255))
                Blue.append((112,42,84,255))
                og.append((66,85,132,255))
            elif(item[0] == 90 and item[1]==47 and item[2]==123 and item[3]==255):#also bottomspikes? lol
                DarkPink.append((0, 102, 85, 255))
                Pink.append((86,84,170,255))
                Cream.append((255,85,85,255))
                Crocodile.append((132,70,66,255))
                DarkCyan.append((255,85,0,255))
                DarkPurple.append((85,0,85,255))
                Fire.append((85,0,170,255))
                Grayscale.append((64,64,64,255))
                HunterGreen.append((0,85,85,255))
                Independance_blue.append((66,88,132,255))
                Kelly_green.append((0,106,0,255))
                Light_orange.append((170,85,0,255))
                Light_purple.append((0,85,85,255))
                Orange.append((0,85,255,255))
                Pale_Green.append((255,85,170,255))
                Persian.append((85,85,85,255))
                Pidgeon_Blue.append((66,132,125,255))
                Red.append((255,85,0,255))
                Violet.append((85,0,170,255))
                Blue.append((112,42,84,255))
                og.append((66,85,132,255))
            elif(item[0] == 36 and item[1]==30 and item[2]==23 and item[3]==255):# nearly black
                DarkPink.append(item)
                Pink.append(item)
                Cream.append(item)
                Crocodile.append(item)
                DarkCyan.append(item)
                DarkPurple.append(item)
                Fire.append(item)
                Grayscale.append(item)
                HunterGreen.append(item)
                Independance_blue.append(item)
                Kelly_green.append(item)
                Light_orange.append(item)
                Light_purple.append(item)
                Orange.append(item)
                Pale_Green.append(item)
                Persian.append(item)
                Pidgeon_Blue.append(item)
                Red.append(item)
                Violet.append(item)
                Blue.append(item)
                og.append(item)
            elif(item[0] == 105 and item[1]==22 and item[2]==22 and item[3]==255):# mouth intern
                DarkPink.append(item)
                Pink.append(item)
                Cream.append(item)
                Crocodile.append(item)
                DarkCyan.append(item)
                DarkPurple.append(item)
                Fire.append(item)
                Grayscale.append(item)
                HunterGreen.append(item)
                Independance_blue.append(item)
                Kelly_green.append(item)
                Light_orange.append(item)
                Light_purple.append(item)
                Orange.append(item)
                Pale_Green.append(item)
                Persian.append(item)
                Pidgeon_Blue.append(item)
                Red.append(item)
                Violet.append(item)
                Blue.append(item)
                og.append(item)
            else:
                DarkPink.append(item)
                Pink.append(item)
                Cream.append(item)
                Crocodile.append(item)
                DarkCyan.append(item)
                DarkPurple.append(item)
                Fire.append(item)
                Grayscale.append(item)
                HunterGreen.append(item)
                Independance_blue.append(item)
                Kelly_green.append(item)
                Light_orange.append(item)
                Light_purple.append(item)
                Orange.append(item)
                Pale_Green.append(item)
                Persian.append(item)
                Pidgeon_Blue.append(item)
                Red.append(item)
                Violet.append(item)
                Blue.append(item)
                og.append(item)
                #print(item)

        rgba.putdata(DarkPink)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/dark pink/dark pink_"+ part, "PNG")
        rgba.putdata(Pink)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/pink/pink_"+part, "PNG")
        rgba.putdata(Cream)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/cream/cream_"+part, "PNG")
        rgba.putdata(Crocodile)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/crocodile/crocodile_"+part, "PNG")
        rgba.putdata(DarkCyan)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/dark cyan/dark cyan_"+part, "PNG")
        rgba.putdata(DarkPurple)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/dark purple/dark purple_"+part, "PNG")
        rgba.putdata(Fire)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/fire/fire_"+part, "PNG")
        rgba.putdata(Grayscale)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/grayscale/grayscale_"+part, "PNG")
        rgba.putdata(HunterGreen)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/hunter green/hunter green_"+part, "PNG")
        rgba.putdata(Independance_blue)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/independance blue/independance blue_"+part, "PNG")
        rgba.putdata(Kelly_green)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/kelly green/kelly green_"+part, "PNG")
        rgba.putdata(Light_orange)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/light orange/light orange_"+part, "PNG")
        rgba.putdata(Light_purple)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/light purple/light purple_"+part, "PNG")
        rgba.putdata(Orange)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/orange/orange_"+part, "PNG")
        rgba.putdata(Pale_Green)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/pale green/pale green_"+part, "PNG")
        rgba.putdata(Persian)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/persian green/persian green_"+part, "PNG")
        rgba.putdata(Pidgeon_Blue)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/pigeon blue/pigeon blue_"+part, "PNG")
        rgba.putdata(Red)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/red/red_"+part, "PNG")
        rgba.putdata(Violet)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/violet/violet_"+part, "PNG")
        rgba.putdata(Blue)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/blue/blue_"+part, "PNG")
        rgba.putdata(og)
        rgba.save("E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/og/og_"+part, "PNG")
    del  og 
    del    DarkPink 
    del    Pink 
    del    Cream 
    del    Crocodile
    del    DarkCyan 
    del    DarkPurple 
    del    Fire
    del    Grayscale
    del    HunterGreen 
    del    Independance_blue 
    del    Kelly_green 
    del    Light_orange 
    del    Light_purple
    del    Orange 
    del    Pale_Green 
    del    Persian 
    del    Pidgeon_Blue 
    del    Red 
    del    Violet 
    del    Blue 
    gc.collect()
    print('\r└[read given img data] of '+ part)