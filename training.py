import rtftotext as rtf #file containing function to convert rtf files to txt files
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer
import string
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = './cases_2017'
token_dict = {}


#function to tokenize, remove stop words and stem the remaining
def tokenize(text):
    #setting stop words (defining the corpus of stop words)
    stop_words = set(stopwords.words('english'))
    #following added to remove dates
    stop_words.update([u'january', u'february', u'march', u'april', u'may', u'june', u'july', u'august', u'september', u'october', u'november', u'december' ])
    stop_words.update([u'monday', u'tuesday', u'wednesday', u'thursday', u'friday', u'saturday', u'sunday'])
    #setting regexp so that only words taken and punctuation and digits removed
    tokenizer = RegexpTokenizer(r'[a-zA-Z][^\s]*\b')
    word_tokens=tokenizer.tokenize(txt) #tokenizing
    final_tokens = []
    #removing stop words and stemming
    for word in word_tokens:
    if word.lower() not in stop_words:
        final_tokens.append(PorterStemmer().stem(word.lower()).encode())
    return final_tokens

for dirpath, dirs, files in os.walk(path):
    for f in files:
        fname = os.path.join(dirpath, f)
        print "fname=", fname
        with open(fname) as pearl:
            text = pearl.read()
            token_dict[f] = text.lower().translate(None, string.punctuation)