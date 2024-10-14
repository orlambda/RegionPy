# Jump to the debugging label and control other program behaviour
define debugging = False

# To detect errors saving/assigning player name
default pname = "Missing_name"
default psurname = "Missing_name"

# Avoid quick flashing of presplash screen
define config.minimum_presplash_time = 0.5
# Disable scrolling back using mouse wheel as allows quick undo of player decisions
define config.rollback_enabled = False
# Disable skipping through dialogue using tab or ctrl key (or quick menu)
define config.allow_skipping = False

# Player has to find map
default player_has_map = False
default allow_map_view = True

# Player has to find item
default player_has_item = False
default player_item = ""

# Splashscreen (not presplash/loading - before start)
image splash = "splash.png"
label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

# Skip past main_menu
label main_menu:
    return
# Skip past game menu
label game_menu:
    return

# Customized keyboard input (for function, add arguments as an argument e.g. Function(toggle_map, arg1="maybe a string") )
screen keymapscreen():
    zorder 10
    key "m" action Function(toggle_map)

label map_label:
    # use call instead of show if using modal True in screen map
    show screen map
    $ renpy.pause(hard=True)
    # wait4ui ""
    # q "efwfwef wefwe fwef wefwefwef"
    return(True)

screen map():
    # show "images/map.png" (image fills screen)
    # modal True
    zorder 99
    frame:
        background "map.png"
    # Note: hides map screen if mouse was clicked before map screen 
    key ["m", "mouseup_1"] action Return()

# First label
label start:
    # Allow "m" key input
    show screen keymapscreen

    $ you = Person(0, "Your name")

    # The player's name
    define p = Character("[pname]")
    # The player's thoughts (no name displayed)
    define i = Character("", what_italic = True, what_xalign=0.5)
    # The narrator
    define n = Character("", what_xalign=0.5)

    # Give player a name before jumping to debug label
    if debugging:
        
        "Hi - you are debugging"

        $ pname = "Debugging"
        
        p "My name is [pname]!"
        
        jump debugging

    jump character_creation

label character_creation:

    scene bg black

    i "Where..."

    n "You feel a cool breeze."

    n "Sand, wet... seaweed on your toes?"

    python:
        pname = renpy.input("You try and recall your first name...", length=20)
        pname = pname.strip()
            
    $ you.name = pname
    p "That's right! My name is [you.name]!"    

    jump island_start

label island_start:

    # Sets the scene as the player gains orientation.

    p "How did I get here?..."

    n "Your eyes start to adjust to the darkness and you see some movement ahead of you."

    n "Trees. Leaves brushing against a rocky surface."

    n "An expanse of blackness. Water."
    
    n "You spend a moment to enjoy the calmness of the beach."

    n "That's nice."    

    n "You get your bearings."
    
    jump beach


label beach:

    # Jump to initial coordinates
    jump beach_10_10

label wizard_first_meeting:

    scene bg grey
    
    # Meet the wizard for the first time
    "Wizard" "HELLO I AM A WIZARD!"

    "Wizard" "I'M HAVING SUCH A DIFFICULT DAY"

    menu:

        "Wizard" "I'M HAVING SUCH A DIFFICULT DAY"

        "I'm sorry to hear that. Want to talk about it?":
            
            "Wizard" "WOW! I'D LOVE TO!"

            "Wizard" "Well, it all started last week."

            "Wizard" "I bought some cheese at the shop, but it was out of date."
            
            "Wizard" "And it was the only cheese they had!"
            
            "Wizard" "In fact, it was the only anything they had."
            
            "Wizard" "In fact it wasn't a shop, it was a monkey."

            "Wizard" "But yes, I ate it, because people say cheese is just mould anyway, so I thought it's probably fine, AND NOW MY MOUTH TASTES ALL FIZZY AND MOULDY AND NOTHING WILL MAKE IT GO AWAY!"

            "Wizard" "I just need something to distract me. At least until the taste fades away."

            "Wizard" "I've heard there are some nice things in this dungeon, and it's a sort of help-yourself type dealio."

            "Wizard" "Just a normal, lovely, community dungeon, with lovely things in it that anyone can take for free and without negative consequences."

            "Wizard" "BUT I'M TOO BIG! I CAN'T GET THROUGH THE HOLE!!"

            "Wizard" "So..."

            "Wizard" "Perhaps you would enter the aforementioned community dungeon in my place, procure some serotonin-boosting goodies, return with haste, and pass them into my possession?"
            
            i "Seriously, this guy."
    
            p "Ugggh."

            p "Reeaaaally?"

            "Wizard" "yes uwu"

            p "okee np bestie xx"

            jump dungeon_entrance

        "Oh god. Here we go.":

            "Wizard" "DON'T WORRY. I WON'T BORE YOU WITH IT."

            p "Oh thank god."

            "Wizard" "JUST POP INTO THAT DUNGEON AND BRING ME BACK SOMETHING NICE TO CHEER ME UP."

            "Wizard" "THEN I WON'T HAVE TO KILL YOU!"
            
            n "You recall that wizards are not to be messed with."

            p "No need to be making threats, my friend! Say no more, of course I'll help you."

            p "Everyone deserves a lil' treat."

            p "Self-care is so important."

            n "You realise tears are dripping down your cheeks. Your attempts to hide your fear may have failed."

            i "Great, now I don't stand a chance at romancing the wizard..."

            i "Better check out this dungeon."

label dungeon_entrance:

    n "This \"entrance\" to the dungeon is a small hole at the foot of the ruined wall. You can just about fit through."

    n "You enter the dungeon."

    scene bg black

    n "It's surprisingly warm."
    
    # Jump to initial coordinates
    $ you.x = 10
    $ you.y = 10
    $ you.area = "dungeon"
    jump dungeon_10_10

label wizard:
    # Meet the wizard again

    scene bg grey
    
    if player_has_item == False:
        "Wizard" "WHERE IS MY TREAT?"

        "Wizard" "TIME TO DIE!"

    elif player_item == "orange":
        
        "Wizard" "Wow."

        "Wizard" "It's beautiful!!!"

        "Wizard" "I don't know what to say."

        "Wizard" "Thank you."

        "Wizard" "Anyway, where you headed?"
        
        n "The wizard pulls out a super fancy car from his pocket."
        
        n "There are flames painted on the doors, it's soo cringe"

        n "But also you can't remember ever seeing car before, because you are a zombie and you don't have brains to speak of, so you're kinda amazed."

        "Wizard" "Pop in, I'll give you a lift."

        n "Fancy music plays"

        jump end

    elif player_item == "wig":

        "Wizard" "OOOOOOOOO"

        "Wizard" "How FAAAANCY!"

        n "The wizard puts on the wig under his cloak."

        "Wizard" "Look at meeeee"

        n "You look at him"

        "Wizard" "Oh yeaaaah"

        "Wizard" "I say, let's go to the club!"

        n "You go to the club. It is fun."

        n "You won the game btw."

    else:

        "Wizard" "What is THAT???"

        "Wizard" "OOO you must have broken the game. I don't recognise that item!"

        "Wizard" "Please report this to the programmer. And consider this the best ending in return for your trouble!"

        "Wizard" "WOOOO!"

        n "You both do the debug dance."

    jump end

# NESW error - end game
label pit:
    n "You fall into a pit."
    jump end

# Where we start when debugging - change this as necessary
label debugging:

    "Jumping to island_start"

    jump island_start

label nav:

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

label end:
    scene bg black
    with dissolve
    $ renpy.pause(delay=3, hard=True)
    scene bg playagain
    pause
    scene bg black
    with dissolve
    $ renpy.pause(delay=0.5, hard=True)

    return