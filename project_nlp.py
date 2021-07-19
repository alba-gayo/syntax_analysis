# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:59:27 2021

@author: alba2
"""
# T O K E N I Z E
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
example_text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(example_text))


# S T O P   W O R D S
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]


print(word_tokens)
print(filtered_sentence)

# S T E M 
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))
    
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))

# L E M M A T I Z E    
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))

# examples codecademy
import re
 
text = "1,        2,        3,      4" 
 
result = re.sub(r'\s', '', text)
 
print(result) 
# 1,2,3,4

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
 
my_words = ["I", "was", "pizza", "for", "Halloween"]
 
stemmed = [stemmer.stem(token) for token in my_words]
 
print(stemmed)
# ['I', 'wa', 'pizza', 'for', 'Halloween']