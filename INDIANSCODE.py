n= 8
for i in range(1,n,1):
    for b in range(n,i,-1):
        print(" ", end=" ")
    for h in range(i,1,-1):
        print(h, end=" ")
    
    print(1,end=" ")
    
    for j in range(2,i+1):
        print(j, end=" ")
    print()
    
for i in range(n-2,0,-1):
    for b in range(n,i,-1):
        print(" ", end=" ")
    for h in range(i,1,-1):
        print(h, end=" ")
    
    print(1,end=" ")
    
    for j in range(2,i+1):
        print(j, end=" ")
    print()
