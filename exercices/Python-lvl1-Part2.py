#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################
print("**********************")
print("\tExercice 1")
print("**********************")
# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def array_check(nums):
  # CODE GOES HERE
  for i in list(range(1,4)):
    if i not in nums:
      return False
  return True

print("True:", array_check([1,1,2,3,1]))
print("False:", array_check([1,1,2,4,1]))
print("True:", array_check([1,1,2,1,2,3]))

#####################
## -- PROBLEM 2 -- ##
#####################
print("**********************")
print("\tExercice 2")
print("**********************")
# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  result = ""
  # CODE GOES HERE
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print("Hlo:", stringBits('Hello'))
print("H:", stringBits('Hi'))
print("Hello:", stringBits('Heeololeo'))

#####################
## -- PROBLEM 3 -- ##
#####################
print("**********************")
print("\tExercice 3")
print("**********************")
# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

print("True:", end_other('Hiabc', 'abc'))
print("True:", end_other('AbC', 'HiaBc'))
print("True:", end_other('abc', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################
print("**********************")
print("\tExercice 4")
print("**********************")
# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  return ''.join([char * 2 for char in str])

print("TThhee:", double_char("The"))
print("AAAAbbbb:", double_char("AAbb"))
print("HHii--TThheerree:", double_char("Hi-There"))
#####################
## -- PROBLEM 5 -- ##
#####################
print("**********************")
print("\tExercice 5")
print("**********************")
# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n in list(range(13,20)) and n != 15 and n != 16:
    return 0
  return n

print("6:", no_teen_sum(1,2,3))
print("3:", no_teen_sum(2,13,1))
print("3:", no_teen_sum(2,1,14))
#####################
## -- PROBLEM 6 -- ##
#####################
print("**********************")
print("\tExercice 6")
print("**********************")
# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

print("[2, 1, 2, 3, 4] expected 3: got", count_evens([2, 1, 2, 3, 4]))
print("[2, 2, 0] expected 3: got", count_evens([2, 2, 0]))
print("[1, 3, 5] expected 0: got", count_evens([1, 3, 5]))