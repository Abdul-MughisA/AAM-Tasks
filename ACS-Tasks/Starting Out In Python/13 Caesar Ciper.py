#This program encodes text into a Caesar Cipher by taking in the sentence and the offset.

print("Do not enter any punctuation: ")
originalSentence = input("Enter the sentence you would like to encode: ")
print("Present your offset in the form of an integer. To offset a sentence by 1 letter, enter 1.")
offset = int(input("Enter the desired offset: "))
print("Your output will be printed in all lowercase. All punctuation will be removed.")
print()

#Converts the sentence to lowercase.
modSentence = originalSentence.lower()

#Remove all spaces from the sentence.
modSentence = modSentence.replace(" ", "")

#Check thingies for thing.