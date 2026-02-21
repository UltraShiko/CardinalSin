
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

    show nick happy at center, nick_far_range
    
    pause

    return


transform nick_normal_range:

    zoom 0.2976846747519294
    yoffset 25

transform nick_close_range:

    zoom 0.5
    yoffset 750

transform nick_far_range:

    zoom 0.2
    yoffset 0
    