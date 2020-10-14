import spacy

nlp = spacy.load('en') #load the library

nlp = spacy.load('en_core_web_sm') #loading this from the library

document = nlp("In 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C), devoted to developing web technologies")

for entity in document.ents: 
    print(entity.text, ':', entity.label_) #able to identify certain word's in your sentence and label them 

#similarity detection
#we use this for plagiarism 


