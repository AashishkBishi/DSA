#Binary-sort Algorithm


k=[-17,-5,0,1,5,12,15,23]  
target=15
least=0
high=len(k)-1
while least <high:
    mid = (least+high)//2
    if k[mid] > target:
        high = mid-1
    if k[mid] < target:
        least = mid+1
    else:
        print(mid)
        break
else:
    print(-1)      




# output: 6
