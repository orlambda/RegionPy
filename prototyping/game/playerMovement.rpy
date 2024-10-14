init python:
    def movePlayerUp():
        if canMove:
            renpy.hide_screen("block")
            player.move("UP")    
    def movePlayerLeft():
        if canMove:
            renpy.hide_screen("block")
            player.move("LEFT")
    def movePlayerDown():
        if canMove:
            renpy.hide_screen("block")
            player.move("DOWN")
    def movePlayerRight():
        if canMove:
            renpy.hide_screen("block")
            player.move("RIGHT")