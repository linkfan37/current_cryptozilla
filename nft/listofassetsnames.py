from typing import List
import json



Background={}
Skin = {}
Mouth = {}
Body ={}
Eyes = {}
Head = {}


List =[Background,Skin,Mouth,Body,Eyes,Head]
ListStr = ["Background: ","Skin: ","Mouth: ","Body: ","Eyes: ","Head: "]
#table
i=0
file = open('/home/flo/projekt/nft/CryptoZillaProperties.csv', 'r')
r=0
while True:
 
    # Get next line from file
    line = file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    
    splitted = line.split(',')
    if not "Number" in splitted:
        splitted[6] = splitted[6].replace('\n',"")
        for i in range(1,len(splitted)):
            if splitted[i]!="-":
                #lookup if already in dict, if yes add 1 else add to dict 
                if (splitted[i].lower() in List[i-1].keys()):
                    List[i-1][splitted[i].lower()] = List[i-1][splitted[i].lower()] + 1
                else:
                    List[i-1][splitted[i].lower()] = 1
                if splitted[i] == "":
                    print(r)
                #else:
                     #List[i-1][splitted[i].lower()]= 1
    r=r+1
k=0

l=0
"""
for di in List:
    print(ListStr[k])
    for d in di:
        print(d," : ",round(di[d]* 0.1,3))
        di[d] = round(di[d]* 0.1,3)

    k=k+1
    print("\n")
"""
List2=[]
for i in range(0,len(List)):
    List2.append(sorted(List[i].items(), key=lambda x:x[1]))

Background={}
Skin = {}
Mouth = {}
Body ={}
Eyes = {}
Head = {}


List =[Background,Skin,Mouth,Body,Eyes,Head]

for i in range(0,len(List2)):
    for tup in List2[i]:
        List[i][tup[0]]=tup[1]
    print(List2[i])
    print("\n")

k = 0
for di in List:
    print(ListStr[k])
    for d in di:
        print(d," : ",round(di[d]* 0.1,3))
        di[d] = round(di[d]* 0.1,3)

    k=k+1
    print("\n")
k=0
for di in List:
    print(ListStr[k])
    for d in di:
        print(d)

    k=k+1
    print("\n")



    


