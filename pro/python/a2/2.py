#program to calculate simple interest with long code
print("Enter the Principle Amount: ")
p = int(input())
print("Enter Rate of Interest (%): ")
r = float(input())
print("Enter Time Period: ")
t = float(input())
si = (p*r*t)/100
print("\nSimple Interest Amount : ")
print(si)

#This is a simple Method with short code
print("\n")
p=int(input("Enter the principal Amount : \n"))
r=float(input("Enter the Rate of interest(%) : \n"))
t=float(input("Enter the Time in Years : \n"))
si=(p*r*t)/100
print("The simple interest is : ",si)