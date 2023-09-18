#This task simply reverses the input.

sentence = input("Enter an input to be reversed: ")
newSentence = ""

#Counts a for loop from the length of the sentence down to -1 (because for loops are not inclusive) with step -1.
#With each step down, the newSentence variable has the letter appended.
#So that as the for loop continues, the reverse letter continues to be appended to the newSentence.
#And at the end, then, newSentence will hold the whole reversed sentence.
for i in range(len(sentence)-1, -1, -1):
    newSentence = newSentence + sentence[i]
#end for

#Outputs the reverse in a user-friendly format.
print("Reverse:")
print(newSentence)