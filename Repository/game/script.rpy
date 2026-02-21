
label start:

    menu:

        "What to do?"

        "Start the game.":

            pass

        "Test sprite positioning.":

            jump sprite_positioning

    stop music fadeout 1.0

    pause 1.2

    stop music

    jump prologue

    return



label sprite_positioning:

    window hide

    show nick neutral at center, nick_normal_range

    pause

    show nick elated at center, nick_close_range
    
    pause

    show nick happy
    
    pause

    hide nick

    ############################################

    ############################################
    
    show celestial at center, celestial_normal_range

    pause

    show celestial combat at center, celestial_normal_range

    pause

    show celestial at center, celestial_close_range

    pause

    show celestial combat at center, celestial_close_range

    pause

    window show

    show celestial at center, celestial_far_range

    pause

    show celestial combat at center, celestial_far_range

    pause

    ############################################
    

    return


