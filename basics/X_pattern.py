rows = 7 

for i in range(rows):
    for j in range(rows):
        if j == i or j == (rows - 1 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()