import urllib2 
import re
from collections import Counter
'''Gets profile link as input and insert the text in a text file'''
def html_to_txt():
	url = str(input("Provide us the profile link"))
	response = urllib2.urlopen(url)
	with open('output.txt','w') as f:
		f.write(response.read())

'''Reading text file'''
with open('output.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage) #Finds all the different words

cap_words = [word.upper() for word in words] #Change all the different word to caps so that wont be different

word_counts = Counter(cap_words) #Count number of appearance of each word

#Finds the most frequent word
def findMostCommon(Counter):
  mostFreq = ''
  mostFreqCount = 0
  for k in Counter:
    if Counter[k] > mostFreqCount:
      mostFreqCount = Counter[k]
      mostFreq = k
  return mostFreq

  print "Most Frequent word is", mostFreq , "with " , mostFreqCount ,"appearances"