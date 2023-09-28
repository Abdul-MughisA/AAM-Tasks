# GET USER INPUT
# VALIDATE USER INPUT

# STRIKE: NEXT 2 ROLLS
# SPARE: NEXT ROLL

# CALCULATE TOTAL

# REJIG CODE TO BE IN SUBROUTINES

print("This is a Ten Pin Bowling score calculator.")
print("")
print("[STAGE 1] DATA ENTRY")
print("")
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

    # VALIDATION
    if score[i,0] > 10:
        while score[i,0] < 1 or score[i,0] > 10:
            print("Try again: ")
            score[i,0] = int(input("Enter the score on the first bowl: "))
        #end while

    elif score[i,0] < 10:
        score[i,1] = int(input("Enter the score on the second bowl: "))
        print("")
        if score[i,0] + score[i,1] == 10:
            print("Spare!")
            print("")
        #end if
    else:
        print("Strike!")
        print("")
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
        if score[(j+1),1] == 0:
            final = final + score[(j+1),0] + score[(j+2),0]

        else:
            final = final + score[(j+1),0] + score[(j+1),1]
        #end if
    #end if

    #Adds the spare.
    elif (score[j,0] + score[j,1]) == 10:
        final = final + score[(j+1),0]
    #end if

#end for

print("[STAGE 2] SCORING")
print("")
print("Well played! Your final score is:")
print(final)