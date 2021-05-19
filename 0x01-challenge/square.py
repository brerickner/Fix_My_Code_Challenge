#!/usr/bin/python3
""" This is a square module """
class square():
    """ This is a square method 
    width = 0
    height = 0"""

    
    def __init__(self, *args, **kwargs):
        """ init of square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Method to get perimeter of square """
        return (self.width * 4)

    def __str__(self):
        """ str repr method"""
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
