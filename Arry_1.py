from array import *

arr=array('i',[])

n = int(input("Enter size of the array"))

for i in range(n):
    y =int(input(("Enter the next number to array")))
    arr.append(y)
    
print(arr)

val = int(input("Enter value search out of array"))

c=0
for j in arr:
    if j==val:
        print(c)
        break
    c+=1
        
print(arr.index(val))   #function directly can be used to search index
