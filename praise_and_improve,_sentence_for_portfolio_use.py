# -*- coding: utf-8 -*-
"""praise and improve, sentence-for portfolio use

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QrGoqFKuYIOIPZhmm-5gkGYUpwDiYEz0

# Praise: no long and hard-to-grasp sentences
# Improve: long and hard-to-grasp sentences
"""

!pip install gradio
import gradio as gr

## This is the general version of readability score calculator. It hasn't been matched to targeting audience yet.
import re
import warnings
warnings. filterwarnings("ignore")
## There might be some circumstances the codes can run properly but python will still present warnings. This is used to ignore the warnings.
import nltk
nltk.download('punkt')

def longsentence(text):
  text_word_bag_pucglued = list(text.split())
  text_sentence= nltk.sent_tokenize(str(text))
  text_word_bag_withpunc = []
  for sentence in text_sentence:
    text_word_bag_withpunc = nltk.word_tokenize(str(text_sentence))
  from nltk.tokenize import RegexpTokenizer
  tokenizer = RegexpTokenizer(r'\w+')
  text_word_bag = tokenizer.tokenize(str(text_word_bag_withpunc))

  ## Detecting long sentences.
  long_sent_word_bag = []
  long_sents = []
  sent_word_bag = [sentence.split() for sentence in text_sentence]
  for each_sent_word_bag in sent_word_bag :
    if len(each_sent_word_bag) >= 20:
      long_sent_word_bag.append(each_sent_word_bag)

  for i in long_sent_word_bag:
    long_sents.append(" ". join(i))

  ## Count the number of long sentences.
  num_long_sentence = len(long_sent_word_bag)

  num_periods = text_word_bag_withpunc.count('.') + text_word_bag_withpunc.count('?') + text_word_bag_withpunc.count('!') + text_word_bag_withpunc.count(';') + text_word_bag_withpunc.count(':') + text_word_bag_withpunc.count('...') + text_word_bag_withpunc.count('......')
  ## Calculate the number of periods.

  if num_long_sentence > 0:
    returncontent = "Improve 🤔\n" + str(num_long_sentence) + " " + "long and hard-to-grasp sentence(s) highlighted in your text. See if you can split it(them).\n" + "Long sentences: " + " " +  str(long_sents) + " \n" + "How to split a long sentence?\n" + "You can split a long sentence by cuting it at the commas/conjunctions/relative pronouns/relative adverbs. Then you can refer to the last thing in the last sentence at the begining of the next sentence. Or you can directly rewrite the long sentence in a simpler way.\n" + "See examples here:\n" + "That's WHY we bring the culture to YOU, who don't yet know your favorite...and to you, who don't even know beer IS your favorite.\n" + " 👉 That's WHY we bring the culture to YOU. You may don't yet know your favorite, or don't even know beer IS your favorite.\n" + "When people walk in H&M they see cheap and good-looking clothes but seldom think about the children in India who made them and suffer terrible working environments and extremely low salaries.\n" + "👉 When people walk in H&M, they see cheap and good-looking clothes. But they seldom think about children who made them. These children live and work in terrible working environments in India. They only have extremely low salaries in return.\n" + "It's 'dansk for alle' where you can find any type of Danish education and make it wing your career in Denmark.\n"+"👉 It's 'dansk for alle' where you can find any type of Danish education. It will wing your career in Denmark.\n" + "When practicing, please remember to stop a little bit longer after periods than you do after commas/conjunctions/relative pronouns/relative adverbs. Then your audience can really catch up them as shorter and easier-to-grasp sentences."
    return returncontent

  if num_long_sentence == 0 and num_periods > 0:
    returncontent = "Praise 🎉\n"  + "Congrats! No long and hard-to-grasp sentences now!"
    return returncontent
  
  if num_periods == 0:
    return "Please write at least a complete sentence with a period :)."
 

iface = gr.Interface(fn=longsentence, inputs="text", outputs="text")
iface.launch()