print("\t\t *")  

for uma in range(1, 11, 1):  
    for deez in range(10, uma, -1):
        print(" ", end=" ")
    for y in range(1, uma, 1):
        print("*", end=" ")
    for z in range(1, uma, 1):
        print("*", end=" ")
    print()

for uma in range(1, 11, 1):  
    for deez in range(1, uma, 1):
        print(" ", end=" ")
    for y in range(10, uma, -1):
        print("*", end=" ")
    for z in range(10, uma, -1):
        print("*", end=" ")
    print()

print("\t\t *") 

#second more advanced triangle please input 11 i got this from an indian coder lol

#n=eval(input("enter number for triangle"))
#for i in range(1,n,1):
   # for d in range(n,i,-1):
        #print(" ", end=" ")
    #for j in range(1,i,-1):
        #print("*", end=" ")
    #for l in range(i,1,-1):
        #print("*", end=" ")

    #print(1,end=" ")
     
    #for k in range(2,i+1):
        #print("*", end=" ")
    #print()

#for i in range(n-2,0,-1):
    #for d in range(n,i,-1):
        #print(" ", end=" ")
    #for j in range(1,i,-1):
        #print("*", end=" ")
    #for l in range(i,1,-1):
        #print("*", end=" ")

    #print("*",end=" ")
     
    #for k in range(2,i+1):
        #print("*", end=" ")
    #print()
