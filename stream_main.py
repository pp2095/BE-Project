import GetTheData as gd
import Preprocess as sp
def get():
	try:
		g=gd.GetData()
		g.getTweets()
	except KeyboardInterrupt:
		print 'Stopping streaming'
	finally:
		r=gd.ReadJson()
		r.readjson()
		#now replace slang with english
		s=sp.SlangReplace()
		s.replace('extracted_text.txt')
		print 'Slang done'		
		#remove duplicate entries
		tweets=[]
		with open('final_text_file.txt','r') as textfile:
			for row in textfile:
				tweets.append(row)
		final=[]
		for item in tweets:
			if item not in final:
				final.append(item)
			else:
				continue
		f=open('final_tweets.txt','w+')
		for item in final:
			f.write(item)
			#f.write('\n')
		return True