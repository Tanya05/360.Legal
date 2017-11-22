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
    word_tokens=tokenizer.tokenize(text) #tokenizing
    #removing stop words and stemming
    final_tokens = []
    for word in word_tokens:
        if word.lower() not in stop_words:
            final_tokens.append(PorterStemmer().stem(word.lower()).encode())
    stripped_text = " ".join(final_tokens)
    return stripped_text

for dirpath, dirs, files in os.walk(path):
    #os.walk() generates the file names in a directory tree by walking the tree
    for f in files:
        fname = os.path.join(dirpath, f) #creates filename as path+file
        #print "fname=", fname
        with open(fname) as pearl:
            text = pearl.read()
            stripped_text = tokenize(text)
            token_dict[f] = stripped_text.translate(None, string.punctuation)
            #stored text corresponding to file in dictionary

tfidf = TfidfVectorizer(tokenizer=tokenize)
tfs = tfidf.fit_transform(token_dict.values())

for file in token_dict:
    print token_dict[file]

print tfs