import requests
from datetime import date, timedelta,timezone
from datetime import datetime

today = (datetime.now(timezone.utc) - timedelta(hours=24))
ts = today.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(ts)

url = "https://api.opensea.io/api/v1/events"



querystring = { "collection_slug":"cryptozilla",
                "only_opensea":"false",
                "offset":"0",
                "limit":"50",
                "occurred_after":ts,
                "event_type":"successful"
                }
response = requests.request("GET", url, params=querystring)
print("response will be checked here")
if response.status_code != 200:
    print('error')
    exit()
print(response)

zillasdat = response.json()['asset_events']

if(len(zillasdat)!=0):
    for j in range(0,len(zillasdat) ):
        print(j,zillasdat[j]['asset']['token_id'])



