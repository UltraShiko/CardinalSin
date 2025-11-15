# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Celestial")
define ca = Character("Caius")
define ch = Character("Christoph")
define gr = Character("Griswyr")
define gri = Character("Griswyr", what_italic=True)
define j = Character("Jory")
define m = Character("Man")
define mo = Character("Mom")
define ni = Character("Nick")
define pei = Character("Persephone", what_italic=True)
define v = Character("Voice")
define vi = Character("Voice", what_italic=True)
define w = Character("Woman")


init: # lets me have the screen flash certain colors
    define bloodflash = Fade(.25, 0.0, .75, color="#ff0000")
    define maliceflash = Fade(.25, 0.0, .75, color="#680a0a")
    define sinflash = Fade(.25, 0.0, .75, color="#56066e")
    define graceflash = Fade(.25, 0.0, .75, color="#92a9f5")
    define iceblast = Fade(.1, 0.0, .75, color="#ced6f0")
    define fireflash = Fade(.25, 0.0, .75, color="#cb7f1c")
    define electricflash = Fade(.25, 0.0, .75, color="#5c7bd5")
    
init python: #allows me to attach sound fx to transform commands
    def play_sound_c(trans, st, at, file=None):
        renpy.sound.play(file, loop=False)
        return None
    play_sound = renpy.curry(play_sound_c)

define quickblinds = ImageDissolve(im.Tile("blindstile.png"), 0.5, 8)
define quicksquares = ImageDissolve(im.Tile("squarestile.png"), 0.5, 256)

# The game starts here.

label Prologue:

    #scene CG
    "...My head, it hurts..."
    "I can't see...nothing but stars. And there's something gooey on me."

    v "-istop- Chris- ca- -ou -ar me?!"

    "Mom...?"
    extend " Owww, the red stuff is in my eyes. It's warm and sticky..."
    "I brush it away but it keeps coming. Only a warm cloth can douse the stream."

    mo "By Ishmael, he split your head open..."
    ch "Mom...? What's-"
    mo "Shh! Be quiet, dear. He's still outside."
    ch "He...?"

    "My head throbs suddenly. Thinking about it hurts...!"
    "I was, outside, gathering firewood and-"

    play sound zap
    with bloodflash
    ch "Aghhh!"
    mo "Shh! You have to be strong. You have to or he'll-"

    #play sound crash
    with hpunch
    "Mommy holds me tight as our door is torn from its hinges. We're crammed inside the wardrobe."
    "Heavy footsteps pound against our floor, followed by our stuff being thrown to and fro."
    "Mom tries to calm me down by humming in my ear. One hand presses a hankerchief on my head, and the other grips a knife."
    extend " But she'll die if he catches us. He's a monster..."
    "He threw me at a tree like I was a toy. That's all I can remember..."

    v "Graaaah! Where the hell are they?!" with vpunch

    "Mama holds my mouth shut as another door is torn from its hinges. He's in our room..."
    "Mom's breathing is getting faster. She pulls me back, tucking me in her arms and scooting in front of me."

    ch "Mom, you'll die. Let me-"
    mo "No, no Christoph... I won't let him hurt you again."

    #play sound crash
    with hpunch
    ch " But mom he's-"
    mo "Shh! Not another word."
    ch " But-"
    mo "I love you, Christoph. I always-"

    #play sound crash
    #play sound weapon_swing
    #play sound blood_splatter

    ch "Mooooom!!!" with vpunch

    "My mouth falls open. All I saw was the door open, and mom..."
    "She didn't even hurt him. She jumped at him, driving the knife into his chest. Did it even hurt...?"
    "Now, he holds her, his teeth tearing into her neck."

    v "Uughhh..."
    extend " Chris...toph-"
    v "Mmph! Bland."

    #play sound thud
    "He drops her like a sack of potatoes. She lays there, her eyes open and her throat torn open."
    "The monster, looking like one of the humans, wipes his mouth and glares at me."
    "I stare back, both afraid and angry."
    extend " I grab the broom. I know I can't hurt her, but I'll make him pay! Somehow.."

    ch "You...You killed her-"
    play sound weapon_swing
    queue sound grapple
    extend " Aggh!"
    v "If you hadn't ran, she'd be alive."
    #have screen turn red
    ch "{b}AHHHHHHHHH!!!{/b}" with vpunch
    
    jump Explanation
