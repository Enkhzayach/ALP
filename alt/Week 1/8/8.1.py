'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
 
print(Sentence)
#sentence is defined as ["Always", "look", "on", "the", "bright", "side", "of",] and each words in the square brackets are independent elements

print(Sentence[1])
#each elements in the square bracket can be out separately by defining its location from what order, sentence[1] probable means second element of the set since first element is Sentence[0]
Sentence.append("life")
#append probably means element 'life' is included in the set 
Sentence[4] = "sunny"
#sunny is added as the 4th element into the set 

print(Sentence[4])
# 'always' would be printed out.
print(Sentence[0] + " " + Sentence[3])
#from the first element to 4th elements of the sets are printed out 


print(Sentence)
#entire set with modification is printed out 