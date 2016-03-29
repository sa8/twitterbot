#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
reload(sys)  
sys.setdefaultencoding('utf8')
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
from keys import keys
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
replies=all
# filename=open(argfile,'r')
# f=filename.readlines()
# filename.close()
#  
#for line in f:
   # api.update_status(line)
   # time.sleep(900)#Tweet every 15 minutes
   
# twt = api.search(q="feel sad")     
#  
# #list of specific strings we want to check for in Tweets
# t = ['I feel sad',
#     'I feel so sad',
#     'i feel sad',
#     'i feel so sad',
#     'I feel a bit sad today'
#     ]
#  
# for s in twt:
#     for i in t:
#         if i == s.text:
#             sn = s.user.screen_name
#             m = "@%s The more you praise and celebrate your life, the more there is in life to celebrate. - Oprah Winfrey" % (sn)
#             s = api.update_status(m, s.id)
#             time.sleep(900)
#             
#twt = api.search(q="Hello World!")     
 

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, s):
    	sn=s.user.screen_name
    	m="@%s" % (sn)
    	api.update_status(m+'Be believing, be happy, don’t get discouraged. Things will work out. Gordon B. Hinckley',in_reply_to_status_id = s.id)
    	
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['feel so sad'])
