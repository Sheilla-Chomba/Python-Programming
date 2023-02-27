# Below is a case study for giving users 5 subtraction quizzes
# This case study will also include the time it has taken to finish the quizzes and the number of correct answers

from random import randint
import time

questions=5
correctAnswers=0
startTime=time.time()
while questions>0:
    num1=randint(0,10)
    num2=randint(0,10)

    if num1<num2:
        num1,num2=num2,num1

    answer=eval(input(f"What is {num1} - {num2} = "))

    if(answer==(num1-num2)):
        print(f"Your are correct. {answer} is the answer.")
        correctAnswers+=1
    else:
        print(f"That is incorrect. The answer is the {num1-num2}.")

    questions=questions-1
print("\nThat is the end of your quiz.")
endtime=time.time()
timeUsed=endtime-startTime
print(f"You got {correctAnswers} out of 5.")
print(f"You have used {int(timeUsed)} seconds to complete the quizzes.")