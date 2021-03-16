
#set as a variable so that the open function can be used easier
employee_file = open("employees", "r") #open(file name, command) file should be in the same directory(folder) as the program
                                       # r = read
                                       # w = write/edit
                                       # a = append/only add info to end of file
                                       # r+ = read and write

#print(employee_file.readable()) = tells us whether the file can be read (true/false)
#print(employee_file.read()) = reads whole file
#print(employee_file.readline()) = reads first line, and then can read any number of following lines based on how many times this line is repeated
#print(employee_file.readlines()[1]) = reads every line and puts them into a list then prints that specific index of list

for employee in employee_file.readlines(): #turns the file into a list / then for each employee(index) in the file line being read it will print that employee
    print(employee + " is cool ")

employee_file.close() #good practice to close file after opening it