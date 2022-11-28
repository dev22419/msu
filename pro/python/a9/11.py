row = 5

for i in range(1 , row + 1):
    for j in range(1 , 6):
        if j%2==0:
            print(0 , end=" ")
        else :
            print(1 , end=" ")
    print("")