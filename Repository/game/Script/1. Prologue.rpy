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

label Prologue:

    #scene CG
    "...My head, it hurts..."
    "I can't see... Every time I open my eyes, a red, goo burns them. This ick is all
    over me..."

    v "-istop- Chris- ca- -ou -ar me?!"

    "Mom...?"
    "I try wiping the red stuff aweay, but it keeps coming. Only a warm cloth manages to douse this 
    crimson stream."

    mo "By Ishmael, he split your head open..."
    ch "Mom...? What's-"
    mo "Shh! Be quiet, dear. He's still outside."
    ch "He...?"

    "My head throbs suddenly. Even thinking about it hurts...!"
    "I was, outside, gathering firewood and-"

    play sound zap
    with bloodflash
    ch "Aghhh!"
    mo "Shh! You have to be strong. You have to or he'll-"

    #play sound crash
    with hpunch
    "Mommy holds me tight as our front door is torn from its hinges. We're crammed inside the wardrobe."
    "Heavy footsteps pound against our floor, followed by crashing sounds as our stuff is thrown around."
    "Mom tries to calm me down by humming in my ear. One hand presses a hankerchief to my head, and her other hand grips a knife."
    extend " But she'll die if he catches us. He's a monster..."
    "He threw me at a tree like I was a toy. That's all I can remember..."

    v "Graaaah! Where the hell are they?!" with vpunch

    "Mama holds my mouth shut as another door is torn from its hinges. He's in our room..."
    "Mom's breathing is getting faster. She pulls me back, tucking me under her arms and scooting in front of me."

    ch "Mom, you'll die! He wants me, so I'll-"
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

    "My mouth falls open. All I see is the door open, and then Mom..."

    play sound stab
    "She tries her best. lunging and driving the knife into his chest." 
    extend " But there's no sign that he's hurt..."
    "He grabs her, and his teeth tear into her neck."
    extend " Red goo starts gushing from her. I yelp as some splatters on my leg."

    v "Uughhh..."
    extend " Chris...toph-"
    v "Mmph! Bland."

    #play sound thud
    "He drops her like a sack of potatoes. She lies there, her eyes open and her throat torn to shreds."
    extend " Their pupils look at me. It feels like she's still here, even though she's not..."
    "I shiver like a leaf as the monster, looking like one of the humans, wipes his mouth and glares at me."
    "A mix of tears and more goop run down my face. I'm about to cry, but I clench my fists instead."
    extend " I grab the broom. I know I can't hurt her, but I'll make him pay! Somehow..."

    ch "You...You killed her-"
    play sound weapon_swing
    queue sound grapple
    extend " Aggh!"
    v "If you hadn't ran, she'd be alive."
    #play sound heavy_slash
    #have screen turn red
    ch "{b}AHHHHHHHHH!!!{/b}" with vpunch
    
    jump Explanation
