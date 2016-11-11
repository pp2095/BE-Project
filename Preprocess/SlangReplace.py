import csv
class SlangReplace:
	def __init__(self):
		#the slang to english mapping is stored in sd1.csv
		data_file=open('SD1.csv','rU')
		#create a dictionary that maps the slang to the english equivalent
		reader=csv.DictReader(data_file)
		self.data={}
		for row in reader:
			self.data[row['slang']]=row['meaning']
		data_file.close()
	def replace(self,filename):
	#this method does the actual replacement
		with open(filename) as slang_file:
			for line in slang_file:
				words = line.lower().split()
				replaced = []
				for y in words:
					if y in self.data:
						replaced.append(self.data[y])
					else:
						replaced.append(y)
				text = " ".join(map(str,replaced))
				new_main = open("final_text_file.txt", 'a+')
				new_main.write(text)
				new_main.write('\n')
				