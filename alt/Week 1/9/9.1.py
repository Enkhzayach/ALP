# Example Code 1

def say_hi():
#function of say_hi is defined using def 
  print("Why hello there!")
#say_hi is defined as Why hello there!

def offer_drink():
  # similarly offer_drink function is defined as below
  print("Would you care for a spot of tea?")

def offer_food():
  # offer_food function is defined as below
  print("Biscuit?")

def say_bye():
  #say_bye is defined as below
  print("Cheerio then.")


offer_drink()
#as offer_drink is defined as Would you care for a spot of tea?, it will print out defined function sentence. 
say_hi()
#Why hello there is the output of the function of say_hi as it is defined to do so 
offer_food()
# similarly offer_food() is Biscuit? its calling out the function 

# Example code 2
def maths1():
  # subroutine, function of math1 is assigned as below within the loop
  num1 = 50
  #num1 is 50
  num2 = 5
  #num2 is 5 
  return num1 + num2
  #return ends the execution of a function and sends the function's result back to the caller

def maths2():
  #subroutine, function of math2 is assigned as below
  num1 = 50
  #num1 is 50 
  num2 = 5
  #num2 is 5
  return num1 - num2
  # execution of num1- num2 is sent to the caller
def maths3():
  # subroutine, function of math3 is assigned as below within the loop
  num1 = 50
  #num1 is 50
  num2 = 5
  #num2 is 5 
  return num1 * num2
  #num1*num2 num1 multiplied by num2 is sent to the caller
outputNum = maths2()
#subroutine of math2 is defined as outputNum, im not sure if it is the proper way of explaining this line;
print(outputNum)
#as outputNum is the subroutine math2 it will be out 
# Example Code 3
def location(country):
  #argument country is inserted 
  print("I am from " + country)
  # i am from and whatever the argument you set is concencated 


location("Brazil")
#we can put any value of country in the bracket of subroutine location

