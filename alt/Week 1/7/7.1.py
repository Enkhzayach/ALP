# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
answer = input() 
#identation is to indicate if the inner statement belongs to the upper block since there is no identation its outside of the loop

while answer != "Paris":
# as long as the answer is not Paris following functions are executed
  print("Incorrect! Try again.")
  #its in the inner loop therefore answer is not Paris it prints out Incorrect! Try again.
  answer = input("What is the capital of France?: ")
   
    
  # its in the inner loop of while, question what is the capital of France is imposed

print("Correct!")
# its outside of the loop therefore the answer is other than not equal to Paris, Correct is out

# Example code 2

counter = 1
#counting hashable objects, counter is defined as  1

while counter < 5:
  # as long as counter is less than 5 
  print("This code is inside the loop")
  # inner part of the loop, so as the counter is less than 5 is true then This code is inside the loop is printed out as a result
  counter += 1
  #counter =counter+1
  