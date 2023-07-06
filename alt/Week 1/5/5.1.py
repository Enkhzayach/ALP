'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 

# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
#it means if guess is equal to 5 then it it correct!
if guess < number:
  print("Too Low!")
# if guess is lower than 5 then it is lower than the targeted number

if guess > number:
  print("Too High!")
# == compares objects for equality
