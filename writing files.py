#set as a variable so that the open function can be used easier
new_file = open("new file test", "w") #w will overwrite what is in a file
                                # adding a new file name will instead create a new file with the following contents

new_file.write("This is a file") #instead of adding to the print out in python it overwrites to the actual file (REPEATS IF RUN MULTIPLE TIMES BE CAREFUL)
new_file.write("\nnot too sure why i wouldn't just make a separate on my own") #\n adds a new line after the last existing line in the file

new_file.close() #good practice to close file after opening it