# ASK WHAT TO NAME FILE?
myfile = str(input("Enter file name you want to (TXT)write: "))

# OPEN GIVEN NAME .txt FILE IN WRITE MODE
with open (myfile, 'w') as file_object:

    contents = str(input("\nEnter text to write and save on file: "))
    # FOR MULTI LINE INPUT ASK AND WRITE AGAIN WITH "\n" AT THE END FOR NEW LINE
    file_object.write(contents)
file_object.close()

# OPEN SAME FILE AGAIN IN READ MODE
# PRINT LINES AND CLOSE

with open(myfile, 'r') as read_object:
    print (read_object.readlines())
read_object.close()
