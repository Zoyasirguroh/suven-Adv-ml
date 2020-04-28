# Self to do excerises in class
"""
1> find the frequency or count of the non-stop words and rank them in descending order. Use the above df['tweet'] data.
"""

# version 1 : Explains how to solve the above problem.
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
  cnt[word] += 1

print(cnt)


# be careful. We don't want alphabetical sorting !!!!! 
print(sorted(cnt.items()))


# For reverse alphabetical sorting !!!!! 
sorted(cnt.items(), reverse=True)


# Solution : to print the list of tuples in reverse order according to count
l = cnt.items()
print(sorted(l, key = lambda item: item[1], reverse=True))


# Counter class can directly read from iterable object. No need of FOR loop 
# Counter takes iterable object like a list or set, 
# hence recode above like this
mywords = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt = Counter(mywords)

print(cnt)


#--------------------------------------------

# Version-2 : Not using Counter class

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq))) # it would only print the object


# Recall from Python Course : to print contents of zip object 
# convert to list or set
list(zip(wordlist, wordfreq))


#---------------------------------------

# all concepts clear.
# Now focusing on our problem df['tweet']

import nltk
from nltk.corpus import stopwords

# removing all punctuation marks 
df['tweet'] = df['tweet'].str.replace('[^\w\s]','')

# convert all words to the lower case
df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# remove stop words
stop = stopwords.words('english')
df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

# converting df to list of string
all_words =   [str(i) for i in df['tweet'].values]
print(all_words) # note its a list of string phrases, NOT list of all strings

all_split_words = []

print("----------------------------------------")

# extracting each word and making a single list of strings
for word in all_words :
  for x in word.split():   
   all_split_words.append(x) 

# see the list of all string words
print(all_split_words)

# Create a frequency distribution. it needs a list of string words only.
freq = nltk.FreqDist(all_split_words)

# Show the words in the list, with counts in desc order.
sorted(list(freq.items()), key = lambda item: item[1], reverse=True )

#--------------------------------

"""
Extra Reading 
https://programminghistorian.org/en/lessons/counting-frequencies
"""

