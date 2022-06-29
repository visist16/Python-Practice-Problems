#program to reverse a number
n = int(input('Enter your n Value: '))
originalValue = n
reverse = 0 
while(n>0):
    num = n%10
    reverse = reverse*10+num
    n = n//10
    
print('Rever of number {} is {}'.format(originalValue,reverse))    