#Print a string about the program
print ("Print leap year between two given years")
#Get the input start and end year from user
print ("Enter start year : ")
startYear = int(input())
print ("Enter last year : ")
endYear = int(input())

print ("List of leap years:")
#loop through between the start and end year
for year in range(startYear, endYear):
  #check if the year is a Leap year if yes print
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print (year)
