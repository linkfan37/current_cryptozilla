from typing import List
import json



Background={}
Skin = {}
Mouth = {}
Body ={}
Eyes = {}
Head = {}


List =[Background,Skin,Mouth,Body,Eyes,Head]
#table
i=1
file = open('/home/flo/projekt/nft/CryptoZillaProperties.csv', 'r')
while True:
 
    # Get next line from file
    line = file.readline()
    data = {}
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    
    splitted = line.split(',')
    if not "Number" in splitted:
        """ data.append({
            "tokenID":i,
            "Background":splitted[1],
            "Skin":splitted[2],
            "Mouth":splitted[3],
            "Body":splitted[4],
            "Eyes":splitted[5],
            "Head":splitted[6]
        })"""
        #data["tokenID"]=i
        data["Background"]=splitted[1].lower()
        data["Skin"] = splitted[2].lower()
        if splitted[3] != "-":
            data["Mouth"] = splitted[3].lower()
        if splitted[4] != "-":
            data["Body"] = splitted[4].lower()
        if splitted[5] != "-":
            data["Eyes"] = splitted[5].lower()
        splitted[6] = splitted[6].replace('\n',"")
        if splitted[6] != "-":
            data["Head"] = splitted[6].lower()
        print(data)
        with open('/home/flo/projekt/nft/test/{}.json'.format(i), 'w') as outfile:
            json.dump(data, outfile,indent=2)
            print("CREATED")
        i=i+1
        if i == 666 :
            i=i+1
            
#for di in List:
    #print(di)

