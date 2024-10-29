label test_area_0_0_0:
    # $ canMove = False
    # $ config.allow_skipping = True
    $ preventPlayerMovement()
    "0 0 0 cannot move yet!"
    "This text should be skippable"
    "Skip skip skip!"
    "Skippy skip skip skip..."
    "And that ends the skipping!"
    $ allowPlayerMovement()
    menu:
        "MOVE 0 0 0"
        "":
            ""
label nergrego23224:
    "ERROR!got here from 0 0 0 "
label test_area_1_0_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    # show screen block
    # $ config.allow_skipping = False
    "1 0 0"
    menu:
        "MOVE 1 0 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no232ggg24:
    "ERROR!got here from 1 0 0"
label test_area_2_0_0:
    $ preventPlayerMovement()
    # $ canMove = False
    # $ config.allow_skipping = True
    "2 0 0 cannot move yet! Can skip text!"
    "1 sec!"
    # show screen block
    # $ canMove = True
    # $ config.allow_skipping = False
    $ allowPlayerMovement()
    menu:
        "MOVE 2 0 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no23rffrff224:
    $ "ERROR!got here from 2 0 0 "
label test_area_0_1_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    menu:
        "MOVE 0 1 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no2322mn4:
    $ "ERROR!got here from 0 1 0 "
label test_area_1_1_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    "1 1 0"
    menu:
        "MOVE 1 1 0"
        "":
            ""
    $ renpy.pause(hard = True)
label no2g3224:
    $ "ERROR!got here from 1 1 0 "
label test_area_2_1_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    menu:
        "MOVE 2 1 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no23224:
    "ERROR!got here from 2 1 0 "
label test_area_0_2_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    menu:
        "MOVE 0 2 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no2334:
    "ERROR!got here from 0 2 0 "
label test_area_1_2_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    menu:
        "MOVE 1 2 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no234:
    "ERROR!got here from 1 2 0 "
label test_area_2_2_0:
    $ preventPlayerMovement()
    $ allowPlayerMovement()
    menu:
        "MOVE 2 2 0 "
        "":
            ""
    $ renpy.pause(hard = True)
label no:
    "ERROR! got here from 2 2 0"