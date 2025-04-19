import math

print("Area Calculator")

running = True

while running:
    print("")
    print("Please select which operation you would like to do using 1-5")
    triangle = print("1. Triangle")
    rectangle = print("2. Rectangle")
    square = print("3. Square")
    circle = print("4. Circle")
    quit = print("5. Quit")
    math_operation = int(input("Which operation would you like to do? (1-5): "))
    print("")

    if math_operation == 1:
        triangle_height = int(input("What is the height?: "))
        triangle_base = int(input("What is the base?: "))
        triangle_answer = (triangle_height * triangle_base / 2)
        triangle_answer_rounded = round(triangle_answer, 2)
        print("Rounded:", triangle_answer_rounded)
        print("Full:", triangle_answer)
    elif math_operation == 2:
        rectangle_length = int(input("What is the length?: "))
        rectangle_width = int(input("What is the widith?: "))
        rectangle_answer = (rectangle_length * rectangle_width)
        rectangle_answer_rounded = round(rectangle_answer, 2)
        print("Rounded:", rectangle_answer_rounded)
        print("Full:", rectangle_answer)
    elif math_operation == 3:
        square_length = int(input("What is the length?: "))
        square_answer = (square_length * square_length)
        square_answer_rounded = round(square_answer, 2)
        print("Rounded:", square_answer_rounded)
        print("Full:", square_answer)
    elif math_operation == 4: #pie r^2
        circle_radius = int(input("What is the radius of the circle?: "))
        circle_answer = (math.pi * circle_radius ** 2)
        circle_answer_rounded = round(circle_answer, 2)
        print("Rounded:", circle_answer_rounded)
        print("Full:", circle_answer)
    elif math_operation == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid option")
    again = input("Do you wish to do another operation? Y/N: ")
    if again.lower() != "y":
        running = False
    print("Thank you, have a good day!")
