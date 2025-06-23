# Ask the user for a password and check if it matches the saved password.
# If it matches, print a success message; otherwise, print an error message.
saved_password = "secret123"
user_password = input("Enter your password: ")
if user_password == saved_password:
    print("Access Granted")
else:
    print("Access Denied")
# Check the length of the password and print a message accordingly.
if len(user_password) < 8:
    print("Password is too short, it must be at least 8 characters long.")
elif len(user_password) > 16:
    print("Password is too long, it must be no more than 16 characters long.")
else:
    print("Password length is good.")
# Check if the password is only numeric or contains letters nor special characters and message accordingly.
if user_password.isnumeric():
    print("Password is numeric only.")
elif user_password.isalpha():
    print("Password contains letters only.")
else:
    print("Password contains both letters and numbers or special characters.")
# Alert message if the user enters the wrong password more than two times.
attempts = 0
while attempts < 2:
    user_password = input("Enter your password: ")
    if user_password == saved_password:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Access Denied")
        if attempts == 2:
            print("You’ve been signed out after too many failed login attempts. please try again later.")
            break
# Check If the password does not contain any digits, print "Error: Need a digit."
if not any(char.isdigit() for char in user_password):
    print("Error: Need a digit.")
# Check If the password contains at least one digit but is still incorrect, print "Access denied."
if any(char.isdigit() for char in user_password) and user_password != saved_password:
    print("Access denied.")
