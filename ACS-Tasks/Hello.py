import time

# Declares variables.
loop = True
names = [""]

def displayMenu():
    valid = False
    print("")
    print("[MENU]")
    print("[1] Add Name")
    print("[2] Display List")
    print("[3] Quit")
    print("")

    while valid == False:
        selection = int(input("Enter a valid number: "))

        if selection >=3 and selection <=1:
            valid = False
        elif selection <= 3 and selection >=1:
            valid = True
        #end if
    #end while

    return selection
#end def

while loop == True:
    choice = displayMenu()
    
    if choice == 1:
        position = int(input("Enter the position in the list to insert the name: "))
        name = input("Enter the name: ")
        names[(position - 1)] = name
    #end if

    if choice == 2:
        print("The names in order are:")
        print(names)

    if choice == 3:
        print("The program will now terminate.")
        time.sleep(2)
        loop = False
#end while

print(...)
print("The program has now been terminated.")