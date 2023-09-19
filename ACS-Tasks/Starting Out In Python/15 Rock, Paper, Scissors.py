import random
import time

#This task plays rock, paper, scissors with the user.

playerInput = input("Enter R, P or S for Rock, Paper or Scissors: ")
print("Thinking...")
time.sleep(3)
computer = random.randint(1,3)

if computer == 1:
    computer = "R"
elif computer == 2:
    computer = "P"
elif computer == 3:
    computer = "S"
else:
    print("An error occurred with this input.")
#end if

print("The computer got", computer + " and is now determining the outcome.")
time.sleep(3)

if computer == playerInput:
    print("You drew! The computer also got", playerInput + ".")
elif computer == "R" and playerInput == "S":
    print("The computer won! A rock destroys scissors.")
elif computer == "S" and playerInput == "R":
    print("You won! A rock destroys scissors.")
elif computer == "R" and playerInput == "P":
    print("You won! The paper envelops the rock.")
elif computer == "P" and playerInput == "R":
    print("The computer won! The paper envelops the rock.")
elif computer == "P" and playerInput == "S":
    print("You won! Scissors cut paper.")
elif computer == "S" and playerInput == "P":
    print("The computer won! Scissors cut paper.")
else:
    print("Some error has occured with your inputs. Run the program again.")