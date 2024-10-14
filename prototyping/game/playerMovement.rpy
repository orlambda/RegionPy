init 1 python:
    def allowPlayerMovement():
        global playerCanMove
        config.allow_skipping = False
        playerCanMove = True
        if not playerCanMove:            
            renpy.show_screen("block")


    def preventPlayerMovement():
        global playerCanMove
        if playerCanMove:
            playerCanMove = False
            renpy.hide_screen("block")
            config.allow_skipping = True


    def movePlayerUp():
        global playerCanMove
        if playerCanMove:
            renpy.hide_screen("block")
            player.move("UP")    
    def movePlayerLeft():
        if playerCanMove:
            renpy.hide_screen("block")
            player.move("LEFT")
    def movePlayerDown():
        if playerCanMove:
            renpy.hide_screen("block")
            player.move("DOWN")
    def movePlayerRight():
        if playerCanMove:
            renpy.hide_screen("block")
            player.move("RIGHT")