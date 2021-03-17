from Student import Student #importing the student class from a separate file

student1 = Student("Nic", "Marine Biology", 2.9, False) #sets the values onto the object that was created separately
print("Hello, " +student1.name+ ". How are you today? Right now your gpa is " +str(student1.gpa))