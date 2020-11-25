
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
print(mylist[:-1])
splitted = [ (elem[0]+1) for elem in mylist ]
print(splitted)
splitted.extend([10,11,12])
print(splitted)