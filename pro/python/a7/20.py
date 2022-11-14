# code by : dev patel
# https://www.github.com/dev22419/

x = int(input("starting year : "))
y = int(input("ending year : "))

z = y - x
i = 0

while x <= y:
    if (x % 400 == 0) and (x % 100 == 0):
        print("{0} is a leap year".format(x))
    elif (x % 4 ==0) and (x % 100 != 0):
        print("{0} is a leap year".format(x))
    else :
        pass
    x = x + 1