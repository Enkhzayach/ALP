# Example code 1

number = 7
# number is defined as 7 
print("I have thought of a number between 1 and 10")
# I have thought of a number between 1 and 10 is printed out 
guess = int(input("Can you guess what it is?"))
# Can you guess what it is?--> question is imposed in class of 'int' to be answered

if guess == number:
  print("Correct!")
# == is comparing the equality between your guess and the number, and if its equal its printed out as Correct!
elif guess < number:
  print("Too Low!")
# if the previous condition is not true or if else, another words if your guess is lower than the number(<), then it is Too low!
else:
  print("Too High!")
# here else means if your guess does not match the conditions that are given previously, it means your guess it Too high!

# Example code 2

number1 = int(input("Please enter a number"))
#number1 is integer 
number2 = int(input("Please enter another number"))
#number2 is class integer as well, other number than number1

if number1 > number2:
  print("Number 1 is bigger than number 2")
  # this condition means if number1 is greater than number2 is true then number 1 is bigger than number 2 
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
  # if the previous condition is not true or if else, or number2 is greater than 1 then "Number 2 is bigger than number 1" will be printed out 
else:
  print("Both numbers are the same")
  #here if it does not satisfy the two conditions given above then it means Both numbers are the same

