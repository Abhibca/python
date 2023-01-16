n1 = input('Enter First No :- ')
n2 = input('Enter second NO :- ')

#print(n2+''+n1)

print(n2[-1:-(len(n2)+1):-1]+' '+n1[-1:-(len(n1)+1):-1])

#print(n2[::-1]+' '+n1[::-1])