class Student: #creating student class that can be imported to other files
    def __init__(self, name, major, gpa, is_on_probation): #these are values that will be applied to the object
        self.name = name # self.name applies the passed in "name" to the object itself
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation