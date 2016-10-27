f=open('emo_list.txt','r')
emos=[]
for row in f.read().splitlines():
	sub=[]
	for item in row.split(','):
		sub.append(item)
	emos.append(sub)
print emos
	