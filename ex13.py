import itertools 
'''Getting the inputs'''
n=int(input("Insert the number of digits"))
s=int(input("Insert the sum of the numbers"))

'''Generating numbers'''
for i in range(1,n)


''''''


''' Choosing and print the numbers with sum = s'''
result = [seq for i in range(n, 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == s]
print result
