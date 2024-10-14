init python:
    def movePlayerUp():
        renpy.hide_screen("block")
        player.location.move("UP")    
    def movePlayerLeft():
        renpy.hide_screen("block")
        player.location.move("LEFT")
    def movePlayerDown():
        renpy.hide_screen("block")
        player.location.move("DOWN")
    def movePlayerRight():
        renpy.hide_screen("block")
        player.location.move("RIGHT")