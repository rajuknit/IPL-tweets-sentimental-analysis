from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="izjbgtWWMtJv8ilpie6qkoSu0"
csecret="TYCwxHOLJIHkuEJrc9B2FHgIvka8zo0QqCUSdOmblQNy1BdwKt"
atoken="2343512629-zuricPp8h6sVdjUO1IRjPleVbTdU2VvdxJuP3SP"
asecret="AOTzqLjG5qcPfqBPU3i05QPhUOHh7LtscfQWyoCcxXL7k"

#from twitterapistuff import *

class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            createdat = all_data["created_at"]
            ff=open("output_singleteam/alltweet.txt",'a')
            sentiment_value, confidence = s.sentiment(tweet)
            ff.write(str(createdat)+" "+str(tweet)+" "+ str(sentiment_value)+" "+str( confidence)+"\n")
            ff.close()
            if confidence*100 >= 70:
                        output = open("output_singleteam/twitter-out.txt","a")
                        output.write(sentiment_value)
                        output.write('\n')
                        output.close()

            return True
        except:
            return True

    def on_error(self, status):
         print(status)

def abcd(s):
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[s])

#abcd("ipl")

while 1:
    p=raw_input("Enter which u want to check on twitter")
    abcd(s)
    
