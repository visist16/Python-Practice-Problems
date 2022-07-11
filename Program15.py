#Finding Numericaldigits in a string
name = input('Enter a name: ')

'''for i in name:
    if(i.isdigit()):
        print(i)
        count = count+1'''
     



count = 0
for i in name:
    if(i in numbers):
        count = count+1
        print(i)
print('number of digits in {} is {}'.format(name,count))       
