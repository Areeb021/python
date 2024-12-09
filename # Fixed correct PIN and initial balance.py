# Fixed correct PIN and initial balance
correct_pin = "1234"
balance = 1000

# Ask the user to enter their PIN
entered_pin = input("Enter your PIN: ")

# Check if the entered PIN is correct
if entered_pin == correct_pin:
    print("\nPIN accepted.")
    print("Welcome to the ATM")

    # Display the menu options
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Withdraw Money")

    # Get user's choice
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        # Option to check balance
        print("\nYour current balance is:", balance)

    elif choice == "2":
        # Option to withdraw money
        withdrawal_amount = float(input("Enter amount to withdraw: "))

        if withdrawal_amount <= balance:
            # Deduct the amount from the balance
            balance -= withdrawal_amount
            print("\nWithdrawal successful.")
            print("Your new balance is:", balance)
        else:
            # Insufficient balance
            print("\nInsufficient balance.")
    else:
        print("\nInvalid option selected.")

else:
    # Incorrect PIN entered
    print("Incorrect PIN. Access denied.")
