MAX = 10
name_array = [" " for _ in range(MAX)] # Array creation
found = False
index = 0
name_array[0] = "Bob"
name_array[1] = "Fred"
name_array[2] = "Barry"
name_array[3] = "Felix"

request = input("Enter the name you wish to search for: ")

for i in range(MAX):
    if name_array[index] == request and index < MAX:
        print("Student record is in " + str(index + 1) + ".")
        found = True
    index += 1
    if index == MAX:
        print("Student record was not found. Try again.")