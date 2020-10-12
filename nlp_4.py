from pathlib import Path

text = Path('RomeoandJuliet.txt').read_text() #read the text of Romeo and Juliet

import imageio

mask_image = imageio.imread('mask_heart.png') #we are loading our png image

from wordcloud import WordCloud

wc = WordCloud(colormap='prism',mask=mask_image, background_color='white') #mask is the shape the cloud takes

wc = wc.generate(text) #look at the entire text at one time and looking at the most used words to blow them up 

wc = wc.to_file('RomeoJuliet.png') #writing the wordcloud to a file