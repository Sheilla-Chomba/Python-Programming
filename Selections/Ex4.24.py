# Below is the programming exercise
# (Game: pick a card ) Write a program that simulates picking a card from a deck of
# 52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.

import time

print("..................... We are going to play a card picking game....................")
time.sleep(2)
print("You get to pick any card of your choice from any of the suits and the computer displays what card you have chosen.")
time.sleep(1)
print("The suits will be represented as below:"
      "\n Clubs - 1"
      "\n Diamonds - 2"
      "\n Hearts - 3"
      "\n Spades - 4")
time.sleep(2)
print("The cards will be represented as below:"
      "\n Ace - 1"
      "\n 2 - 2"
      "\n 3 - 3"
      "\n 4 - 4"
      "\n 5 - 5"
      "\n 6 - 6"
      "\n 7 - 7"
      "\n 8 - 8"
      "\n 9 - 9"
      "\n 10 - 10"
      "\n Jack - 11"
      "\n Queen - 12"
      "\n King - 13")
time.sleep(2)

# Prompts user to type in their choice
card=eval(input("As per the instructions above, what card would you like to pick: "))

while card<1 or card>13:
    card = eval(input("Incorrect input. As per the instructions above, what card would you like to pick: "))

suit=eval(input("As per the instructions above, what suit would you like your card to come from: "))

while suit<1 or suit>4:
    suit = eval(input("Incorrect input. As per the instructions above, what suit would you like your card to come from: "))

if card==1:
    cardName="Ace"
elif card==2:
    cardName="2"
elif card==3:
    cardName="3"
elif card==4:
    cardName="4"
elif card==5:
    cardName="5"
elif card==6:
    cardName="6"
elif card==7:
    cardName="7"
elif card==8:
    cardName="8"
elif card==9:
    cardName="9"
elif card==10:
    cardName="10"
elif card==11:
    cardName="Jack"
elif card==12:
    cardName="Queen"
else:
    cardName="King"

if suit==1:
    suitName="Clubs"
elif suit==2:
    suitName="Diamonds"
elif suit==3:
    suitName="Hearts"
else:
    suitName="Spades"

print(f"The card you picked is the {cardName} of {suitName}")