
### Griswyr

# TODO: Acquire Griswyr portraits 

#image side griswyr = "griswyr neutral"
#image side griswyr neutral = "griswyr neutral"
#image side griswyr angry = "griswyr angry"
#image side griswyr smile = "griswyr smile"
#image side griswyr snide = "griswyr snide"

# TODO - Redraw sprite if available
#image Celestial:

    #yoffset 251

    # "images/sprites/celestial/default.webp"

#image Celestial combat:

    #yoffset 251

    # "images/sprites/celestial/combat.webp"

# TODO - Acquire and fine tune sprites
#image Caius: #This sprite will have him masked

    #yoffset 251

    # "images/sprites/caius/neutral.png"

# TODO - Acquire and fine tune sprites
#image Christoph

    #yoffset 251

    # "images/sprites/christoph/neutral.png"

# TODO - Acquire and fine tune sprites
#image Christoph combat

    #yoffset 251

    # "images/sprites/christoph/combat.png"

layeredimage nick:

    yoffset 175
    zoom 0.90

    xysize (1962, 1471)

    always: #ensures the default sprite is the one below

        "images\sprites\nick\base.png"

    group emotions:

        attribute happy default:

            pos (900, 333)

            "images\sprites\nick\happy.png"

        attribute neutral:

            pos (900, 333)

            "images/sprites/nick/neutral.png"

        attribute elated:

            pos (902, 344)

            "images/sprites/nick/elated.png"


### Jory

# TODO: Replace Jory's sprites with redraws if commissioned

image Jory:

    yoffset 251

    "images/sprites/jory/neutral.png"
    # "images/sprites/jory/silhouette.png"

image Jory angry:

    yoffset 251

    "images/sprites/jory/angry.png"
    # "images/sprites/jory/silhouette.png"

image Jory happy:

    yoffset 251

    "images/sprites/jory/happy.png"
    # "images/sprites/jory/silhouette.png"

image Jory neutral:

    yoffset 251

    "images/sprites/jory/neutral.png"
    # "images/sprites/jory/silhouette.png"

image Jory sad:

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

### Other


