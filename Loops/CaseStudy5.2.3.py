# Below is a case study for giving users 5 subtraction quizzes

from random import randint

questions=5
while questions>0:
    num1=randint(0,10)
    num2=randint(0,10)

    answer=eval(input(f"What is {num1} - {num2} = "))

    if(answer==(num1-num2)):
        print(f"Your are correct. {answer} is the answer.")
    else:
        print(f"That is incorrect. The answer is the {answer}.")

    questions=questions-1
print("\nThat is the end of your quiz.")