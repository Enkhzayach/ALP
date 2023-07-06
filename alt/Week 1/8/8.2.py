'''
Answer the questions

'''

# Example code:

names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  name = input("Enter the name")
  names.append(name)
elif choice == 3:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")


# What is the identifier for the list in this program?
  # Answer numbers 

# What would happen if you choose option “3” and entered index “0”? 
  # Answer option 3 is adding name so entering the index of the name is shown if we choose zero as an index it means we are choosing the first element among names 

# What would happen if you choose option “3” and entered index “7”?
  # Answer it is out of range therefore no value is out, error

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer there will be error because Stuart is not in the domain of the set of names 

# What is the purpose of int(input()) on line 10 ?
  # choice is questions are posed as in form of  integer numbers 

