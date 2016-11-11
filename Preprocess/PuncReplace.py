import string
import re
class PuncReplace:
	def replace_punc(self, line):
		regex = re.compile('[%s]' % re.escape(string.punctuation))
		out = regex.sub(' ', line)
		return out