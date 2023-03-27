# We are going to display the word with the highest number of counts in wordcount.txt file

file=open("wordcount.txt")
fileRead=file.read()

words=fileRead.split()
counts=dict()

for word in words:
    counts[word]=counts.get(word,0)+1       # Simplifies what we would have done using the try and except


bigCount=None
bigword= None
for eachWord, count in counts.items():
    if bigCount is None or bigCount<count:
        bigword=eachWord
        bigCount=count
print(bigword,bigCount)