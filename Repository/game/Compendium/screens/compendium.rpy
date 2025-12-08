
### Style

style codex_label is gui_label:

    xalign 0.5
    xoffset 150
    yoffset 100
    size 50

style codex_label_text is gui_label_text

style codex_text is gui_text:

    justify True

style codex_label_text:

    size gui.label_text_size

style codex_scrollbar is gui_vscrollbar:

    xoffset 100

style compendium_screen_title_style:

    bold True
    size 50

### Screen used to display the compendium information unlocked by the player.

screen compendium_screen():

    modal True

    tag menu

    ### Variables.
    default currently_selected_entry = -1

    frame:

        pos (0,0)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background "Compendium/gui/background.png"

        ### Title
        text "Compendium":

            xpos 85
            ypos 0.054

            size gui.title_text_size
            color gui.accent_color

        ### List of entries.

        ## Viewport containing the entries.
        viewport:

            xpos 25 ypos 400
            xsize 350 ysize 350

            mousewheel True
            scrollbars "vertical"
            draggable True
            pagekeys True

            vbox:
                spacing 10
                xoffset 350

                for i in range ( 0, persistent.compendium.numberOfEntries() ):

                    if persistent.compendium.isEntryLocked( i ):

                        text "????":

                            style "button_text"

                    else:

                        textbutton persistent.compendium.getEntryTitle( i ):

                            selected ( i == currently_selected_entry )

                            if currently_selected_entry == -1:

                                action SetScreenVariable( "currently_selected_entry", i )

                            else:

                                action [
                                    SetScreenVariable( "currently_selected_entry", i ),
                                    Scroll("compendium_content_viewport", "vertical decrease", amount=1.0)
                                ]

        ### Selected entry content.

        # Only display the information, if the selected entry index is different than -1.
        # -1 means no entry is selected.
        if not currently_selected_entry == -1:

            # vbox:
            #     style_prefix "codex"
            #
            #     xsize 850
            #     xalign 0.5 yalign 0.5
            #     xoffset 200
            #     text persistent.compendium.getEntryContent( currently_selected_entry )
            #     #text _p("""Welcome to the codex!""")


                    #Really short text might not be centered correctly, you have to adjust the xoffset.


            viewport:

                id "compendium_content_viewport"

                xpos 642 ypos 190
                xsize 948 ysize 781

                mousewheel True
                scrollbars None
                draggable True
                pagekeys True

                scrollbar_unscrollable "hide"

                vbox:

                    pos (0,0)
                    xfill True
                    yfill False

                    text persistent.compendium.getEntryContent( currently_selected_entry ):

                        justify True

                    #    style "compendium_content_text"

            # Right Scroller
            vbar:

                #style "compendium_vbar_small"

                pos (1710, 190)
                xysize (18, 781)

                unscrollable "hide"


                value YScrollValue( "compendium_content_viewport" )
        #
        #     ### Buttons
        #     # use shared_back_button()
        #
        #     ### Reset compendium.
        #     imagebutton:
        #
        #         pos (500, 123)
        #         xysize (393, 50)
        #
        #         idle "Compendium/gui/rc_idle.png"
        #         hover "Compendium/gui/rc_hover.png"
        #
        #         action Confirm(
        #             "This will reset compendium, reverting it to its original state.\nProceed?",
        #             yes=Function( clearCompedium ),
        #             no=NullAction()
        #         )
        #


    textbutton _("Return"):

        style "return_button"

        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
