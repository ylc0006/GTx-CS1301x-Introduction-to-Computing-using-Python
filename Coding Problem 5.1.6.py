# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 23:15:04 2017

@author: yan.yl.chen
"""

#Copy both your code and ours from the previous exercise.
#You should copy your Burrito class and our Meat, Rice, and
#Beans classes into this exercise.
#
#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.

#Paste your previous code here.
class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False
class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, 
                 pico = False, corn = False):
        self.meat = Meat(meat)
        self.to_go = to_go
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn
            
    # getters
    def get_meat(self):
        return self.meat.get_value()
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice.get_value()
    def get_beans(self):
        return self.beans.get_value()
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return self.guacamole
    def get_cheese(self):
        return self.cheese
    def get_pico(self):
        return self.pico
    def get_corn(self):
        return self.corn
    
    # setters
    def set_meat(self, meat):
           self.meat = Meat(meat)
    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False
    def set_rice(self, rice):
            self.rice = Rice(rice)
    def set_beans(self, beans):
            self.beans = Beans(beans)
    def set_extra_meat(self, extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False
    def set_guacamole(self, guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
        else:
            self.guacamole = False
    def set_cheese(self, cheese):
        if type(cheese)== bool:
            self.cheese = cheese
        else:
            self.cheese = False
    def set_pico(self, pico):
        if type(pico)==bool:
            self.pico= pico
        else:
            self.pico= False
    def set_corn(self, corn):
        if type(corn)==bool:
            self.corn= corn
        else:
            self.corn= False
    # get cost method
     
    def get_cost(self):
        cost = 5.0
        if self.meat.get_value() in ["chicken", "pork" , "tofu"]:
            cost +=1
        if self.meat.get_value() == "steak":
            cost +=1.5
        if self.extra_meat == True and self.meat.get_value() != False:
            cost += 1
        if self.guacamole == True:
            cost += 0.75
        return cost


#Write your new function here.
def total_cost(burritoList):
    total_cost =0
    for burrito in burritoList:
        total_cost += burrito.get_cost()
    return total_cost
    



#You can add code below to test your function. We'd suggest
#creating a couple instances of Burrito, adding them to a
#list, then passing that list to total_cost and printing the
#result.

burrito1 = Burrito("tofu", True, "brown", "pinto")
burrito2 = Burrito("steak", False, "hello", "world")
burritoList = [burrito1, burrito2]
print(total_cost(burritoList))

