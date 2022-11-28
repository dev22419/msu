row = 5 

for i in range(1, row +1):
    if i%2==0:
        for j in range(1,6):
            print(0 , end=" ")
        print("")
    else:
        for j in range(1,6):
            print(1 , end=" ")
        print("")