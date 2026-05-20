
label start:

    # Hide the quick menu.
    $ quick_menu = False

    menu:

        "What to do?"

        "Start the game.":

            pass

        "Test Griswyr sprites.":

            jump griswyr_test

    stop music fadeout 1.0

    pause 1.2

    stop music

    jump prologue

    return


label griswyr_test:

    gr neutral "Dialogue"
    
    gr smirk "Dialogue"
    
    gr angry "Dialogue"
    
    gri neutral "Dialogue"
    
    gri smirk "Dialogue"
    
    gri angry "Dialogue"

    show buzz happy at buzz_normal_range:
        center

    bu "Hiii!!!"

    show buzz shocked at buzz_close_range:
        center 

    bu "You ugly..."

    show buzz happy at buzz_normal_range:
        left 

    bu "Lalalalala!!!"

    show buzz shocked at buzz_close_range:
        right

    bu "Aiiiiieeee!!!"

    show buzz shocked at buzz_close_range:
        left

    bu "ugly...."

    show buzz happy at buzz_normal_range:
        right

    bu "DONATE MONEY, UGLY!!!" with vpunch
    
    return