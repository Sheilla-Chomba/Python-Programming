# This program basically displays the multiplication table

print("\t Multiplication table")

for j in range(1,10):
    print("  ",j,end="")
print("")
print("________________________________________________")

for i in range(1,10):
    print(i, end="| ")
    for j in range(1,10):
        print(i*j, end="\t")
    print("")