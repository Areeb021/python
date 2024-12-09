def sum_even_numbers(numbers):

    total = 0
    for num in numbers:
        if num % 2 == 0:  
            total += num
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,11,23,10]
print(f"The sum of the even numbers is: {sum_even_numbers(numbers)}")
