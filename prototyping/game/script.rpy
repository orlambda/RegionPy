# The script of the game goes in this file.

# Start the game

$ config.allow_skipping = True

init python:
    
    player = Being()
    # 0 ID means this is the player
    player.ID = 0
    player.location.region = "test_area"
    player.location.x = 0
    player.location.y = 0
    player.location.z = 0

# Jump to label "next" when "m" key is pressed
screen movementKepMapScreen():
    zorder 2
    key "i" action Function(movePlayerUp)
    key "j" action Function(movePlayerLeft)
    key "k" action Function(movePlayerDown)
    key "l" action Function(movePlayerRight)

screen block():
    zorder 1
    #  A modal screen prevents the user from interacting with displayables below it,
    # except for the default keymap.
    # This is evaluated once, when the game starts.
    modal True

label start:
    
    # movementTest.rpy
    jump movementTest
