#program to prime numbers from m to n
m = int(input('Enter Starting(m) value: '))
n = int(input('Enter Ending(n) value: '))
givenValue = m
if(m == 0 or 1):
    m = 2
primeNumbers = []
for i in range(m,n+1):
    for j in range(2,i):
        if(i%j==0):
            break 
    else:
        #print(i)
        primeNumbers.append(i)
print('Number of Prime Number in {} to {} is'.format(givenValue,n),len(primeNumbers),primeNumbers)
