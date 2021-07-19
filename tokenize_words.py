# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:56:32 2021

@author: alba2
"""

from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

def word_sentence_tokenize(text):
  
  # create a PunktSentenceTokenizer
  sentence_tokenizer = PunktSentenceTokenizer(text)
  
  # sentence tokenize text
  sentence_tokenized = sentence_tokenizer.tokenize(text)
  
  # create a list to hold word tokenized sentences
  word_tokenized = list()
  
  # for-loop through each tokenized sentence in sentence_tokenized
  for tokenized_sentence in sentence_tokenized:
    # word tokenize each sentence and append to word_tokenized
    word_tokenized.append(word_tokenize(tokenized_sentence))
    
  return word_tokenized