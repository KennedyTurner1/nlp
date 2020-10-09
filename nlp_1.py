from textblob import TextBlob 

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

#print(blob.sentences) #broke it up into a list

#print(blob.words) #list of  words

#print(blob.tags) #list of tuples, parts of speech [('Today', 'NN'), ('is', 'VBZ')]

#print(blob.noun_phrases) #['beautiful day', 'tomorrow', 'bad weather']

#sentiment analysis, most common but most valuable

#print(round(blob.sentiment.polarity,3)) #(polarity=0.07500000000000007, subjectivity=0.8333333333333333)
#polarity is pos or negative, it is more positive than negative (-1 to +1)
#subjectivity is how subjective it is
#we rounded it to 3 digits
'''
sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity,3))
    print(round(sentence.sentiment.subjectivity,3)) 
'''
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer()) #Sentiment(classification='neg', p_pos=0.47662917962091056, p_neg=0.5233708203790892)

#print(blob.sentiment) 

sentences = blob.sentences
'''
for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)

#print(blob.detect_language()) #en

spanish = blob.translate(to='es')

print(spanish) #Hoy es un hermoso dia. Mañana parece mal tiempo.

viet = blob.translate(to='vi')

print(viet)

print(viet.translate()) #Today is a beautiful day. Tomorrow it looks like bad weather.

print(spanish.translate()) #Today is a beautiful day. Tomorrow looks like bad weather.

from textblob import Word

index = Word('index')

print(index.pluralize()) #indices

animals = TextBlob('dog cat fish sheep bird').words

print(animals.pluralize()) #['dogs', 'cats', 'fish', 'sheep', 'birds'] #makes plural

cacti = Word('cacti')

print(cacti.singularize()) #cactus, makes single

word = Word('theyr') 

print(word.spellcheck()) #[('they', 0.5713042216741622), ('their', 0.42869577832583783)]

new = word.correct()

print(new) #they

sentence = TextBlob('Ths sentense has missplled wrds.')

sentence = sentence.correct()

print(sentence) #The sentence has misspelled words.
'''
