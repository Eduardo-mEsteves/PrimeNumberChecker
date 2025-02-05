n = int(input("Number: ")) #Choose a number
x = 1 #it will run the while loop
dividers  = [] #it will show the dividers of that number

#number of dividers
d = 0

#division
r = 0 #will show the rest of the division

while x <= n:
  r = 0
  r = n % x
  if r == 0:
    d = d + 1
    dividers.append(x)

  x += 1

print(f"Dividers of {n}: {dividers}")
if d == 2:
  print(f"{n} is a prime number")
elif d > 2:
  print(f"{n} isn't a prime number")