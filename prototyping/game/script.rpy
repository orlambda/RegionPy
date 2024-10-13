# The script of the game goes in this file.

# Start the game


init python:

    def jumpToNext():
        renpy.jump("next")

# Jump to label "next" when "m" key is pressed
screen keymapscreen():
    zorder -1
    key "m" action Function(jumpToNext)

label start:

    show screen keymapscreen

    "Hiya!"

label start01:

    "Hiya again!"

label start02:

    "And hiya again!"

label next:

    "It worked! You are at the label called next"

    return
