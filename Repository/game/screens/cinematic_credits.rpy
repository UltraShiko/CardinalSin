
### Auxiliar animations.

transform credits_text_fade(pause_time, fadein_time, hold_time, fadeout_time):

    alpha 0.0

    pause pause_time

    ease fadein_time alpha 1.0

    pause hold_time

    ease fadeout_time alpha 0.0

### Auxiliary styles

style credits_text_role_style:

    text_align 0.5
    xalign 0.5

    font "fonts/GARA.TTF"
    size 50
    color "#fff"

    bold True

style credits_text_name_style is credits_text_role_style:

    size 50

    bold False

### Screen definition

screen cinematic_credits_screen():

    timer 40.0 action Return()

    frame:

        pos (0,0)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background "#000"

        ### Credit page 1
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Director & Lead Writer", "TotalLeeAwesome")

            null height 150 width 0

            use credits_screen_role_and_name("Script Editor", "Jenna Rose")

            at credits_text_fade(0.0, 1.0, 2.0, 1.0)

        ### Credit page 2
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Background artist", "Lynnasaurus")

            null height 150 width 0

            use credits_screen_role_and_name("Sprite Artist", "Kate")

            at credits_text_fade(5.0, 1.0, 2.0, 1.0)

        ### Credit page 3
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Cinematography", "ragyuo")

            null height 150 width 0

            use credits_screen_role_and_name("GUI & Logo Designer, UI coding,\nMarketing Assets & Jory's sprite artist", "senchousan")

            at credits_text_fade(10.0, 1.0, 2.0, 1.0)

        ### Credit page 4
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Coding", "YoruUta")

            null height 150 width 0

            use credits_screen_role_and_name("Sound Composer", "Monochrome")

            null height 150 width 0

            use credits_screen_role_and_name("Casting & Voice Direction", "ChickenUkelele")

            at credits_text_fade(15.0, 1.0, 2.0, 1.0)

        ### Credit page 5
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Young Caius's voice", "Roxcoord")

            null height 150 width 0

            use credits_screen_role_and_name("Priam's voice", "Shykodah-Khi McGrath")

            null height 150 width 0

            use credits_screen_role_and_name("Caius's voice", "Noah Blum")

            at credits_text_fade(20.0, 1.0, 2.0, 1.0)

        ### Credit page 6
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Jory's voice", "Dylan Duck")

            null height 150 width 0

            use credits_screen_role_and_name("Reverend Hale IV's voice", "Matthew S. Scott")

            null height 150 width 0

            use credits_screen_role_and_name("Griswyr's voice", "Justice Margowski")

            at credits_text_fade(25.0, 1.0, 2.0, 1.0)

        ### Credit page 7
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Cultist A's voice", "Claudio F")

            null height 150 width 0

            use credits_screen_role_and_name("Cultist B & D's voice", "Jeff Rosenau")

            null height 150 width 0

            use credits_screen_role_and_name("Cultist C's voice", "Lazzi Faire")

            at credits_text_fade(30.0, 1.0, 2.0, 1.0)

        ### Credit page 7
        vbox:

            align (0.5, 0.5)

            xfill False
            yfill False

            use credits_screen_role_and_name("Cultist Mage's voice", "Rachel Adkins")

            null height 150 width 0

            use credits_screen_role_and_name("Persephone's voice", "Savy Des-Etages")

            at credits_text_fade(35.0, 1.0, 2.0, 1.0)

    # If credits have been watched once, allow the credits to be skipped.
    if persistent.ending_watched is True:

        key "dismiss" action Return()

    # Disable the option of opening the menu.
    key "game_menu" action NullAction()



screen credits_screen_role_and_name(role, name):

    text role:

        style "credits_text_role_style"

    null height 15 width 0

    text name:

        style "credits_text_name_style"
