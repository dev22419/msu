rows = 6
space =  20

for i in range(1, rows + 1):
    for j in range(0, space):
        print(end=" ")
    space = space - 2
    for j in range(1, i ):
        print(j, end=" ")
    for j in range(i , 0, -1):
        print(j, end=" ")
    print()
