# The script of the game goes in this file.

# Start the game


init python:

    def jumpToNext():
        renpy.hide_screen("block")
        renpy.jump("next")


    player = Being()
    player.location.region = "test_area"
    player.location.x = 0
    player.location.y = 0
    player.location.z = 0

# Jump to label "next" when "m" key is pressed
screen keymapscreen():
    zorder -1
    key "m" action Function(jumpToNext)
    key "i" action Function(movePlayerUp)
    key "j" action Function(movePlayerLeft)
    key "k" action Function(movePlayerDown)
    key "l" action Function(movePlayerRight)

screen block():
    zorder -2
    modal True

label start:

    show screen keymapscreen

    show screen block
    
    "Press M when ready to enter test_area!"

label next:

    "Ok here we go!"

    jump test_area_0_0_0

    return
