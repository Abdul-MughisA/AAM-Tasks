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

#Uses a for loop with range as long as the length of the sentence to add the offset to each character to shift it.
#If adding the offset makes the ASCII go past the letter z, then just subtract 26 from the ASCII code.
for change in range(0, len(modSentence)):
    print(modSentence[0])
#end for