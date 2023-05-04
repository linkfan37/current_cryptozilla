import json
from alive_progress import alive_bar

Bodyuri=""
head_top_uri=""
mouthuri=""
left_arm_1=""
left_arm_2=""
left_arm_3=""
right_arm_1=""
right_arm_2=""
right_arm_3=""
left_leg_1=""
left_leg_2=""
left_leg_3=""
right_leg_1=""
right_leg_2=""
right_leg_3=""
tail_1=""
tail_2=""
tail_3=""
tail_4=""
shade_body=""
shade_head=""
shade_tail_1=""
shade_tail_2=""
shade_tail_3=""
shade_tail_4=""

def creategltfs( gltf_in = 'thirstplace.gltf'):
    print('CREATE COLOR VARIATIONS')

    skins = ["light orange/light orange.json","pale green/pale green.json","blue/blue.json","fire/fire.json","independance blue/independance blue.json","light purple/light purple.json","grayscale/grayscale.json","pink/pink.json","dark cyan/dark cyan.json","red/red.json","persian green/persian green.json","orange/orange.json","pigeon blue/pigeon blue.json","dark pink/dark pink.json","kelly green/kelly green.json","violet/violet.json","dark purple/dark purple.json","cream/cream.json","crocodile/crocodile.json","hunter green/hunter green.json","og/og.json"]
    color = ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green","og"]

    #gltf_in = 'thirstplace.gltf'
    gltf_name = gltf_in.replace(".gltf","")
    
    uri_read_create(gltf_in)

    print(Bodyuri)
    #for skin in skins:
    print('└[skin replace]')
    i = 0
    with alive_bar(len(skins),force_tty=True) as bar:
        for skin in skins:
            f = open('/home/flo/projekt/new/zilla gltf create_v2/gltf in/'+gltf_in, 'r')
            f2 = open('/home/flo/projekt/new/zilla gltf create_v2/gltf out/'+color[i]+"_"+gltf_name+'.gltf', 'w')
            while True:
                line = f.readline()
                with open('/home/flo/projekt/new/zilla gltf create_v2/skins/'+skin) as json_file:
                    data = json.load(json_file)
                if Bodyuri in line:
                    line = line.replace(Bodyuri,data[color[i]+'_Body_Center'])
                if head_top_uri in line:
                    line = line.replace(head_top_uri,data[color[i]+'_head_top'])
                if mouthuri in line:
                    line = line.replace(mouthuri,data[color[i]+'_mouth'])
                if left_arm_1 in line:
                    line = line.replace(left_arm_1,data[color[i]+'_left_arm_1'])
                if left_arm_2 in line:
                    line = line.replace(left_arm_2,data[color[i]+'_left_arm_2'])
                if left_arm_3 in line:
                    line = line.replace(left_arm_3,data[color[i]+'_left_arm_3'])
                if right_arm_1 in line:
                    line = line.replace(right_arm_1,data[color[i]+'_right_arm_1'])
                if right_arm_2 in line:
                    line = line.replace(right_arm_2,data[color[i]+'_right_arm_2'])
                if right_arm_3!="":
                    if right_arm_3 in line:
                        line = line.replace(right_arm_3,data[color[i]+'_right_arm_3'])
                if right_leg_1 in line:
                    line = line.replace(right_leg_1,data[color[i]+'_right_leg_1'])
                if right_leg_2 in line:
                    line = line.replace(right_leg_2,data[color[i]+'_right_leg_2'])
                if right_leg_3 in line:
                    line = line.replace(right_leg_3,data[color[i]+'_right_leg_3'])
                if left_leg_1 in line:
                    line = line.replace(left_leg_1,data[color[i]+'_left_leg_1'])
                if left_leg_2 in line:
                    line = line.replace(left_leg_2,data[color[i]+'_left_leg_2'])
                if left_leg_3 in line:
                    line = line.replace(left_leg_3,data[color[i]+'_left_leg_3'])
                if tail_1 in line:
                    line = line.replace(tail_1,data[color[i]+'_tail_1'])
                if tail_2 in line:
                    line = line.replace(tail_2,data[color[i]+'_tail_2'])
                if tail_3 in line:
                    line = line.replace(tail_3,data[color[i]+'_tail_3'])
                if tail_4 in line:
                    line = line.replace(tail_4,data[color[i]+'_tail_4'])
                if shade_body in line:
                    line = line.replace(shade_body,data[color[i]+'_shade_body'])
                if shade_head in line:
                    line = line.replace(shade_head,data[color[i]+'_shade_head'])
                if shade_tail_1 in line:
                    line = line.replace(shade_tail_1,data[color[i]+'_shade_tail_1'])
                if shade_tail_2 in line:
                    line = line.replace(shade_tail_2,data[color[i]+'_shade_tail_2'])
                if shade_tail_3 in line:
                    line = line.replace(shade_tail_3,data[color[i]+'_shade_tail_3'])
                if shade_tail_4 in line:
                    line = line.replace(shade_tail_4,data[color[i]+'_shade_tail_4'])

                if not line:
                    break
                f2.write(line)
            f.close()
            f2.close()
            bar()
            i = i + 1

def uri_read_create(gltf_in):
     #/////////////URI READ/////////////
    print('└[uri read]')

    uri_reader = open('/home/flo/projekt/new/zilla gltf create_v2/gltf in/'+gltf_in, 'r')
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

    uri_reader.close()
    
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

    
    
    