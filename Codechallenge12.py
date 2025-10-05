n = 6

for uma in range(1, n + 1):               
    for deez in range(n, uma, -1):        
        print(" ", end=" ")

    for y in range(uma, 1, -1):           
        print(y, end=" ")

    print(1, end=" ")                     

    for z in range(2, uma + 1):           
        print(z, end=" ")

    print()                               
