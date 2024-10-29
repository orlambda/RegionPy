init python:

    playerCanMove = False
    
    def allowPlayerMovement():
        # if not renpy.get_screen("block"):
        #     renpy.show_screen("block")
        global playerCanMove
        playerCanMove = True
        config.allow_skipping = False         
        
    def preventPlayerMovement():
        global playerCanMove
        if playerCanMove:
            playerCanMove = False
            renpy.hide_screen("block")
            config.allow_skipping = True


    def movePlayerUp():
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