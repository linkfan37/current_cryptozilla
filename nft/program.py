
import requests
import time

url = "https://api.opensea.io/api/v1/assets"
sum = 0
file = open('/home/flo/projekt/nft/wallets.csv', 'r')
wallet_addresses = []
while True:
 
    # Get next line from file
    line = file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    newstring = line.replace('\n','') 
    if (line in wallet_addresses)==1:
        continue 
    wallet_addresses.append(newstring)

print(wallet_addresses)
file.close()