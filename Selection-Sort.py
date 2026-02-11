l=[6,2,9,4,0,6]     
for ind1 in range(len(l)-1):
    leng=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[leng] > l[ind2]:
            leng=ind2
    l[ind1],l[leng]=l[leng],l[ind1]
print(l)


#output: [0, 2, 4, 6, 6, 9]
