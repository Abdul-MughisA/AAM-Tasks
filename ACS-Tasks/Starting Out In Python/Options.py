#This program asks the user to select an option and keeps prompting the user until a valid option has been selected.
print("OPTIONS")
print("[1] Option 1")
print("[2] Option 2")
print("[3] Option 3")
print()
while True:
    ans = int(input("Select an option: "))
    print("You have selected option", str(ans) + ".")
    if ans >= 1 and ans <= 3:
        break
#end while