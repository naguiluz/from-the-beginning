
try: #try to execute the program
    number = int(input("Enter a number :"))
    print(number)

except ValueError: #if there is a value error (like inputting a string instead of a number) print this
    print("Invalid Input")

#this allows the program to specify to the user what is causing problems instead of just giving an error that is too broad