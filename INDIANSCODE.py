n=eval(input("enter number for diamond"))
for i in range(1,n,1):
    for d in range(n,i,-1):
        print(" ", end=" ")
    for j in range(1,i,-1):
        print(j, end=" ")
    for l in range(i,1,-1):
        print(l, end=" ")

    print(1,end=" ")
     
    for k in range(2,i+1):
        print(k, end=" ")
    print()

for i in range(n-2,0,-1):
    for d in range(n,i,-1):
        print(" ", end=" ")
    for j in range(1,i,-1):
        print(j, end=" ")
    for l in range(i,1,-1):
        print(l, end=" ")

    print(1,end=" ")
     
    for k in range(2,i+1):
        print(k, end=" ")
    print()
