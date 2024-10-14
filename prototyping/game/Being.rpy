# Python class for beings
# Used to track and change a being's location
# ID of 0 is the player

init python:

    class Being():
        # Can refactor x, y, z into a Coordinates class
        def __init__(self):
            self.ID = None
            self.location = Location()
