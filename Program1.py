#program to print sum of 1 to n
p = int(input('Enter n value = '))
print('entered value', p)

sum = 0
for i in range(1,p+1):
    sum = sum + i
    
print('Total sum from 1 to {} is {}'.format(p,sum))