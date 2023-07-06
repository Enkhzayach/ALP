# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter other number"))

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Both numbers are the same")
if number3 > number1:
  print("number 3 is greater than number 1")
elif number1 > number3:
  print("number 3 is less than number 1")
else:
  print("number 3 and number 1 are the same")
if number3 > number2:
  print("number3 is greater than number 2")
elif number2 > number3:
  print("number 2 is greater than number 3")
else:
  print("number3 and number2 are same")