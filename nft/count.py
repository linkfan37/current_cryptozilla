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
    if (newstring in wallet_addresses)==1:
        continue 
    wallet_addresses.append(newstring)

print(wallet_addresses)

file.close()
for address in wallet_addresses:
    querystring = { "owner":address,
                    "order_direction":"desc",
                    "offset":"0",
                    "limit":"50",
                    "collection":"cryptozilla"
                    }
    response = requests.request("GET", url, params=querystring)
    print("response will be checked here")
    if response.status_code != 200:
        print('error:',response.status_code)
        continue
    print(response)

    zillasdat = response.json()['assets']
    sum = sum + len(zillasdat) 

    print(address,len(zillasdat))
    time.sleep(5)
print("Total:",len(wallet_addresses),sum)

