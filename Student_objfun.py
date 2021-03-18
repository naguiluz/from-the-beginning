class Student: #creating student class that can be imported to other files
    def __init__(self, name, major, gpa): #these are values that will be applied to the object
        self.name = name # self.name applies the passed in "name" to the object itself
        self.major = major
        self.gpa = gpa


    def on_honor_roll(self): #defining a function that can determine if the student is on the honor roll or not by testing the gpa
        if self.gpa >= 3.5:
            return True
        else:
            return False