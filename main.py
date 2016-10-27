import stream_main as s
import create_dict as cd
import cluster
import csv
import webbrowser
'''
#This method retrieves tweets and puts them in raw_tweets.txt, 
#puts tweet text in extracted_text.txt, slang replaced tweets in final_text_file.txt
#and non-duplicated tweets in final_tweets.txt.
s.get()
#this method takes the tweets from final_tweets.txt, classifies themm into their emotions and
#stores the result in result_file.csv
cluster.make_cluster('final_tweets.txt','result_file1.csv')
#this converts the csv result into json format and stores in flare.json
cd.make_json('result_file1.csv','flare.json')
#this opens the web page having results
webbrowser.open('http://localhost/BE Project Vis/index.html')
'''

#cluster.make_cluster('final_tweets_maria.txt','maria_results12.csv')


cd.make_json("maria_results1.csv","flare1.json")
cd.make_json("trump_results.csv","flare2.json")
webbrowser.open('http://localhost/BE Project Vis/index1.html')
#webbrowser.open('http://localhost/BE Project Vis/index2.html')

