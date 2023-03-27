# We are going to count the number of times each word has been mentioned in the wordcount.txt file

file=open("wordcount.txt")
fileRead=file.read()

words=fileRead.split()
counts=dict()

for word in words:
    counts[word]=counts.get(word,0)+1       # Simplifies what we would have done using the try and except
print(counts)