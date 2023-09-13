#Declaring and defining a Recursive Function
def factorial(n):
  if n==0 or n==1:
    return n
  else:
    return n*factorial(n-1)

#Getting the n value to be calculated
n=int(input("Enter a Number: "))

#printing the Final Result
print("The factorial of {} is {}".format(n, factorial(n))) 