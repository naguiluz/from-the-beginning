age = int(input("Enter your age: "))
name = input("Enter your name: ")

print("Hey, " + name + " . Were you born in " + str(int(2021 - age)),"?")
answer = input("Yes or No? : ") #this answer corresponds with the if below it
if answer == "no":

    print("How about " + str(int(2020 - age)), "?")
    answer = input("Yes or No? : ") #this answer corresponds with the if below it

    if answer == "yes":
        print("Great!")
    else:
        print("Well...that's weird")
elif answer == "yes":
    print("Great!")

#establish age and name as user inputs (setting age as an integer so it can be used for math)
#print question with math and variables inserted
#set up answer for upcoming if statements
#if user answer is no, print follow up question and establish answer for said question
#else/elif print responses
