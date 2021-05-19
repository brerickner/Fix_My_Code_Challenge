#!/usr/bin/python3
""" This is a square module """


class Square():
    """ This is a square method """

    width = 0
    height = 0


    def __init__(self, width, height):
        """ init of square """
        self.height = height
        self.width = width
            

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Method to get perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ str repr method"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
