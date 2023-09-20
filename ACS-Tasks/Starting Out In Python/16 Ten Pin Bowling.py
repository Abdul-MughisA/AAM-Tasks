# There are 10 frames, each with 10 pins.
# A whole frame cannot exceed a total of 10.

# STRIKE:
#   Comes into action when you score 10 in 1 hit

#   MEANS
#       No second bowl (obviously)
#       Score of the next 2 frames is added onto the final total

# SPARE:
#   Comes into action when there is a total of 10 in a frame (but not in 1 hit).

#   MEANS
#       The score of the next hir (but not the frame) is added to the final total

# The final score is all the frames added together (including strike and spare).

print("This is a Ten Pin Bowling score calculator.")
hits = ["",""]
finalScore = ""
counterStrike = 0
counterSpare = 0
frame = ""

for i in range(1, 11):

    # Input score for first hit.
    hits[i,1] = input("Enter the score for hit", i + ": ")

    #Checks for strike.
    if hits[i,1] == 10:
        counterStrike =+ 3
    else:
        #Only asks for this if there is no strike.
        hits[i,2] = input("Enter the score for 2nd hit", i + ": ")

    if hits[i,1] + hits[i,2] > 10:
        print("An error has occured.")
    elif hits[i,1] + hits[i,2] == 10:
        counterSpare =+ 1

    if counterStrike > 0:
        finalScore =+ frame
        counter =- 1
    
# CALCULATE THE STRIKE AND SPARE INFORMATION IN A SEPARATE LOOP IN THE END BY QUERYING IF THE SCORES ADD UP TO 10.
