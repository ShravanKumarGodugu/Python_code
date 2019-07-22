'''
list [] - A list is a data type that can be used to store any type of data and number of variables information.
'''

N = []
A = int(raw_input('Enter a number'))

for i in range(A):
  B = int(raw_input('Enter number'))
  N.append(B)
print N

N.extend([20,30,40])  ## extend method to add two Lists
print N

N.insert(2,100)  ### Inserting a value in defined index position its starts from 0 to N-1
print N

N.remove(3)     ##To remove an item from the list we use remove method.
print N

N.pop(4)       ## To remove the item from a list with given index.
print N

print N.index(30)   ## To find out the position of a item. 

print N.count(2)    ## Counts the items in the list which were repeated.

N.sort()        ## To print the list in Ascending Order.
print N

N.reverse()     ## To Print the list in reverse.
print N
