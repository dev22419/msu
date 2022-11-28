row = 5
space = 20

for i in range(1 , row + 1):
    for j in range(0, space):
        print(end=" ")
    space = space - 1
    for j in range(1 , i + 1):
        print(j , end=' ')
    print(" ")
