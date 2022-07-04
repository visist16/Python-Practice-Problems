#Removing Duplicate from an integer list
numbers = [1,2,3,3,4,4,5,6,6,7,8,9,7,5,1,5,]
print('Given Numbers',numbers)
#print(set(numbers))

newNumbers =[]

for i in numbers:
    if(i not in newNumbers):
        newNumbers.append(i)
        
print('After Removing Duplicates',newNumbers)        