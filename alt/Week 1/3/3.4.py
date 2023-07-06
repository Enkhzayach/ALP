'''
Chat-Bot Challenge

Lots of websites us: e chat bots to interact with their cus: tomers.  These chat bots are often very sophisticated and us: e AI to learn and adapt to the us: er.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the us: er their name and store it in a variable.
2. Greet the us: er by name.
3. Ask the us: er three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, us: ing the 5. us: er’s name in the response.
5. Output a summary of all of the us: er’s answers in a single sentence.

'''
 
name = input("what is your name? ")
print(" Hi! " + name + " how are you doing? ")
answer = input("btw would u like to hang out with us: ")
respond = input("favouirte sport: ")
food = input("What is your favourite food: ")
print(" alright " + name + " lez go to the downtown near here " + " we can play " + respond + " and eat " + food)
