number = int(input("Number: ")) #Choose a number
counter = 1 #it will run the while loop
divisors  = [] #it will show the divisors of that number

#number of dividers
divisorCount = 0

#division
remainder = 0 #will show the remainder of the division

while counter <= number:
  remainder = 0
  remainder = number % counter
  if remainder == 0:
    divisorCount += 1
    divisors.append(counter)

  counter += 1

print(f"Dividers of {number}: {divisors}")
if divisorCount == 2:
  print(f"{number} is a prime number")
elif divisorCount > 2:
  print(f"{number} isn't a prime number")
