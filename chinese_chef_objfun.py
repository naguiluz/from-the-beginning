from chef_objfun import Chef #have to import the class we want to inherit

class Chinese_chef(Chef): #by adding (Chef), Chinese_chef inherits its proprties and functions

    def make_special_dish(self):
        print("The chef makes a pork buns.")

    def make_fried_rice(self):

        print("The chef makes fried rice.")