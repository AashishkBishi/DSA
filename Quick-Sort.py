def quick(l):      
    if len(l) <= 1:
        return l
    pivot=l[0]
    left= [ele for ele in l[1:] if ele < pivot]
    right = [ele for ele in l[1:] if ele >= pivot]
    return quick(left) + [pivot] + quick(right)
l=[2,6,-5,0,7,6,11,2] 
print(quick(l)) 


output: [-5, 0, 2, 2, 6, 6, 7, 11] 
