def draw_square(side_length):
 
    for i in range(side_length):
        print('*' * side_length)

side_length = int(input("Enter the side length of the square: "))
draw_square(side_length)
