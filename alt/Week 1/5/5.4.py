print("Y means you failed")
print()
print("N means you passed")

 
  

grade = int(input("what is you grade?: grade range is between 0 to 100: "))
# i am not sure if its a correct way of specifying the range for grade
 
if grade <= 40:
  print("U")
  print("Y-You have failed the class!")
  print("retake required")
else:
  print("you passed the class")
if 40 <= grade <= 59:
  print("grade C")
 
if 69 <= grade <= 79:
  print("grade B")
 
if grade >= 80:
  print("A")
  
 
