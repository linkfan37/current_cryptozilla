from typing import List
import json



Background=[]
Skin = []
Mouth = []
Body =[]
Eyes = []
Head = []


List =[Background,Skin,Mouth,Body,Eyes,Head]
counts={}
#table
i=0
myin=0    
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
        safedf=0
        if not splitted[1].lower() in Background:
            Background.append( splitted[1].lower())
            #counts[splitted[1].lower()]=1
            #safedf=1
        if not splitted[2].lower() in Skin:
            Skin.append( splitted[2].lower())
            counts[splitted[2].lower()]=1
            safedf=1
        if  not splitted[3].lower() in Mouth and splitted[3] != "-":
            Mouth.append(splitted[3].lower())
        if  not splitted[4].lower() in Body and splitted[4] != "-":
            Body.append(splitted[4].lower())
        if  not splitted[5].lower() in Eyes and splitted[5] != "-":
            Eyes.append(splitted[5].lower())
        splitted[6] = splitted[6].replace('\n',"")
        if  not splitted[6].lower() in Head and splitted[6] != "-":
            Head.append(splitted[6].lower())
        #print(data)
        if splitted[2].lower() in Skin and safedf !=1:
            counts[splitted[2].lower()]+=1
            myin+=1
            print(myin)
        with open('/home/flo/projekt/nft/test/{}.json'.format(i), 'w') as outfile:
            json.dump(data, outfile,indent=2)
            #print("CREATED")
        i=i+1
            
print("Background: ", len(Background))
print("Skin: ", len(Skin))
print("Mouth: ", len(Mouth))
print("Body: ", len(Body))
print("eyes: ", len(Eyes))
print("head: ", len(Head))
#for di in List:
    #print(di)
print(counts)

