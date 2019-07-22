'''IF STATEMENT AND LOGICAL OPERATORS
  In Python we have 3 Logical Operatiors those are
  1.AND   2.OR   3.NOT
'''

D = int(raw_input("Enter a Number"))
N = int(raw_input("Enter a Number"))
E = int(raw_input("Enter a Number"))
G = int(raw_input("Enter a Number"))

if D>N and D>E and D>G:
  print("Higest is {}".format(D))
elif D<N and D<E and D<G:
  print("Smallest is {}".format(D))

if N>D and N>E and N>G:
  print("Higest is {}".format(N))
elif N<D and N<E and N<G:
  print("Smallest is {}".format(N))

if E>D and E>N and E>G:
  print("Higest is {}".format(E))
elif E<D and E<N and E<G:
  print("Smallest is {}".format(E))

if G>D and G>E and G>N:
  print("Higest is {}".format(G))
elif G<D and G<E and G<N:
  print("Smallest is {}".format(D))