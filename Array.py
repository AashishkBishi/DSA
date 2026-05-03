l=[2,7,11,15]       #Two sum array
target=9
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == target:
            print(i,j)
            break

        
l=[2,5,8,3,6,1,9,4,7,3,6,5]   #find min , max
min=l[0]
max=l[0]
for num in l:
    if num < min:
        min=num
    if num > max:
        max=num
print(min)
print(max) 
