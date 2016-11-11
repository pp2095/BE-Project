import json
import re, string
class ReadJson:
	def readjson(self):
		tweets = []
		#make a list of the text of the tweets from w.txt
		for line in open('raw_tweets.txt'):
		  try: 
			tweets.append(json.loads(line))
		  except:
			pass
		i=0
		f=open("extracted_text.txt","a+")
		chars=set(string.printable)
		while i<len(tweets):
			#encode it to utf-8 and replace all occurrences of \n within a single tweet to ensure that one tweet is saved per line in the output file
			d=tweets[i]['text'].encode('utf-8')
			d=d.replace('\n',' ')
			d=d.replace('"','')
			d=d.replace('#','')
			#remove URLs
			d = re.sub(r"https\S+", "", d)
			d = re.sub(r"@\S+","AT_USER", d)
			for x in d:
				if x in chars:
					continue
				else:
					d=d.replace(x,'')
			f.write(d)
			f.write('\n')
			i=i+1
			
			