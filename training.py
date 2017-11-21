import nltk

data = nltk.corpus("./cases_2017") 
 
print data.fileids()         # The list of file names inside the corpus
print len(data.fileids())            # Number of files in the corpus = 10788