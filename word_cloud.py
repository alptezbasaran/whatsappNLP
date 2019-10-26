# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:49:54 2019

@author: Alp Tezbasaran
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from wordcloud import WordCloud
from collections import Counter



# Importing the dataset
dataset = pd.read_csv('chat_processed.txt', delimiter=" ", sep=" ", header=None, engine = 'python', encoding = 'utf_8_sig', error_bad_lines = False)

ayak = dataset.replace(np.nan, '', regex=True)
alp = ayak.values.tolist()


seperator = ' '
ciplak_ayak = []
for i in range(len(alp)):
    ciplak_ayak.append(seperator.join(alp[i]))
    ciplak_ayak[i] = ciplak_ayak[i].strip()

cok_guzel_ciplak_ayak = seperator.join(ciplak_ayak)

re.sub(' +', ' ',cok_guzel_ciplak_ayak)

with open("processed2.txt", "w", encoding="utf-8") as f:
    f.write(cok_guzel_ciplak_ayak)

# Some parameters
WC_height = 1080
WC_width = 1920
WC_max_words = 500

# Generate a word cloud image
stopwords = ['de','da','mi','com','http','you','the','misin','it','www','to','end',
             'youtube', 'youtu','with', 'https','thi','musun','mu','ref']

stopwords = ['de','da','mi','com','http','you','the','misin','it','www','to','end',
             'youtube', 'youtu','with', 'https','thi','musun','mu','ref','ben','sen','o',
             'biz', 'siz', 'onlar','Neden', 'ne', 'ya','bu', 'bir', 'nasil','yok' 'degil',
             'evet','hayir','Evet','Hayir', 'Her', 'zaman', 'hala', 'biri']

stopwords = common_words
stopwords = []

def analyze(name, wc, stopwords):
    wordcloud = WordCloud(collocations=False, stopwords = stopwords, prefer_horizontal=0.9, max_words=wc,
                      height=WC_height, width=WC_width).generate(cok_guzel_ciplak_ayak)
    wordcloud.to_file(name[:-4]+str(wc)+".png")

word_counts = [50, 100, 150, 200, 250, 300,350, 400, 450, 500]
word_counts = [200]
for wc in word_counts: analyze(wc)

reg = '(.(?P<Date>\d{1,2}/\d{1,2}/\d{1,2}), (?P<Time>\d{1,2}:\d{1,2}:\d{1,2} \wM). (?P<Sender>.* .*): (?P<Message>.+))|(?P<Raw>^\w.*$)'
reg_bad = '^.+omitted'
reg_link = '.(?P<Date>\d{1,2}/\d{1,2}/\d{1,2}), (?P<Time>\d{1,2}:\d{1,2}:\d{1,2} \wM). (?P<Sender>.* .*): (?P<Message>.*http.*|.*com.*)'
seperator = ' '

# New method
files=['tutku.txt', 'osc.txt', 'yesim.txt', 'zerey.txt']
files=['anne', 'aysenur', 'bugrik','ceylan','gulcin','iliknotron',
       'ilkokul', 'iron', 'omer', 'osc','serra','sule','suna',
       'yesim','zerey']
files=['tutku']
for _ in files:
  with open(_+'.txt', encoding="utf_8_sig") as chat:
      line = chat.readline()
      ayak = []
      while line:
          if len(re.findall(reg_bad, line)) == 1 or len(re.findall(reg_link, line)) == 1 :
            line = chat.readline(); continue
          for m in re.finditer(reg, line):
            if m.group('Message')==None: ayak.append(m.group('Raw')); continue
            ayak.append(m.group('Message'))
          line = chat.readline()
      cok_guzel_ciplak_ayak = seperator.join(ayak)
      analyze(_+'.txt',200,stop_en_tr)


# Number of occurance and reporting
def replace_bad_character(line):
    return line.strip().replace(u"\u202a", "").replace(u"\u200e", "").replace(u"\u202c", "").replace(u"\xa0", " ")

cok_guzel_ciplak_ayak_processed = replace_bad_character(cok_guzel_ciplak_ayak)
most_occur = dict(Counter(cok_guzel_ciplak_ayak_processed.split()).most_common(100))

stop_from_chat = []
with open('occurance.csv','w', newline='' , encoding='utf-8') as file:
  for key, val in most_occur.items():
    file.write(key.ljust(10)+'\t'+str(val).rjust(4)+'\n')
    stop_from_chat.append(key)


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
extra = [ 'misin', 'bi', 'sey' , 'su' , 'eger' , 'mi' , 'nicin' , 'icin' , 'hic' ,'eger' , 'cunku' , 'cok', 'birsey', 'birkac', 'bazi', 'aslinda']
stop_en_tr = stopwords.words('english') + stopwords.words('turkish') + extra
