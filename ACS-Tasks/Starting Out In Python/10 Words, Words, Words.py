#This outputs the number of words in a sentence.
#This will be achieved by counting the number of space in the sentence and then adding 1 to it.
sentence = str(input("Type a sentence: "))
words = sentence.count(" ") + 1
print("There are", words, "words in your sentence.")