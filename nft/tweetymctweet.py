import tweepy

# Authenticate to Twitter
CONSUMER_KEY ="IG2OE5LaWsJ93bVD7kZVDMqf1"
CONSUMER_SECRET = "XtXPjARS8Jd5qHtFZYanGR8EFLDBZ9YId9X0i3FIoHu9sWu6fk"
ACCESS_TOKEN ="1447644180294082560-2x9qBsbR4O4EOtOx01SJgYK1oPoCqr"
ACCESS_TOKEN_SECRET ="g2W4ob85eNRVDCnXYXXAdizwhraRs65mjTBdI6ewO6KgQ"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)
#user = api.get_user('florianLMC')

#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
#waiting for rate limits


# create new tweet from python string

#media = api.media_upload("/home/flo/projekt/nft/Black magic.png")
# Post tweet with image
tweet = "testing"
#api.update_status(status=tweet, media_ids=[media.media_id])
#Post text
api.update_status(status=tweet)
