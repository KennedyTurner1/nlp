import nltk
#nltk.download("stopwords") just have to download once
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text()) 

stops = stopwords.words("english")
#print(stops) #list of words

#blob = TextBlob('Today is a beautiful day.')

#new_blob = [word for word in blob.words  if word not in stops]

#print(new_blob)

items = blob.word_counts.items()

#print(items) #collection of tuples, every word and their count

items = [word for word in items if word[0] not in stops]

#print(items)

from operator import itemgetter #pick which key to sort 

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

#print(sorted_items)

top20 = sorted_items[:20]

print(top20) #prints top 20 items

import pandas as pd

df = pd.DataFrame(top20, columns=['word', 'count'])

print(df)

axes = df.plot.bar(x='word', y='count', legend=False)

import matplotlib.pyplot as plt

plt.gcf().tight_layout()

plt.show()
