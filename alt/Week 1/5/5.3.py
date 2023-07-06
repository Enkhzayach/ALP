# Starter Code

number = 5
# 5 is idendified as number 
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
# "can you guess what it is" is asked in class of 'int' imposing question 

if guess < number:
  print("Too Low!")
# if guessed number is lower than 5, there will be too low answer
if guess > number:
  print("Too High!")
# if guessed number is higher than 5, it shows its Too high
