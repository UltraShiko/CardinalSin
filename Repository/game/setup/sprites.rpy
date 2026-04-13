
### Griswyr

# TODO: Acquire Griswyr portraits 

#image side griswyr = "griswyr neutral"
#image side griswyr neutral = "griswyr neutral"
#image side griswyr angry = "griswyr angry"
#image side griswyr smile = "griswyr smile"
#image side griswyr snide = "griswyr snide"


image celestial:

    "images/sprites/celestial/neutral.webp"

image celestial smile:

    "images/sprites/celestial/default.webp"

image celestial combat:

    "images/sprites/celestial/combat.webp"



# TODO - Acquire and fine tune sprites
#image Caius: #This sprite will have him masked

    #yoffset 251

    # "images/sprites/caius/neutral.png"

layeredimage christoph:

    attribute combat: #combat is first attribute for purpose of second statement

        "images/sprites/christoph/combat.png"

    attribute base default when not combat: #when combat is not typed, base pose will appear

        "images/sprites/christoph/base.png"

    group emotions: #groups all expressions

        attribute happy: 

            "images/sprites/christoph/happy.png"

        attribute neutral:

            "images/sprites/christoph/neutral.png"

        attribute angry:

            "images/sprites/christoph/angry.png"

        attribute feral:

            "images/sprites/christoph/feral.png"



    

# TODO - Acquire and fine tune sprites
#image Christoph_combat

    #yoffset 251

    # "images/sprites/christoph/combat.png"

layeredimage nick:

    always: #ensures the default sprite is the one below

        "images/sprites/nick/base.png"

    group emotions:

        attribute happy default:

            pos (906, 417)

            "images/sprites/nick/happy.png"

        attribute neutral:

            pos (905, 434)

            "images/sprites/nick/neutral.png"

        attribute elated:

            pos (905, 412)

            "images/sprites/nick/elated.png"


### Jory

# TODO: Replace Jory's sprites with redraws if commissioned

image jory:

    yoffset 251

    "images/sprites/jory/neutral.png"
    # "images/sprites/jory/silhouette.png"

image jory angry:

    yoffset 251

    "images/sprites/jory/angry.png"
    # "images/sprites/jory/silhouette.png"

image jory happy:

    yoffset 251

    "images/sprites/jory/happy.png"
    # "images/sprites/jory/silhouette.png"

image jory neutral:

    yoffset 251

    "images/sprites/jory/neutral.png"
    # "images/sprites/jory/silhouette.png"

image jory sad:

    yoffset 251

    "images/sprites/jory/sad.png"
    # "images/sprites/jory/silhouette.png"

layeredimage persephone:

    yoffset 175
    zoom 0.90

    xysize (1962, 1471)

    always:

        "images/sprites/persephone/base.png"

    group emotions:

        attribute smirk default:

            pos (900, 333)

            "images/sprites/persephone/smirk.png"

        attribute angry:

            pos (902, 344)

            "images/sprites/persephone/angry.png"

image villager:
    yoffset 100

    "images/sprites/villager.png"


### Griswyr

image side griswyr = "griswyr_layered emo_neutral"
image side griswyr angry = "griswyr_layered emo_angry"
image side griswyr neutral = "griswyr_layered emo_neutral"
image side griswyr smirk = "griswyr_layered emo_smirk"

layeredimage griswyr_layered:

    zoom 0.7

    yoffset 500
    xoffset -120

    always:

        "images/sprites/griswyr_portraits/body.png"

    group emotes:

        attribute emo_angry:

            pos( 354, 171 )

            "images/sprites/griswyr_portraits/angry.png"  

        attribute emo_neutral default:

            pos( 353, 160 )

            "images/sprites/griswyr_portraits/neutral.png"

        attribute emo_smirk:

            pos( 354, 162 )

            "images/sprites/griswyr_portraits/smirk.png"
