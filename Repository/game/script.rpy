
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
    
    return