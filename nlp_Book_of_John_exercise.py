import nltk
#nltk.download("stopwords") #just have to download once
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path

text = TextBlob(Path('Book_of_John.txt').read_text()) 

#print(text)

stops = stopwords.words("english")

blob = [word[0] for word in text.tags if word[0] not in stops and word[1] == 'NN']

my_dict = {word:blob.count(word) for word in blob}

my_dict = my_dict.items()

from operator import itemgetter #pick which key to sort 

sorted_items = sorted(my_dict, key=itemgetter(1), reverse=True) #sort by the highest value, index 1

#print(sorted_items)

top15 = sorted_items[:15]

print(top15) 

listToStr = ' '.join([str(element) for element in top15]) 

import imageio

mask_image = imageio.imread('mask_oval.png') #we are loading our png image

from wordcloud import WordCloud

wc = WordCloud(colormap='prism',mask=mask_image, background_color='white') #mask is the shape the cloud takes

wc = wc.generate(listToStr) #look at the entire text at one time and looking at the most used words to blow them up 

wc = wc.to_file('BookJohn.png') #writing the wordcloud to a file
