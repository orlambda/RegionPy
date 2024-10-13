label beach_8_9:

    n "The dark sea ahead beckons you."

    menu:

        "You..."

        "Swim ahead into the darkness":
            jump beach_8_9_sea

        "Resist the pull of the sea and try to swim to shore":
            jump beach_8_9_shore

    label beach_8_9_sea:

        n "You feel welcomed by the water ahead of you, your energy slowly restoring as you continue ahead."

        n "The warmth of the sea puts you at ease. The beach is nowhere in sight - you belong to the water now."
        
        p "This is where I should be going. Where else is there to go."

        n "You descend, into the comfort of the darknes."   
        
        jump end

    label beach_8_9_shore:

        n "You muster all your physical and mental strength and set your eyes on the beach."
        
        n "Your legs can barely push against the weight of the water and you try to use each wave to get closer."
        
        n "It's hard to tell if the tide is helping you or pulling you further out."

        p "I can make it."

        p "I'll never make it."

        p "I can make it."

        p "I..."

        jump end

label beach_8_10:

    n "There is a beauty in the perfect straightness of the beach that lies ahead of you."

    n "To the left, the unchanging abyss of the sea. To the right, a mess of tangled growth and boulders."

    n "Ahead of you, a path of soft sand. Safety, clarity, direction."

    n "You are compelled to run, to experience the full length of this beach, to forget the chaos and unknown on either side."

    p "Nothing else."

    p "Onwards."

    n "You run."

    jump end

label beach_9_8:
    
    jump sea_death

label beach_9_9:

    n "The water is comfortably warm here, and shallow enough to stand or swim as you please."

    n "The beach lies to the North, extending as far as you can see to the West, and cut off by rocks to the East."

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

label sea_death:

    n "You swim with courage, sure that wherever you should be heading lies ahead"

    n "You look to see how far you've swum from the beach - it is nowhere to be seen. With no clue what direction you're now facing, you swim on."

    n "Nothing changes until you notice a coldness in your legs."

    n "Any direction must lead to land eventually, you hope."

    n "Your legs have no energy left to swim, and dangle beneath you helplessly."

    n "Your arms keep you afloat, paddling with just enough power to move you slowly forwards."

    p "If I can keep going just a little longer..."

    jump end

label beach_9_10:

    n "Here, the sand is cold and damp."
    
    n "The sea lies to the South. To the North, the beach disappears into blackness, and to the East, a rocky formation lies in the distance."
    
    n "You feel utter serenity as you look to the West, where the beach extends for an eternity."

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

label beach_9_11:

    n "You are enveloped in darkness and feel you may be standing on the edge of reality."

    n "Only the faint light from the beach to the South gives you an idea of your bearings."

    menu:

        "I walk..."

        "North":
            $ move_person(you, "N")

        "East":

            $ move_person(you, "E")
        "South":

            $ move_person(you, "S")
        "West":

            $ move_person(you, "W")   

label beach_10_8:
    
    jump sea_death

label beach_10_9:

    n "The sea is tranquil, and you feel only the gentlest of waves against your waist."

    n "The beach lies to the North, disappearing into the West, and cut off by large boulders to the East."

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

label beach_10_10:

    n "The sea lies to the South. The sandy beach stretches out to the West, with small shrubs growing to the North. You are close to the Eastern end of the beach, which is interrupted by large boulders."

    jump nav

label beach_10_11:

    n "The ground here is pebbly, making it hard to walk."

    n "Creatures crawl within the shrubbery."

    n "A ruined stone wall leads North to South. Darkness to the West, and through a gap in the wall to the East, a glimpse of some greenery."

    jump nav

label beach_10_12:

    n "You see a light, and it takes you a moment to readjust your eyes."

    n "You make out a cloaked figure and approach."

    jump wizard_first_meeting

label beach_11_8:
    
    jump sea_death    

label beach_11_9:

    p "As you stand in the water, strands of seaweed stick to your body."

    p "The sea is met by a large formation of boulders to the North, which descends into a sandy beach to the West."

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

label beach_11_10:

    n "The beach is blocked by large boulders that shine under the moon."

    n "That's nice."

    jump nav

label beach_11_11:

    n "You feel threatened by trees and monkeys."

    menu:

        "I walk..."

        "North":
            $ move_person(you, "N")

        "East":

            $ move_person(you, "E")
        "South":

            $ move_person(you, "S")
        "West":

            $ move_person(you, "W")

label beach_11_12:

    n "The woods are thick, and branches scratch against you as you move."

    menu:

        "I walk..."

        "North":
            $ move_person(you, "N")

        "East":

            $ move_person(you, "E")
        "South":

            $ move_person(you, "S")
        "West":

            $ move_person(you, "W")

label beach_11_13:
    
    n "Your movement is severely restricted by the growth around you."

    n "As you to try to break away from the vines and thorns, they only constrict you further."

    n "You take a few minutes to breath and think of a plan."

    n "There is nothing else to do, you will have to endure the pain as you try to break free."

    n "You slowly slide your arms upwards, hoping to use them to rip away the vines from the rest of your body."

    n "Spikes pierce your skin, and you realise how much blood you have lost already."

    n "You ignore the pain as you struggle, leaving skin and lumps of flesh hanging from the plants around you."

    n "Unable to endure the agony, you go into a frenzy, ripping away faster and faster. Anything but stopping to feel the pain."

    n "Your limbs stop responding as your muscles are torn beyond function."
    
    n "All that's left is for you to manically attack the vines with your teeth, until even your neck won't move any longer."

    n "You are left hanging, your eyes pierced and your torso left hanging from your suspended head."

    n "The pain is all you know."

    p "ow :("
    
    jump end

label beach_12_9:

    n "You lose your footing."

    n "Before you can even gain composure, you are pulled underwater by a huge force. You feel yourself spinning."

    n "All attempts to resist the whirlpool are futile. You feel so weak you can't even feel your body trying to break free as you struggle."
    
    n "In minutes you run of breath, and cannot help but gulp down the water that surrounds you."

    n "A building pressure in your head, then darkness."

    jump end

label beach_12_10:

    n "You descend into a crawl as the shiny, black boulders make the path hazardous."

    python:
        if player_has_map == True:
            renpy.jump("beach_12_10_2")
        else:
            renpy.jump("beach_12_10_1")

label beach_12_10_1:

    menu:
        
        "You see a sheet of paper lodged between two boulders."

        "Take it.":
            $ player_has_map = True
            n "You inspect the paper. It looks like a map. (Press 'm' to view)"
            jump beach_12_10_2

        "Leave it.":
            jump beach_12_10_2

label beach_12_10_2:

    n "Perilous gaps lie between the boulders."

    n "Thick foliage lies to the North, and the rocks descend to a sandy beach in the West. To the Southeast, blackness and the sound of the sea."

    jump nav

label beach_12_11:

    n "Monkeys surround you. They might have noticed you."

    n "One of them pokes you in the face."

    p "Ow."

    n "The woods around you are thick, but thin out to the South. To the East, bananas and howling."

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

label beach_13_11:

    n "A particularly tall monkey emerges from the crowd."

    p "Wow. So tall."

    n "The monkey eats a banana, and you watch, hungrily. You remember that bananas are a good source of energy."

    n "The monkey eats another banana, and you continue to watch. You remember that bananas are high in potassium."

    n "The monkey eats a third banana, and you watch, wondering how many bananas this monkey eats per day."

    n "You wonder how many monkeys are here, and what their total banana consumption must be per year."

    n "You remember that a fungal banana crisis is imminent and wonder whether these bananas are the same variety as those commonly found in stores."

    n "You monkey whacks you in the head."

    jump end