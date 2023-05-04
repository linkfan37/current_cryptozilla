import json
from alive_progress import alive_bar
def creategltfs( gltf_in = 'thirstplace.gltf'):
    print('CREATE COLOR VARIATIONS')

    skins = ["light orange/light orange.json","pale green/pale green.json","blue/blue.json","fire/fire.json","independance blue/independance blue.json","light purple/light purple.json","grayscale/grayscale.json","pink/pink.json","dark cyan/dark cyan.json","red/red.json","persian green/persian green.json","orange/orange.json","pigeon blue/pigeon blue.json","dark pink/dark pink.json","kelly green/kelly green.json","violet/violet.json","dark purple/dark purple.json","cream/cream.json","crocodile/crocodile.json","hunter green/hunter green.json","og/og.json"]
    color = ["light orange","pale green","blue","fire","independance blue","light purple","grayscale","pink","dark cyan","red","persian green","orange","pigeon blue","dark pink","kelly green","violet","dark purple","cream","crocodile","hunter green","og"]

    #gltf_in = 'thirstplace.gltf'
    gltf_name = gltf_in.replace(".gltf","")

    #/////////////URI READ/////////////
    print('└[uri read]')

    uri_reader = open('/home/flo/projekt/new/zilla gltf create_teeth/gltf in/'+gltf_in, 'r')

    for line_num, line in enumerate(uri_reader.readlines()):
        #print(line_num)

        if '"},' in line:
            line = str(line.replace('{"uri": "','').replace('"},','').strip())
        else:
            line = str(line.replace('{"uri": "','').replace('"}','').strip())
        
        #print(line)
        
        if line_num == 44 : Bodyuri=line
        if line_num == 2: head_top_uri=line
        if line_num == 4 : mouthuri=line
        if line_num == 18 : left_arm_1=line
        if line_num == 20 : left_arm_2=line
        if line_num == 22 : left_arm_3=line
        if line_num == 12 : right_arm_1=line
        if line_num == 14 : right_arm_2=line
        if line_num == 16 : right_arm_3=line
        if line_num == 30 : left_leg_1=line
        if line_num == 32 : left_leg_2=line
        if line_num == 34 : left_leg_3=line
        if line_num == 24 : right_leg_1=line
        if line_num == 26 : right_leg_2=line
        if line_num == 28 : right_leg_3=line
        if line_num == 36 : tail_1=line
        if line_num == 38 : tail_2=line
        if line_num == 40 : tail_3=line
        if line_num == 42 : tail_4=line
        if line_num == 45 : shade_body=line
        if line_num == 3: shade_head=line
        if line_num == 37 : shade_tail_1=line
        if line_num == 39 : shade_tail_2=line
        if line_num == 41 : shade_tail_3=line
        if line_num == 43 : shade_tail_4=line

        if line_num>45:
            break

    uri_reader.close()

    print(Bodyuri)
    #for skin in skins:
    print('└[skin replace]')
    i = 0
    with alive_bar(len(skins),force_tty=True) as bar:
        for skin in skins:
            f = open('/home/flo/projekt/new/zilla gltf create_teeth/gltf in/'+gltf_in, 'r')
            f2 = open('/home/flo/projekt/new/zilla gltf create_teeth/gltf out/'+color[i]+"_"+gltf_name+'.gltf', 'w')
            while True:
                line = f.readline()
                with open('/home/flo/projekt/new/zilla gltf create_teeth/skins/'+skin) as json_file:
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
