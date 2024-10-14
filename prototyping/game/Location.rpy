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

        def move(self, direction):
            # target = {
            #     "x": self.x,
            #     "y": self.y,
            #     "z": self.z
            # }
            targetX = self.x
            targetY = self.y
            targetZ = self.z
            if direction == "UP":
                targetY -= 1
            elif direction == "RIGHT":
                targetX += 1       
            elif direction == "DOWN":
                targetY += 1  
            elif direction == "LEFT":
                targetX -= 1   
            elif direction == "FORWARD":
                targetZ -= 1
            elif direction == "BACK":
                targetZ += 1
            else:
                a = 5/0
            destination = f"{self.region}_{targetX}_{targetY}_{targetZ}"
            # Ensure cell exists in renpy script before updating location
            if renpy.has_label(destination):
                self.x = targetX
                self.y = targetY
                self.z = targetZ
                renpy.jump(destination)
