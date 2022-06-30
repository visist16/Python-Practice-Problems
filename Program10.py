#program to get the matching characters in a string
name = input('Enter name: ')
print(name.count('0'))
matchingCharacters = []
for i in name:
    if(name.count(i)>1):
        matchingCharacters.append(i)
        
print(matchingCharacters)

'''#Not Allowing Multiple Char
name = input('Enter name: ')    2
print(name.count('0'))
matchingCharacters = set()
for i in name:
    if(name.count(i)>1):
        matchingCharacters.add(i)
        
print(matchingCharacters)'''