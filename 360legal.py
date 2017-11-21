import rtftotext as rtf
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer

#Read documents and convert to txt by using function striprtf
txt = open("./cases_2017/1.rtf").read()
txt=rtf.striprtf(txt)
#word_tokens = word_tokenize(txt)

#Use RegexpTokenizer to tokenize only words by removing numbers and punctuations.
tokenizer = RegexpTokenizer(r'[a-zA-Z][^\s]*\b')
word_tokens=tokenizer.tokenize(txt)

#Get stopwords library from nltk and add days and months to reduce number of tokens.
stop_words = set(stopwords.words('english'))
stop_words.update([u'january', u'febuary', u'march', u'april', u'may', u'june', u'july', u'august', u'september', u'october', u'november', u'december' ])
stop_words.update([u'monday', u'tuesday', u'wednesday', u'thursday', u'friday', u'saturday', u'sunday'])
final_tokens=[]

#remove stopwords
for word in word_tokens:
	if word.lower() not in stop_words:
		final_tokens.append(PorterStemmer().stem(word.lower()).encode())
print final_tokens