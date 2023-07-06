'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer Too low!

# What happens if you input the guess '6'?
  # Answer Too high!

# What happens if you input the guess '5'?
  # Answer Correct!

# What happens if you input the guess '-5'?
  # Answer Too low! 

# What happens if you input the guess '0'?
  # Answer Too low!

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer guess is lower than the correct number, guess is higher than the correct number but not equal 

# What happens if you change line 12 to if guess = number: ?
  # Answer there will be an error

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer print() follows after if statement 


