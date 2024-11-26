# Python class for units
# Used to track and change a unit's location
# ID of 0 is the player

init python:

    class Unit():
        # Can refactor x, y, z into a Coordinates class
        def __init__(self):
            self.ID = None
            self.location = Location()
            self.direction = None

        def move(self, direction):
            # TODO: refactor
                # self.location to target.
                # process target and direction in a separate function.
                # copy target to self.location
            targetX = self.location.x
            targetY = self.location.y
            targetZ = self.location.z
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
            elif direction != "SAME":
                raise Exception("Invalid direction for Unit.move()")
            destination = f"{self.location.region}_{targetX}_{targetY}_{targetZ}"
            # Ensure cell exists in renpy script before updating location
            if renpy.has_label(destination):
                self.location.x = targetX
                self.location.y = targetY
                self.location.z = targetZ
                if self.ID is 0:
                    renpy.scene()
                    cellBackground = f"{self.location.region}_{self.location.x}_{self.location.y}_{self.location.z}".lower()
                    renpy.show(cellBackground)
                    renpy.jump(destination)

