def noof_digits(numbers):
    count = 0
    for digit in numbers:
        count += 1
    return count


numbers = input("Enter the number: ")
print(f"The number of digits is: {noof_digits(numbers)}")
