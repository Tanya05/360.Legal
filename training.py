from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer
import string
import os
from re import sub
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import scipy

path = './cases_2017'
token_dict = {}

#function to tokenize, remove stop words and stem the remaining
def tokenize(text):
    #setting stop words (defining the corpus of stop words)
    
    #Remove non ascii characters 
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
        if (word.lower() not in stop_words):
            #remove numberd from words - trail231 becomes trial
            word = sub(r'\d+', '', word)
            final_tokens.append(str(PorterStemmer().stem(word.lower())))
    # stripped_text = " ".join(final_tokens)
    return final_tokens

for dirpath, dirs, files in os.walk(path):
    #os.walk() generates the file names in a directory tree by walking the tree
    for f in files:
        fname = os.path.join(dirpath, f) #creates filename as path+file
        #print "fname=", fname
        with open(fname) as pearl:
            text = pearl.read()
            #remove unwanted utf-8 characters
            text=sub(r'[^\x00-\x7f]|[\x11]',r' ',text)
            token_dict[f] = text.translate(None, string.punctuation)
            #stored text corresponding to file in dictionary

tfidf = TfidfVectorizer(tokenizer=tokenize)#expects list
#Fit the TfIdf model, and Transform a document into TfIdf coordinates
tfs = tfidf.fit_transform(token_dict.values())

#print tfs
feature_names = tfidf.get_feature_names()
#print feature_names
#print tfidf.vocabulary_
print tfs.shape

# svd = TruncatedSVD(n_components = 5)
# svdMatrix = svd.fit_transform(tfs)
tfs_matrix = [[0 for x in range(tfs.shape[1])] for y in range(tfs.shape[0])] 
i = 0
while i < tfs.shape[0]:
    j = 0
    while j < tfs.shape[1]:
        tfs_matrix[i][j] = tfs[i,j]
        j=j+1
    i=i+1


u,sigma,vt = scipy.linalg.svd(tfs_matrix)

 #Reconstruct MATRIX'
reconstructedMatrix= scipy.dot(scipy.dot(u,scipy.linalg.diagsvd(sigma,tfs.shape[0],len(vt))),vt)
print reconstructedMatrix