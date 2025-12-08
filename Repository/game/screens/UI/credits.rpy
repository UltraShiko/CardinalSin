
### Auxiliary variables.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
{b}Credits:{/b}

{b}Director / Lead Writer{/b}

TotalLeeAwesome ({a=https://twitter.com/BigoofStudios}Twitter{/a})

{b}Script Editor{/b}

Jenna Rose ({a=https://twitter.com/JRoseReads}Twitter{/a}, {a=http://www.jrosereads.com/}Website{/a})

{b}Lead Background Artist{/b}

Lynnasaurus ({a=https://www.instagram.com/borderbreakersofficial/}Instagram{/a})

{b}Sprite Artist{/b}

Kate ({a=https://www.instagram.com/rkade801}Instagram{/a})

{b}Cinematography{/b}

ragyuo ({a=https://linktr.ee/ragyuo}Linktree{/a})

{b}GUI & Logo Designer, UI coding, Marketing Assets & Jory's sprite artist{/b}

senchousan ({a=https://twitter.com/s3nchousan}Twitter{/a})

{b}Coding{/b}

YoruUta ({a=https://yoruuta.itch.io}Itch.io{/a})

{b}Sound Composer{/b}

Monochrome ({a=https://twitter.com/mediamonochrome}Twitter{/a})

{b}Casting & Voice Direction{/b}

ChickenUkelele


{b}Voice Acting (by order of appearance):{/b}

{b}Young Caius{/b} - Roxcoord ({a=https://roxcoord.carrd.co/}Website{/a})

{b}Priam{/b} - Shykodah-Khi McGrath ({a=https://www.shykodah-khi.com/voice-over}Website{/a})

{b}Caius{/b} - Noah Blum ({a=https://x.com/wingsofthemoth}Twitter{/a})

{b}Jory{/b} - Dylan Duck ({a=https://www.dylanduck.com/}Website{/a})

{b}Reverend Hale IV{/b} - Matthew S. Scott ({a=https://twitter.com/matthewsscottvo}Twitter{/a})

{b}Griswyr{/b} - Justice Margowski ({a=https://linktr.ee/justicemargowski}Linktree{/a}))

{b}Cultist A{/b} - Claudio F ({a=https://claudiof.carrd.co/}Website{/a})

{b}Cultist B & D{/b} - Jeff Rosenau ({a=https://twitter.com/JeffRosenauVA}Twitter{/a})

{b}Cultist C{/b} - Lazzi Faire ({a=https://x.com/Lazzifaire}Twitter{/a})

{b}Cultist Mage{/b} - Rachel Adkins ({a=https://x.com/reabear_}Twitter{/a})

{b}Persephone{/b} - Savy Des-Etages ({a=https://soundofsavy.com/}Website{/a})

""")

#
# {b}Voice cast:{/b}
#
# {b}Aurielle{/b}
# Savy Des-Etages ({a=https://twitter.com/Savy_VO}Twitter{/a}, {a=https://soundofsavy.com/}Website{/a})
#
# {b}Orpheus{/b}
# Allen Chan ({a=https://twitter.com/WhoIsAllenChan}Twitter{/a}, {a=https://www.whoisallenchan.com}Website{/a})
#
# {b}Jory{/b}
# Dylan Duck ({a=https://twitter.com/CrashStarVA}Twitter{/a}, {a=https://www.dylanduck.com/}Website{/a})
#
# {b}Reverend Hale{/b}
# Ethan Waldrep ({a=https://twitter.com/ItsFennwic}Twitter{/a})
#
# {b}Desiree / Hecate{/b}
# Vera Tan ({a=https://twitter.com/veratanva}Twitter{/a}, {a=https://veratan.fun/}Website{/a})
#
# {b}Child / Angry Crowd{/b}
# Jett Barker ({a=https://twitter.com/barkervoiceover}Twitter{/a})
#
# {b}Parent / Wedding Guest / Angry Crowd{/b}
# Mari Chavez ({a=https://twitter.com/TypicalMariVO}Twitter{/a})
#
# {b}Angry Crowd{/b}
# Robert Jackson ({a=https://twitter.com/Mystic_IRJ}Twitter{/a})
#
# {b}Angry Crowd / Wedding Guest{/b}
# Jerron Bacat ({a=https://twitter.com/JerronBacat}Twitter{/a})









## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
