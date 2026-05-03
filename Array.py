l=[2,7,11,15]       #Two sum array
target=9
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == target:
            print(i,j)
            break
        
