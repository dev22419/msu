# code by : dev patel
# https://www.github.com/dev22419/

i = 0

while i <= 5:
    x = input("enter a letter : ")
    x.lower()
    if x in ["a","e","i","o","u"]:
        print("it is an vowel . ")
        i = 6
    else :
        print("you entered an constant . ")