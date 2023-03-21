# How to read data from a file using python

notes=open("exe.txt")
for data in notes:
    print(data.rstrip())        # prints the data without the extra blank line like in Ex1.py