# Below is the programming exercise
# (Random character) Write a program that displays a random uppercase letter
# using the time.time() function.

import time
seconds=time.time()
randomValue=(int(seconds%26))+65
character=chr(randomValue)
print(character)