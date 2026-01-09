l=[1,2,'a',5,6,'b',9]     #linear-search Algorithm
target=9
for ind in range(len(l)-1):
    if l[ind] == target:
        print(ind)
        break
else:
    print(-1)  
