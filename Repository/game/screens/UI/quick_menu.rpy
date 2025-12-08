
## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            spacing 5

            textbutton _("Back") action Rollback()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Log") action ShowMenu('history')

        imagebutton auto "gui/skip_%s.png" xpos 1620  ypos 845 action Skip() alternate Skip(fast=True, confirm=True)
        imagebutton auto "gui/codex_%s.png" xpos 1620  ypos 920 action ShowMenu('compendium_screen')
        imagebutton auto "gui/gear_%s.png" xpos 1620 ypos 770 action ShowMenu('preferences')

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
