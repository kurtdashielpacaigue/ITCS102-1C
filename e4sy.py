for j in range(1,6,1):
    for k in range(6,j,-1):
        print(" ",end=" ")
    for l in range(1,2*j,1):
        print("*",end=" ")
    print()

for i in range(1,6,1):
    for l in range(1,i+1,1):
        print(i, end=(""))
    print()
