try:
    width = float(input("enter rectangle width"))
    length = float(input("enter the rectangle length"))

    if width == length:
        exit("that looks like a square")
    area = length*width
    print(area)
except ValueError:
    print("Please enter a number")