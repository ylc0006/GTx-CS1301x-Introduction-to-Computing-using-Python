# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:44:10 2017

@author: yan.yl.chen
"""

#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute. 
#each setter should accept a value as an argument. If the 
#value is a valid value, it should set the corresponding 
#attribute to the given value. Otherwise, it should set the 
#attribute to False. Edit the constructor to use these new 
#setters and getters.
#
#Valid values for each setter are as follows:

# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False

#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.

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
            
                                  
#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.