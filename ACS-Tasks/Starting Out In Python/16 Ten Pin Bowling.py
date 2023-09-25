# There are 10 frames, each with 10 pins.
# A whole frame cannot exceed a total of 10.

# STRIKE:
#   Comes into action when you score 10 in 1 hit

#   MEANS
#       No second bowl (obviously)
#       Score of the next 2 rolls is added onto the final total

# SPARE:
#   Comes into action when there is a total of 10 in a frame (but not in 1 hit).

#   MEANS
#       The score of the next roll is added to the final total

# The final score is all the frames added together (including strike and spare).

print("This is a Ten Pin Bowling score calculator.")
score = {}
final = 0
spare1 = 0
spare2 = 0

# Sets all values to 0 to prevent out-of-range error.
for a in range(0,12):
    score[a,0] = 0

    for b in range(0,2):
        score[a,b] = 0
    #end for
#end for

# Asks user for inputs (working correctly).
for i in range(0,10):
    score[i,0] = int(input("Enter the score on the first bowl: "))

    if score[i,0] < 10:
        score[i,1] = int(input("Enter the score on the second bowl: "))
        if score[i,0] + score[i,1] == 10:
            print("Spare!")
        #end if
    else:
        print("Strike!")
    #end if
#end for

if score[9,0] == 10:
    spare1 = int(input("Enter the score on the spare bowl: "))
    score[10,0] = spare1
    spare2 = int(input("Enter the score on the spare bowl: "))
    score[11,0] = spare2
elif score[9,0] + score[9,1] == 10:
    spare1 = int(input("Enter the score on the spare bowl: "))
    score[10,0] = spare1
#end if

for j in range(0,10):
    final = final + score[j,0] + score[j,1]

    # Adds the strike.
    if score[j,0] == 10:
        final = final + score[(j+1),0] + score[(j+2),0]

    #Adds the spare.
    elif (score[j,0] + score[j,1]) == 10:
        final = final + score[(j+1),0]
    #end if

#end for

print(final)