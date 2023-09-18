#This task simply reverses the input.

sentence = input("Enter an input: ")
for i in range(0, len(sentence)):
    front = sentence[i]
    back = sentence[len(sentence)-i]
    sentence[i] = back
    sentence[len(sentence)-i] = front
#end for
print(sentence)