# Below is the programming exercise
# (Compute the perimeter of a triangle) Write a program that reads three edges for a
# triangle and computes the perimeter if the input is valid. Otherwise, display that
# the input is invalid. The input is valid if the sum of every pair of two edges is
# greater than the remaining edge.

# Prompts user to type in the value of each edge
edge1=eval(input("Type in the value of the first edge: "))
edge2=eval(input("Type in the value of the second edge: "))
edge3=eval(input("Type in the value of the third edge: "))

if (edge1+edge2)>edge3 and (edge1+edge3)>edge2 and (edge3+edge2)>edge1:
    perimeter=edge1+edge2+edge3
    print(f"The perimeter is {perimeter}")
else:
    print("The input is not valid")