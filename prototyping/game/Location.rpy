# Python class for location

init python:

    import os
    import sys
    
    class Location:
        def __init__(self):
            self.region = None
            self.x = None
            self.y = None
            self.z = None

        def set(region, x, y, z):
            if x is not int or y is not int or (z is not int and z is not None):
                print("Error: x, y, z not valid")
                return
            self.region = region
            self.x = x
            self.y = y
            if z is not None:
                self.z = z
