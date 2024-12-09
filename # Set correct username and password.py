# Set correct username and password
correct_username = "admin"
correct_password = 12345

# Ask the user for their username and password
username = input("Enter your username: ")
password = int(input("Enter your password: "))

# Check if the username and password are correct
if username == correct_username and password == correct_password:
    print("Login Successful!")
elif username != correct_username:
    print("Incorrect username")
elif password != correct_password:
    print("Incorrect password")
