# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:42:52 2017

@author: yan.yl.chen
"""

#Write a function called string_search() that takes two
#parameters, a list of strings, and a string. This function
#should return  a list of all the indices at which the
#string is found within the list.
#
#You may assume that you do not need to search inside the
#items in the list; for examples:
#
#  string_search(["bob", "burgers", "tina", "bob"], "bob")
#      -> [0,3]
#  string_search(["bob", "burgers", "tina", "bob"], "bae")
#      -> []
#  string_search(["bob", "bobby", "bob"])
#      -> [0, 2]
#
#Use a linear search algorithm to achieve this. Do not
#use the list method index.
#
#Recall also that one benefit of Python's general leniency
#with types is that algorithms written for integers easily
#work for strings. In writing string_search(), make sure
#it will work on integers as well -- we'll test it on
#both.


#Write your code here!
def string_search(search_list, string):
    result =[]
    for i in range(0, len(search_list)):
        if search_list[i] == string:
            result.append(i)
    return result

            

#Feel free to add code below to test your function. You
#can, for example, copy and print the test cases from
#the instructions.

