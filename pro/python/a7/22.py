# code by : dev patel
# https://www.github.com/dev22419/

# taking amounts from user using while loop

i = 1
total = 0
while i <= 10:
    print("enter", i ,"value :")
    x = int(input(":> "))
    total = total + x
    i = i + 1

avg = total/10
print("")
print("your average is" , avg)