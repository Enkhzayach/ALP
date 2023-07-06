'''
In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:
- Rename the function so that it has a sensible name. Don't forget to rename it when it is called.
- Call the function with the argument 'Sweden'.
- Get the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.
'''
def intro(country):
  #subroutine, function of my_function(country) is assigned 
  print("I am from " + country)
  # any value of parameter country will be concencatenated with I am from


intro("Sweden")
#Sweden is given for the value of country and the intro will print out I am from Sweden

country = input("where are u from?: ")
intro(country)


