from pathlib import Path
import spacy

nlp = spacy.load('en_core_web_sm') #loading this from the library

document1 = nlp(Path('RomeoandJuliet.txt').read_text()) #first text

document2 = nlp(Path('EdwardTheSecond.txt').read_text()) #second text

print(document1.similarity(document2)) #0.9125 is the similarity between the texts. 91.25% chance of those two books are the same
                                       #you could reasonably say that the authors are the same

