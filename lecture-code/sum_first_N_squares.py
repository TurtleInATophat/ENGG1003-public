N = 20

i = 1
sumN = 0
while i <= N:
    print(i)
    sumN += i**2
    i += 1

print('sum of integers 1...{} is {}'.format(N, sumN))
print('S_N = {}'.format((N*(N+1)*(2*N+1))/6))