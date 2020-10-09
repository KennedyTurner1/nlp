from textblob import TextBlob 

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob)

print(blob.sentences) #broke it up into a list

print(blob.words) #list of  words

