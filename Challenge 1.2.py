#Defining a function to calculate the Leap Year
def LeapYear(year):
  if(year % 4 == 0 and year % 100!= 0) or year % 400 == 0:
    return True
  else:
    return False

#Getting The Value of Year
year=int(input("Enter a year: "))

#Checking and Printing whether the given year is leap year or not
if LeapYear(year):
  print("{} is a Leap Year".format(year))
else:
  print("{} is not a Leap Year".format(year))