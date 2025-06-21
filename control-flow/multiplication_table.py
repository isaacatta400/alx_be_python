number = int(input("Enter a number to see its multiplication table:"))

#fruits = ["apple", "banana", "cherry"]

#for fruit in fruits:
  #print(fruit)

#message = "Hello, world!"

#for A in message:
  #print(A)

for iterator in range(1, 11):
  product = iterator * number
  print(number, "*", iterator, "=", product)