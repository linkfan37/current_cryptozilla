import glob, os

def geturis(gltf_in = 'thirstplace.gltf'): 
    #/////////////URI READ/////////////
    print('└[uri read]')

    uri_reader = open('/home/flo/projekt/new/zilla gltf create/gltf in/'+gltf_in, 'r')
    uris = {}

    for line_num, line in enumerate(uri_reader.readlines()):
        #print(line_num)

        if '"},' in line:
            line = str(line.replace('{"uri": "','').replace('"},','').strip())
        else:
            line = str(line.replace('{"uri": "','').replace('"}','').strip())
        
        #print(line)
        
        if line_num == 2 : uris["Body_Center"]=line
        if line_num == 4 : uris["head_top"]=line
        if line_num == 6 : uris["mouth"]=line
        if line_num == 12 : uris["left_arm_1"]=line
        if line_num == 14 : uris["left_arm_2"]=line
        if line_num == 16 : uris["left_arm_3"]=line
        if line_num == 18 : uris["right_arm_1"]=line
        if line_num == 20 : uris["right_arm_2"]=line
        if line_num == 22 : uris["right_arm_3"]=line
        if line_num == 24 : uris["left_leg_1"]=line
        if line_num == 26 : uris["left_leg_2"]=line
        if line_num == 28 : uris["left_leg_3"]=line
        if line_num == 30 : uris["right_leg_1"]=line
        if line_num == 32 : uris["right_leg_2"]=line
        if line_num == 34 : uris["right_leg_3"]=line
        if line_num == 36 : uris["tail_1"]=line
        if line_num == 38 : uris["tail_2"]=line
        if line_num == 40 : uris["tail_3"]=line
        if line_num == 42 : uris["tail_4"]=line
        if line_num == 3 : uris["shade_body"]=line
        if line_num == 5 : uris["shade_head"]=line
        if line_num == 37 : uris["shade_tail_1"]=line
        if line_num == 39 : uris["shade_tail_2"]=line=line
        if line_num == 41 : uris["shade_tail_3"]=line=line
        if line_num == 43 : uris["shade_tail_4"]=line=line

        if line_num>45:
            break

    uri_reader.close()
    #print(uris)
    return uris
#geturis('thirstplace.gltf')
