from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
class StdOutListener(StreamListener):
    def on_data(self, data):
		f=open('raw_tweets.txt','a+')
		f.write(data)
		f.write('\n')
		return True
    def on_error(self, status):
        print status
class Streamer:
	def __init__(self):
		#uncomment these lines and add your own app's access tokens etc.
		'''
		self.access_token = ""
		self.access_token_secret = ""
		self.consumer_key = ""
		self.consumer_secret = ""
		'''
#Begins the streaming process
class GetData:
	def getTweets(self):
		l = StdOutListener()
		s=Streamer()
		auth = OAuthHandler(s.consumer_key, s.consumer_secret)
		auth.set_access_token(s.access_token, s.access_token_secret)
		stream = Stream(auth, l)
		#prompt user to enter a keyword of his/her choice
		str=raw_input("Enter a keyword: ")
		stream.filter(track=[str],languages=['en'])