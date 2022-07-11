 #program to check if two strings are anagrams
name1 = input('Enter name 1: ')
name2 = input('Enter name 2: ')
#Here sort function is used
n1 = sorted(name1)
n2 = sorted(name2)
if (n1==n2):
    print('The Entered words are anagrams.')
else:
    print('The Entered words are not anagrams.')
