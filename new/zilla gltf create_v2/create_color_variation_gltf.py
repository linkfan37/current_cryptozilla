import json
from alive_progress import alive_bar


def creategltfs( gltf_in = 'thirstplace.gltf'):
    print('CREATE COLOR VARIATIONS')

    skins = ["light orange/light orange.json","pale green/pale green.json","blue/blue.json","fire/fire.json","independance blue/independance blue.json","light purple/light purple.json","grayscale/grayscale.json","pink/pink.json","dark cyan/dark cyan.json","red/red.json","persian green/persian green.json","orange/orange.json","pigeon blue/pigeon blue.json","dark pink/dark pink.json","kelly green/kelly green.json","violet/violet.json","dark purple/dark purple.json","cream/cream.json","crocodile/crocodile.json","hunter green/hunter green.json","og/og.json"]
    color = ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green","og"]

    #gltf_in = 'thirstplace.gltf'
    gltf_name = gltf_in.replace(".gltf","")
    
    gltf_in = gltf_in.replace("\\","/")
    red = readlines_create(gltf_in)

    #print(Bodyuri)
    #for skin in skins:
    print('└[skin replace]')
    i = 0
    with alive_bar(len(skins),force_tty=True) as bar:
        for skin in skins:
            f = open('E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/gltf in/'+gltf_in, 'r')
            f2 = open('E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/gltf out/'+color[i]+"_"+gltf_name+'.gltf', 'w')
            li = 0
            print(len(red))
            while True:
                line = f.readline()
                with open('E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/skins/'+skin) as json_file:
                    data = json.load(json_file)
    	        
                replacement=""

                if '"},' in line:
                    replacement = str(line.replace('{"uri": "','').replace('"},','').strip())
                else:
                    replacement = str(line.replace('{"uri": "','').replace('"}','').strip())
                
                if li == red[0]:
                    line = line.replace(replacement,data[color[i]+'_body_center'])
                if li == red[1]:
                    line = line.replace(replacement,data[color[i]+'_head_top'])
                if  li == red[2]:
                    line = line.replace(replacement,data[color[i]+'_mouth'])
                if li == red[3]:
                    line = line.replace(replacement,data[color[i]+'_left_arm_1'])
                if li == red[4]:
                    line = line.replace(replacement,data[color[i]+'_left_arm_2'])
                if li == red[5]:
                    line = line.replace(replacement,data[color[i]+'_left_arm_3'])
                if li == red[6]:
                    line = line.replace(replacement,data[color[i]+'_right_arm_1'])
                if li == red[7]:
                    line = line.replace(replacement,data[color[i]+'_right_arm_2'])
                if 0 != red[8]:
                    if li == red[8]: 
                        line = line.replace(replacement,data[color[i]+'_right_arm_3'])
                if li == red[9]:
                    line = line.replace(replacement,data[color[i]+'_right_leg_1'])
                if li == red[10]:
                    line = line.replace(replacement,data[color[i]+'_right_leg_2'])
                if li == red[11]:
                    line = line.replace(replacement,data[color[i]+'_right_leg_3'])
                if li == red[12]:
                    line = line.replace(replacement,data[color[i]+'_left_leg_1'])
                if li == red[13]:
                    line = line.replace(replacement,data[color[i]+'_left_leg_2'])
                if li == red[14]:
                    line = line.replace(replacement,data[color[i]+'_left_leg_3'])
                if li == red[15]:
                    line = line.replace(replacement,data[color[i]+'_tail_1'])
                if li == red[16]:
                    line = line.replace(replacement,data[color[i]+'_tail_2'])
                if li == red[17]:
                    line = line.replace(replacement,data[color[i]+'_tail_3'])
                if li == red[18]:
                    line = line.replace(replacement,data[color[i]+'_tail_4'])
                if li == red[19]:
                    line = line.replace(replacement,data[color[i]+'_shade_body'])
                if li == red[20]:
                    line = line.replace(replacement,data[color[i]+'_shade_head'])
                if li == red[21]:
                    line = line.replace(replacement,data[color[i]+'_shade_tail_1'])
                if li == red[22]:
                    line = line.replace(replacement,data[color[i]+'_shade_tail_2'])
                if li == red[23]:
                    line = line.replace(replacement,data[color[i]+'_shade_tail_3'])
                if li == red[24]:
                    line = line.replace(replacement,data[color[i]+'_shade_tail_4'])

                if not line:
                    break
                f2.write(line)
                li= li +1
            f.close()
            f2.close()
            bar()
            i = i + 1

"""def uri_read_create(gltf_in):
     #/////////////URI READ/////////////
    print('└[uri read]')

    uri_reader = open('E:/Zilla/current_cryptozilla/new/zilla gltf create_v2/gltf in/'+gltf_in, 'r')
    readlines=readlines_create(gltf_in)
    
    for line_num, line in enumerate(uri_reader.readlines()):
        #print(line_num)

        if '"},' in line:
            line = str(line.replace('{"uri": "','').replace('"},','').strip())
        else:
            line = str(line.replace('{"uri": "','').replace('"}','').strip())
        
        #print(line)
        
        if line_num == readlines[0] : Bodyuri=line
        if line_num == readlines[1] : head_top_uri=line
        if line_num == readlines[2] : mouthuri=line
        if line_num == readlines[3] : left_arm_1=line
        if line_num == readlines[4] : left_arm_2=line
        if line_num == readlines[5] : left_arm_3=line
        if line_num == readlines[6] : right_arm_1=line
        if line_num == readlines[7] : right_arm_2=line
        if readlines[8]!=0:
            if line_num == readlines[8] : right_arm_3=line
        else:
            right_arm_3=""
        if line_num == readlines[9] : left_leg_1=line
        if line_num == readlines[10] : left_leg_2=line
        if line_num == readlines[11] : left_leg_3=line
        if line_num == readlines[12] : right_leg_1=line
        if line_num == readlines[13] : right_leg_2=line
        if line_num == readlines[14] : right_leg_3=line
        if line_num == readlines[15] : tail_1=line
        if line_num == readlines[16] : tail_2=line
        if line_num == readlines[17] : tail_3=line
        if line_num == readlines[18] : tail_4=line
        if line_num == readlines[19] : shade_body=line
        if line_num == readlines[20] : shade_head=line
        if line_num == readlines[21] : shade_tail_1=line
        if line_num == readlines[22] : shade_tail_2=line
        if line_num == readlines[23] : shade_tail_3=line
        if line_num == readlines[24] : shade_tail_4=line

        if line_num>50:
            break

    uri_reader.close()"""
    
def readlines_create(gltf_in):
    if "tentacle" in gltf_in or "canon" in gltf_in:
        if gltf_in.count("_")==1:
            return [36,2,4,10,12,14,6,8,0,22,24,26,16,18,20,28,30,32,34,37,3,29,31,33,35]
        elif gltf_in.count("_")==2 :
            return [38,2,4,12,14,16,8,10,0,24,26,28,18,20,22,30,32,34,36,39,3,31,33,35,37]
        elif gltf_in.count("_")==3 :
            return [40,2,4,12,14,16,10,12,0,26,28,30,20,22,24,32,34,36,38,41,3,33,35,37,39]
        return []
    else:
        if gltf_in.count("_")==1:
            return [38,2,4,12,14,16,6,8,10,24,26,28,18,20,22,30,32,34,36,39,3,31,33,35,37]
        elif gltf_in.count("_")==2 :
            return [40,2,4,14,16,18,8,10,12,26,28,30,20,22,24,32,34,36,38,41,3,33,35,37,39]
        elif gltf_in.count("_")==3 :
            return [42,2,4,16,18,20,10,12,14,28,30,32,22,24,26,34,36,38,40,43,3,35,37,39,41]
        return []

    
    
    