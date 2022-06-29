#program to swap numbers without using temporary variables

a = int(input('Enter the value of a = '))
b = int(input('Enter the value of b = '))

print('Entered value of a ',a)
print('Entered value of b ',b)

a = a+b
b = a-b
a = a-b

print("a = {}, b = {}".format(a,b))






'''#With Temp
a = int(input('Enter the value of a = '))
b = int(input('Enter the value of b = '))

print('Entered value of a ',a)
print('Entered value of b ',b)

temp = a 
a = b 
b = temp
print("a = {}, b = {}".format(a,b)) '''