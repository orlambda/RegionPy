label dungeon_10_10:

    n "You find yourself in a stone-walled room with velvet sofas, and a disco ball."

    n "There is a hole in the ceiling and each of the four walls has a single door."
    
    menu:

        "I go..."

        "North":
            $ move_person(you, "N")
        "East":
            $ move_person(you, "E")
        "South":
            $ move_person(you, "S")
        "West":
            $ move_person(you, "W") 
        "Through the hole":
            jump wizard

label dungeon_10_11:

    if player_has_item == False:

        n "This room is huge and black. The only visible wall is the one behind you."
        
        n "In this room are two tables conveniently lit with spotlights. On the left table, there is an orange. On the right table, there is a pink wig."

        menu:

            "Pick up..."

            "The orange.":
                $ player_item = "orange"
                $ player_has_item = True

                n "You pick up the orange. It is firm and fresh."

            "The pink wig.":
                $ player_item = "wig"
                $ player_has_item = True

                n "You pick up the wig. It is fabulous."

            "Nothing.":

                n "Sure. No need to take an item back to the wizard."

                n "We could always just live here forever..."

    elif player_item == "orange":

        n "In this room are two tables. On the right table, there is a pink wig. There is nothing on the left table."

        n "You are a very decisive person and do not consider for one moment picking up the other item."

        n "The programmer definitely wrote that functionality, but it just doesn't appeal to you."

    elif player_item == "wig":

        n "In this room are two tables. On the left table, there is an orange. On the right table, there are a few pink strands of hair."

        n "You are a very decisive person and do not consider for one moment picking up the other item."

        n "The programmer definitely wrote that functionality, but it just doesn't appeal to you."

    n "There is a door to the South."
    
    jump nav    
