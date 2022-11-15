x = int(input("Enter the value of X : "))
y = int(input("Enter the value of Y : "))
 
print("(",x,",",y,")",end="")
if(x<0 and y<0):
    print(" belongs to 3rd Quadrant.")
elif(x<0 and y>0):
    print(" belongs to 1st Quadrant.")
elif(x>0 and y>0):
    print(" belongs to 2nd Quadrant.")
else:
    print(" belongs to 4th Quadrant.")
