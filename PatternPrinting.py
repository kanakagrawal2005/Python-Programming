rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    
    # If row is even → print *
    if i % 2 == 0:
        for j in range(i):
            print("*", end=" ")
    
    # If row is odd → print #
    else:
        for j in range(i):
            print("#", end=" ")
    
    print()   # next line