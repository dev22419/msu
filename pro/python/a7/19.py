# code by : dev patel
# https://www.github.com/dev22419/

sum = 0
N = 5
for i in range(1, N + 1) :

    if (i & 1) :
        sum += i / (i + 1)
    
    else :
        sum -= i / (i + 1)
    


print(sum)