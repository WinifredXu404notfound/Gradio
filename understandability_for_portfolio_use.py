# -*- coding: utf-8 -*-
"""understandability-for portfolio use

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zpvIfW-31CNcPBf1_1SiG3EjQixUAD4

# Understandability %
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
## The corpus for recognizing puctuations in texts.
from nltk.stem import PorterStemmer
## for later lemmatization

def understandabiliy(text):
  text_word_bag_pucglued = list(text.split())
  text_sentence= nltk.sent_tokenize(str(text))
  text_word_bag_withpunc = []
  for sentence in text_sentence:
    text_word_bag_withpunc = nltk.word_tokenize(str(text_sentence))
  from nltk.tokenize import RegexpTokenizer
  tokenizer = RegexpTokenizer(r'\w+')
  text_word_bag = tokenizer.tokenize(str(text_word_bag_withpunc))
  num_words = len (text_word_bag_pucglued)
  num_periods = text_word_bag_withpunc.count('.') + text_word_bag_withpunc.count('?') + text_word_bag_withpunc.count('!') + text_word_bag_withpunc.count(';') + text_word_bag_withpunc.count(':') + text_word_bag_withpunc.count('...') + text_word_bag_withpunc.count('......')
  text_7ormorecha_word_bag = []
  for b in text_word_bag:
    if len(b) >= 7:
      text_7ormorecha_word_bag.append(b)
  
  text_tens_bag = []
  text_float_bag = []
  text_fraction_bag = []
  text_percent_bag = []
  for word in text_word_bag_withpunc:
    if len(re.findall(r"\d+", word)) > 0 and len(word) >= 2:
      text_tens_bag.append(word)
    if len(re.findall(r"\d*\.\d+", word)) > 0:
      text_float_bag.append(word)
    if len(re.findall(r"\d+\/\d+", word)) > 0:
      text_fraction_bag.append(word)
    if len(re.findall(r"\d+\%", word)) > 0:
      text_percent_bag.append(word)
  text_number_bag = list(set(text_tens_bag + text_float_bag + text_fraction_bag + text_percent_bag))
  abbr = [
        'approx.', 'appt.', 'apt.', 'A.S.A.P.', 'B.Y.O.B.', 'c/o', 'dept.', 'D.I.Y.', 'est.', 'E.T.A.', 'min.', 'misc.', 'Mrs.', 'R.S.V.P.', 'tel.', 'temp.', 'vet.', 'tsp', 't', 'tbs', 'tbsp', 'T', 'Ave.', 'Blvd.', 'NE', 'NW', 'SE', 'SW', 'BA', 'BS', 'MA', 'M.PHIL', 'MPHIL', 'JD', 'DC', 'PA', 'MD', 'SVP', 'EVP', 'CMO','ACE', 'AFAIK', 'ANI', 'IIRC', 'IQ', 'LOL', 'NP', 'ROFL', 'TY', 'WC', 'e.g.', 'etc', 'Etc', 'i.e.', 'n.b.', 'P.S.', 'viz']
  text_abbr_bag = []
  for word in text_word_bag_withpunc:
    if word in abbr:
      text_abbr_bag.append(word)
  text_longword_bag = list(text_7ormorecha_word_bag + text_number_bag + text_abbr_bag)
  num_longwords = len(text_longword_bag)
  if num_longwords > 0:
    LIX = round((num_words / num_periods) + (num_longwords * 100 / num_words)) 
    return str(100 - LIX ) + "%" + " " + "close to all audience."
  if num_longwords == 0 and num_periods > 0:
    LIX = round((num_words / num_periods)) 
    return str(100 - LIX ) + "%" + " " + "close to all audience."
  if num_periods == 0 :
    return "Please write at least a complete sentence with a period :)."

iface = gr.Interface(fn=understandabiliy, inputs="text", outputs="text")
iface.launch()