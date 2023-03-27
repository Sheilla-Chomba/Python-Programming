# Program to show the number of times a word has been mentioned
import time


print("..........We are going to play a game.........")
time.sleep(2)
print("You are going to enter 5 words of your choice as many times as you want."
      "\n Once you are done, enter the words \"DONE\"")
print("The computer will then guess how many times the words have been mentioned.")
time.sleep(2)
print("Let the games begin......")
time.sleep(1)

word=input("Enter the any word that comes to your head: ")

ultimateWord=word.upper()
words=dict()
words[ultimateWord]=1
while ultimateWord!="DONE":
    word = input("Enter the any word that comes to your head: ")
    ultimateWord = word.upper()
    try:
        words[ultimateWord] = words[ultimateWord] + 1
    except:
        words[ultimateWord] = 1

print(words)