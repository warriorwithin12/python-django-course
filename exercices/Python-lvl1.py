#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

print("***********")
print(" Exercise 1")
print("***********")
# Use indexing to print out the following:
# 'd'
print("slice 'd':", s[0])
# 'o'
print("slice 'o':", s[-1])
# 'djan'
print("slice 'djan':", s[0:4])
# 'jan'
print("slice 'jan':", s[1:4])
# 'go'
print("slice 'go':", s[4:])
# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############
print("***********")
print(" Exercise 2")
print("***********")
# Given this nested list:
l = [3,7,[1,4,'hello']]
l[2][2] = "goodbye"
print("Reassign \"hello\" to be \"goodbye\":", l[2][2])


###############
## Problem 3 ##
###############
print("***********")
print(" Exercice 3")
print("***********")
print("Using keys and indexing, grab the 'hello' from the following dictionaries:")

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print("d1 grab: {}, d2 grab: {}, d3 grab: {}".format(d1.get("simple_key"), d2.get("k1").get("k2"), d3.get("k1")[0].get("nest_key")[1][0]))
###############
## Problem 4 ##
###############
print("***********")
print(" Exercice 4")
print("***********")
# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print("Converted to set: {}".format(set(mylist)))

###############
## Problem 5 ##
###############
print("***********")
print("Exercice 5")
print("***********")
# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {} and he is {} years old".format(name, age))