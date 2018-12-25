import tweepy

#Authentication
consumer_key = 'jjJkmq1vwdBYbRrVRSdtpA'
consumer_secret = 'Enter Here'
access_token = 'Enter Here'
access_token_secret = 'Enter Here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print (tweet.text)
    print(tweet.created_at)
    print(tweet.id)
    #print (tweet)
    
    break

#user = api.me()
#print (user.name)