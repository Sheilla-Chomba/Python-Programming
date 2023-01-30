# Below is the programming exercise
# (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
# number. The program prompts the user to enter a three-digit number and determines
# whether the user wins according to the following rules:

import random
import time
# Prompts user to type in the number they want
print("...............We are going to play a game...................")
time.sleep(2)
print("Type in a three digit number and stand the chance to win $10,000")
time.sleep(2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(2)
guessNumber=eval(input("Enter your lottery number: "))

while guessNumber<0 or guessNumber>999:
    guessNumber = eval(input("Wrong input. Kindly enter a three digit number: "))

lotteryNumber=random.randint(0,9991)
guessDig1=guessNumber%10
remNum=guessNumber//10
guessDig2=remNum%10
guessDig3=remNum//10

lotteryDig1=lotteryNumber%10
remlotNum=lotteryNumber//10
lotteryDig2=remlotNum%10
lotteryDig3=remlotNum//10

if guessNumber==lotteryNumber:
    print("This is exact match :)"
          "\nCongrats!! You have won $10,000")
elif (guessDig1==lotteryDig2 and guessDig2==lotteryDig3 and guessDig3==lotteryDig1)\
     or (guessDig1==lotteryDig1 and guessDig2==lotteryDig3 and guessDig3==lotteryDig2)\
     or (guessDig1==lotteryDig3 and guessDig2==lotteryDig2 and guessDig3==lotteryDig1) \
     or (guessDig1 == lotteryDig2 and guessDig2 == lotteryDig1 and guessDig3 == lotteryDig3)\
     or (guessDig1==lotteryDig3 and guessDig2==lotteryDig1 and guessDig3==lotteryDig2):
    print("You have entered all the digits :)"
          "\nCongrats!! You have won $3,000")
elif guessDig1==lotteryDig2 or guessDig1==lotteryDig3 or guessDig2==lotteryDig1 or \
     guessDig2==lotteryDig3 or guessDig3==lotteryDig1 or guessDig3==lotteryDig2 or \
     guessDig1 == lotteryDig1 or guessDig2 == lotteryDig2 or guessDig3 == lotteryDig3:
    print("You have entered at least one of the digits :)"
          "\nCongrats!! You have won $1,000")
else:
    print("Sorry there is no match. Try Again some other day.")