print("\t\t *")

for uma in range(1, 11, 1):  
    for deez in range(10, uma, -1):
        print(" ", end=" ")
    for y in range(1, uma + 1, 1):
        print("*", end=" ")
    for z in range(1, uma, 1):
        print("*", end=" ")
    print()

for uma in range(9, 0, -1):  
    for deez in range(10, uma, -1):
        print(" ", end=" ")
    for y in range(1, uma + 1, 1):
        print("*", end=" ")
    for z in range(1, uma, 1):
        print("*", end=" ")
    print()

print("\t\t *")
