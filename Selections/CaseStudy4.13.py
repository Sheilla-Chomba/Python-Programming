# Below is a case study to determine whether a user has won the lottery or not

import random
import time
# Prompts user to type in the number they want
print("...............We are going to play a game...................")
time.sleep(2)
print("Type in a two digit number and stand the chance to win $10,000")
time.sleep(2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(2)
guessNumber=eval(input("Enter your lottery number: "))

while guessNumber<0 or guessNumber>99:
    guessNumber = eval(input("Wrong input. Kindly enter a two digit number: "))

lotteryNumber=random.randint(0,99)
guessDig1=guessNumber%10
guessDig2=guessNumber//10

lotteryDig1=lotteryNumber%10
lotteryDig2=lotteryNumber//10

if guessNumber==lotteryNumber:
    print("This is exact match :)"
          "\nCongrats!! You have won $10,000")
elif guessDig2==lotteryDig1 and guessDig1==lotteryDig2:
    print("You have entered all the digits :)"
          "\nCongrats!! You have won $3,000")
elif guessDig2==lotteryDig1 or guessDig1==lotteryDig2 or guessDig1==lotteryDig1 or guessDig2==lotteryDig2:
    print("You have entered at least one of the digits :)"
          "\nCongrats!! You have won $1,000")
else:
    print("Sorry there is no match. Try Again some other day.")