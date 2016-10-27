import csv, umbc, pickle, math
from scipy import spatial
def make_cluster():
	#load antonyms
	ant_file=open('antonyms.csv','r')
	ant_reader=csv.reader(ant_file,delimiter=',')
	ant_dic={}
	for row in ant_reader:
		ant_dic[row[0]]=row[1]
	#load pre-existing dictionary
	dict=pickle.load(open('dict.p','rb'))
	#load stop words
	with open('stopwords.txt','r') as f:
		sw = f.read().splitlines()
	neg_words=['not','no','never','cannot',"can't","won't"]
	neg,there=False,True
	wordlist=[]
	#load main emotions
	f=open('emo_list.txt','r')
	emos=[]
	for row in f.read().splitlines():
		sub=[]
		for item in row.split(','):
			sub.append(item)
		emos.append(sub)
	#load opposite emotions
	opp_emos=[]
	f=open('ant_emos.txt','r')
	for row in f.read().splitlines():
		sub=[]
		for item in row.split(','):
			sub.append(item)
		opp_emos.append(sub)
	#parse the sentence file
	res_file=open("maria_results1.csv","a+")
	csvwriter = csv.writer(res_file, delimiter=',')
	for row in open('final_tweets.txt','r'):
		sentence=row
		print "Tweet is: "+sentence
		list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		for word in sentence.split():
			v=[]
			v1=[]
			#ignore stop word
			if word.lower() in sw:
				continue
			#check if already present
			elif word.lower() in wordlist:
				word=word.lower()
			#check if negation introduced
			elif word.lower() in neg_words:
				neg=True
				continue
			#have none of the other choices
			else:
				print word
				if neg==True:
					try:
						word=ant_dic[word.lower()].lower()
						neg=False
					except KeyError:
						word=word.lower()
						there=False
				else:
					word=word
			#if there isn't any negation, go for the word directly
			if neg==False:
				try:
					v1=dict[word]
				except KeyError:
					for sublist in emos:
						semo=[]
						for item in sublist:
							score=umbc.sss(word,item)
							semo.append(score)
						v1.append(max(semo))
						dict[word]=v1
			#negation is present
			else:
				#antonym available
				if there==True:
					try:
						v1=dict[word]
					except KeyError:
						for sublist in emos:
							semo=[]
							for item in sublist:
								score=umbc.sss(word,item)
								semo.append(score)
							v1.append(max(semo))
						dict[word]=v1
				else:
					neg,there=False,True
					for sublist in opp_emos:
						semo=[]
						for item in sublist:
							score=umbc.sss(word,item)
							semo.append(score)
						v1.append(max(semo))
			for x in v1:
				if math.isinf(x)==True:
					v.append(0)
				else:
					v.append(x)
			list=[sum(x) for x in zip(list, v)]
		#initialize target vectors
		joy=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		optimism=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		admiration=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		acceptance=[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		fear=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		apprehension=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
		amazement=[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
		surprise=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
		loathing=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
		disgust=[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
		rage=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
		anger=[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
		anticipation=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
		interest=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
		sadness=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
		disapproval=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
		appreciation=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
		grief=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
		love=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
		#calculate cosine distances
		if list==[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
			#tweet cannot be classified
			continue
		r=[]
		r.append(1-spatial.distance.cosine(list,joy))
		r.append(1-spatial.distance.cosine(list,optimism))
		r.append(1-spatial.distance.cosine(list,admiration))
		r.append(1-spatial.distance.cosine(list,acceptance))
		r.append(1-spatial.distance.cosine(list,fear))
		r.append(1-spatial.distance.cosine(list,apprehension))
		r.append(1-spatial.distance.cosine(list,amazement))
		r.append(1-spatial.distance.cosine(list,surprise))
		r.append(1-spatial.distance.cosine(list,loathing))
		r.append(1-spatial.distance.cosine(list,disgust))
		r.append(1-spatial.distance.cosine(list,rage))
		r.append(1-spatial.distance.cosine(list,anger))
		r.append(1-spatial.distance.cosine(list,anticipation))
		r.append(1-spatial.distance.cosine(list,interest))
		r.append(1-spatial.distance.cosine(list,sadness))
		r.append(1-spatial.distance.cosine(list,disapproval))
		r.append(1-spatial.distance.cosine(list,appreciation))
		r.append(1-spatial.distance.cosine(list,grief))
		r.append(1-spatial.distance.cosine(list,love))
		#find maximum cosine similarity and corresponding emotion
		m=max(r)
		indices=[i for i,j in enumerate(r) if j==m]
		emos=['joy','optimism','admiration','acceptance','fear','apprehension','amazement','surprise','loathing','disgust','rage','anger','anticipation','interest','sadness','disapproval','appreciation','grief','love']
		for i in indices:
			res=emos[i]
			print res
		csvwriter.writerow([sentence,res,r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18]])
	pickle.dump(dict, open( "dict1.p", "wb" ) )		
				