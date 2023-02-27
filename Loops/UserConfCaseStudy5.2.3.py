# Below is a case study for giving users 5 subtraction quizzes
# This case study will also include the time it has taken to finish the quizzes and the number of correct answers
# This program also includes user confirmation on whether to continue with qustions or not

from random import randint
import time

correctAnswers=0
totalQuestions=0
startTime=time.time()
userConfirmation="Y"
while userConfirmation=="Y":
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

    totalQuestions+=1
    continuation=input("\nTo continue with the questions, press Y, if not press N: ")
    userConfirmation=continuation.upper()
print("\nThat is the end of your quiz.")
endtime=time.time()
timeUsed=endtime-startTime
print(f"You got {correctAnswers} out of {totalQuestions}.")
print(f"You have done {totalQuestions} questions.")
print(f"You have used {int(timeUsed)} seconds to complete the quizzes.")