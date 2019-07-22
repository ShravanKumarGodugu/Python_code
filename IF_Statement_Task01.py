## If Statement_task
# From 4 numbers print smallest two numbers.

a=int(raw_input("enter a number"))
b=int(raw_input("enter a number"))
c=int(raw_input("enter a number"))
d=int(raw_input("enter a number"))
highest=0
smallest=10000000000000000

if a>highest:
  highest=a
if a<smallest:
  smallest=a
if b>highest:
  highest=b
if b<smallest:
  smallest=b
if c>highest:
  highest=c
if c<smallest:
  smallest=c
if d>highest:
  highest=d
if d<smallest:
  smallest=d
print("highest is %d smallest is %d"%(highest,smallest))
print("highest is {} smallest is {}".format(highest,smallest))
print("highest is {1} smallest is {0}".format(highest,smallest))
print("highest is %d smallest is %d"%(smallest,highest))
