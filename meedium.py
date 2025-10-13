for i in range(1,11,1):
    for l in range(1,6,1):
        print(f"{i}x{l}={i*l}", end="\t\t")
    print()

for j in range(1,6,1):
    for k in range(6,j,-1):
        print(" ",end="")
    for l in range(1,j+1,1):
        print("*",end=" ")
    print()
