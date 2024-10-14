label test_area_0_0_0:


    $ canMove = False

    $ config.allow_skipping = True

    "0 0 0 cannot move yet!"

    "This text should be skippable"

    "Skip skip skip!"

    "Skippy skip skip skip..."

    $ canMove = True

    show screen block

    $ config.allow_skipping = False

    "And that ends the skipping! Can move now"


label test_area_1_0_0:

    show screen block

    $ config.allow_skipping = False

    "1 0 0"

label test_area_2_0_0:

    $ canMove = False

    $ config.allow_skipping = True

    "2 0 0 cannot move yet! Can skip text!"

    "1 sec!"

    show screen block

    $ canMove = True

    $ config.allow_skipping = False

    "2 0 0 can move now"



label test_area_0_1_0:

    show screen block

    $ config.allow_skipping = False

    "0 1 0 "



label test_area_1_1_0:

    show screen block

    $ config.allow_skipping = False

    "1 1 0"



label test_area_2_1_0:

    show screen block

    $ config.allow_skipping = False

    "2 1 0"



label test_area_0_2_0:

    show screen block

    $ config.allow_skipping = False

    "0 2 0 "



label test_area_1_2_0:

    show screen block

    $ config.allow_skipping = False

    "1 2 0"



label test_area_2_2_0:

    show screen block

    $ config.allow_skipping = False

    "2 2 0"



label test_area_0_0_1:

    show screen block

    $ config.allow_skipping = False

    "0 0 1"



label test_area_1_0_1:

    show screen block

    $ config.allow_skipping = False

    "1 0 1"



label test_area_2_0_1:

    show screen block

    $ config.allow_skipping = False

    "2 0 1"



label test_area_0_1_1:

    show screen block

    $ config.allow_skipping = False

    "0 1 1 "



label test_area_1_1_1:

    show screen block

    $ config.allow_skipping = False

    "1 1 1 "



label test_area_2_1_1:

    show screen block

    $ config.allow_skipping = False

    "2 1 1"


label test_area_0_2_1:
    show screen block

    $ config.allow_skipping = False
    "0 2 1"


label test_area_1_2_1:
    show screen block

    $ config.allow_skipping = False
    "1 2 1"



