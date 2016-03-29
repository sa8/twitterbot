#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys,random
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

list =['Happiness is not the absence of problems, it’s the ability to deal with them.-Steve Maraboli',
'You are here in this world to make a positive difference.',
'You have the power to spend your life with people who truly matter to you.',
'Be believing, be happy, don’t get discouraged. Things will work out. Gordon B. Hinckley']  
 

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, s):
    	sn=s.user.screen_name
    	m="@%s " % (sn)
    	api.update_status(m+random.choice(list),in_reply_to_status_id = s.id)
    	
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['feel so sad'])
