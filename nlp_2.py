from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text()) #creates the entire novel into an object

#print(blob.words.count('joy')) #count the word 'joy' in the text of R&J

#print(blob.noun_phrases.count('lady capulet')) #46 times mentioned, the phrase "LC" shows up

#synonymns and antonymns of words

from textblob import Word

happy = Word('happy')

#print(happy.definitions) #made the dictionary, gives definitions

print(happy.synsets)