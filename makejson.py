import csv, json
from collections import OrderedDict
csvfile=open("cluster_results.csv","r")
csvreader = csv.reader(csvfile, delimiter=',')
emos=['joy','optimism','admiration','acceptance','fear','apprehension','amazement','surprise','loathing','disgust','rage','anger','anticipation','interest','sadness','disapproval','appreciation','grief','love']
main_json=OrderedDict()
main_json["name"]="flare"
main_json["description"]="flare"
main_json["children"]=[]
	#{"name":"flare","description":"flare","children":[]}
main_children=[]
for item in emos:
	dict=OrderedDict()
	dict["name"]=item
	dict["description"]="Tweets classified as "+item
	dict["children"]=[]
	main_json["children"].append(dict)
	#print main_json
for row in csvreader:
	#print len(row)
	tweet_description=OrderedDict()
	tweet_wise_emo=[]
	i=0
	while i<19:
		dict=OrderedDict()
		dict["name"]=emos[i]
		dict["description"]="How much "+emos[i]+" is present in the tweet"
		dict["size"]=row[i+2]
		i=i+1
		tweet_wise_emo.append(dict)
		#print tweet_wise_emo
	tweet_description["name"]=row[0]
	tweet_description["description"]="A classified tweet"
	tweet_description["children"]=tweet_wise_emo
		#print tweet_description
	for item in main_json["children"]:
	#print item
		if item["name"]==row[1]:
			item["children"].append(tweet_description)
			print "appended to "+row[1]
			#print item
#print "FINAL!!!!!!!!!!!!!!!!!!"
print main_json
output_json = json.dumps(main_json)
	#print output_json
with open('flare1.json','w') as outfile:
	json.dump(main_json,outfile)