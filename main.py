import numpy as np
from PIL import Image


class Canvas:
    """
    Object where all shapes are going to be drawn
    """

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, image_path):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


class Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draws itself into the Canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color


class Square:

    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def draw(self, canvas):
        pass
