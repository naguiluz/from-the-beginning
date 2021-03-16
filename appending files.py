#set as a variable so that the open function can be used easier
employee_file = open("employees", "a") #open(file name, command) file should be in the same directory(folder) as the program
                                       # r = read
                                       # w = overwrite whatever is in the file
                                       # a = append/only add info to end of file
                                       # r+ = read and write


employee_file.write("Amanda - Sales") #instead of adding to the print out in python it appends to the actual file (REPEATS IF RUN MULTIPLE TIMES BE CAREFUL)
employee_file.write("\nKelly - Customer Service") #\n adds a new line after the last existing line in the file

employee_file.close() #good practice to close file after opening it