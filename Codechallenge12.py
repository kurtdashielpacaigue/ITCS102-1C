n = 6

for uma in range(1, n + 1):              # rows
    for deez in range(n, uma, -1):       # spaces
        print(" ", end=" ")

    for y in range(uma, 1, -1):          # left descending numbers
        print(y, end=" ")

    print(1, end=" ")                    # middle 1

    for z in range(2, uma + 1):          # right ascending numbers
        print(z, end=" ")

    print() 
