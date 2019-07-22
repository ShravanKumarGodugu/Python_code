''' Printing EVEN & ODD Numbers 
    Condition for Even Numbers n(variable)%2==0:
    If above is true is even or else it ODD Numbers
'''
N = int(raw_input('Enter a Number '))

if N%2==0:
  print("The given number is Even {}" .format(N))

else:
  print("The Given Number is ODD {}" .format(N))