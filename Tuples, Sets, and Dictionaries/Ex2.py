# Program to show the sorted version of the dictionary
import time


print("..........We are going to play a game.........")
time.sleep(2)
print("You are going to enter any number of words of your choice as many times as you want."
      "\nOnce you are done, enter the words \"DONE\"")
print("The computer will then show you the sorted version of the words.")
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
del words["DONE"]
print(sorted(words))