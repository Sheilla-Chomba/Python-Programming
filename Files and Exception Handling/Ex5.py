# Opening a file as requested by user

file=input("Enter the file that you would like to read: ")

try:
    fileOpen=open(f"{file}")

except:
    print(f"The file {file} cannot be found.")
    quit()

for fileName in fileOpen:
    print(fileName)