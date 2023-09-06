#This program prompts the user to enter a password and notifies the user whether the password is valid for use.
password = input("Enter a password: ")
if len(password) > 6:
    print("Excellent. This password is valid.")
else:
    print("This password is invalid.")
#endif
