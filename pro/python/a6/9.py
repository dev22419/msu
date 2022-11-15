# python program to find square and cube
# of a given number

# User defind method to find square 
def square (num):
	return  (num*num)

# User defind method to find cube
def cube (num) :
	return  (num*num*num) 

# Main code 
# input a number
number = int (input("Enter an integer number: "))

# square and cube
print("square of {0} is {1}".format(number, square(number)))
print("Cube of {0} is {1}".format(number, cube (number)))

