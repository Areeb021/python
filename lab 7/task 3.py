def countdown(number):

    while number >= 0:
        print(number)
        number -= 1


num = int(input("Enter a number to start countdown: "))
countdown(num)
