

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing 0

        # if main_menu:
        #
        #     textbutton _("Start") action Start()
        #
        # else:

        if not main_menu:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        textbutton _("Compendium") action ShowMenu("compendium_screen")

        if not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("Credits") action ShowMenu("about")

        textbutton _("Controls") action ShowMenu("help")

        textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
