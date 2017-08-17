# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:12:43 2017

@author: yan.yl.chen
"""

#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1 to the cost
# - If guacamole is True, add $0.75 to the cost


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, 
                 pico = False, corn = False):
        self.meat = meat
        self.to_go = to_go
        self.rice = rice
        self.beans = beans
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn
            
    # getters
    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return self.beans
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
        valid_meat = ["chicken", "pork", "steak", "tofu", False]
        if meat in valid_meat:
           self.meat = meat
        else:
           self.meat = False
    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False
    def set_rice(self, rice):
        valid_rice =["brown", "white", False]
        if rice in valid_rice:
            self.rice = rice
        else:
            self.rice = False
    def set_beans(self, beans):
        beans_options = ["black", "pinto", False]
        if beans in beans_options:
            self.beans = beans
        else:
            self.beans = False
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
        if self.meat in ["chicken", "pork" , "tofu"]:
            cost +=1
        if self.meat == "steak":
            cost +=1.5
        if self.extra_meat == True and self.meat != False:
            cost += 1
        if self.guacamole == True:
            cost += 0.75

        return cost

#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.