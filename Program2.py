#Program to reverse a string
name = input('Enter a name: ')
print('Entered name is: ',name)

reverse = ""
for i in name:
    reverse = i + reverse
print('Reversed value of {} is {}'.format(name,reverse))    