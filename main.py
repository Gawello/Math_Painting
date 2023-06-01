from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "greem": (0, 255, 0), "blue": (0, 0, 255)}
canvas_color = input("Enter canvas color \n Your options:\n white, black, red, green, blue \n")

# Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

# Endless loop for the user, but only 1 rectangle and 1 square can be drawn
while True:
    shape_type = input("What shape do you like to draw (rectangle or square)? Enter quit to finish canvas..")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        print("Configuration of coordinates")
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        print("Size of your rectangle")
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        print("Now, color configuration in RGB values")
        red = int(input("How much RED should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        print("Configuration of coordinates")
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        print("Size of your Square")
        sqr_size = int(input("Enter size of your square (length of one side): "))
        print("Now, color configuration in RGB values")
        red = int(input("How much RED should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create a square
        q1 = Square(x=sqr_x, y=sqr_y, side=sqr_size, color=(red, green, blue))
        q1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make('canvas.png')


# OLD TEST
# canvas = Canvas(height=20, width=30, color=(255, 255, 255))
# r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
# r1.draw(canvas)
# s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
# s1.draw(canvas)
# canvas.make('canvas.png')
