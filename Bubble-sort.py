#Bubble-sort Algorithm

l=[12,33,15,17,3,9]   
for ind1 in range(len(l)-1):
    for ind2 in range(len(l)-ind1-1):
        if l[ind2] > l[ind2+1]:
            l[ind2],l[ind2+1] = l[ind2+1],l[ind2]
print(l) 


output: [3, 9, 12, 15, 17, 33]
