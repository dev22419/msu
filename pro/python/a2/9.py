#Program to find compound interest
p = float(input("Enter the principal amount : ")) 
 
r = float(input("Enter the rate of interest : "))

t = float(input("Enter the number of years : "))

 
#compute compound interest
amt=p*(pow((1+r/100),t))
ci=amt-p
#print
print("Compound interest : {}".format(ci))

