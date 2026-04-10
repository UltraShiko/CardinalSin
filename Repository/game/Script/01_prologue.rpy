label prologue:

    camera:
        perspective True

    $ quick_menu = True
    window show

    "...My head, it hurts..."
    "I can't see... Every time I open my eyes, a red goo burns them.\nThis ick is all over me..."

    v "-istop- Chris- ca- -ou -ar me?!" with vpunch

    $ quick_menu = False
    window hide

    play music bgm.something_amiss fadein 0.5
    
    scene cg christoph with Dissolve(1.0)

    pause 1.0

    $ quick_menu = True
    window show

    "Mom...?"
    "I try wiping the red stuff away, but it keeps coming.\nOnly a warm cloth manages to douse this 
    crimson stream."

    mo "By Ishmael, he split your head open..."
    ch "Mom...? What's-"
    mo "Shh! Be quiet, dear. He's still outside."
    ch "He...?"

    "My head throbs suddenly. Even thinking about it hurts...!"
    "I was, outside, gathering firewood and-"

    play sound sfx.zap
    with quickblood

    ch "Aghhh!"
    mo "Shh! You have to be strong. You have to or he'll-"

    play sound sfx.pottery_break
    with quickflash

    "Mommy holds me tight as our bedroom door is torn from its hinges.\nWe're crammed inside the wardrobe."
    "Heavy footsteps pound against our floor, followed by crashing sounds as our stuff is thrown around."
    "Mom tries to calm me down by humming in my ear.\nOne hand presses a hankerchief to my head, and her other hand grips a knife."
    extend " But she'll die if he catches us. He's a monster..."
    "He threw me at a tree like I was a toy. That's all I can remember..."

    play sound sfx.door_break
    with hpunch
    v "{size=+40}Graaaah! Where the hell are they?!{/size}" with vpunch

    play sound sfx.light_grapple
    "Mama holds my mouth shut as another door is torn from its hinges.\nHe's in our room..."
    "Mom's breathing is getting faster.\nShe pulls me back, tucking me under her arms and scooting in front of me."

    ch "Mom, you'll die! He wants me, so I'll-"
    mo "No, no, Christoph... I won't let him hurt you again."

    play sound sfx.wood_break
    with quickflash

    ch "But mom he's-"
    mo "Shh! Not another word."
    ch "But-"
    mo "I love you, Christoph. I always-"

    $ quick_menu = False
    window hide
    
    play sound sfx.door_break
    with vpunch

    pause 2.0

    play sound sfx.weapon_swing
    call screen image_display("vfx/sword_swing.png")
    queue sound sfx.blood_splatter
    with quickblood
    scene image "#000"

    $ quick_menu = True
    window show
    
    ch "Mooooom!!!" with vpunch

    "My mouth falls open. All I see is the door crumble, and then Mom..."
    "She tried her best, throwing herself at him."
    extend "\nBut...it isn't enough. He grabs her and sinks and bites into her throat."
    "Her body twitches. I hear her gagging as she stares into my eyes."
    extend "\nI hear him sucking, but blood is everywhere... It makes me want to puke!"

    mo "Uughhh..."
    extend " Chris...toph-"

    v "Mmph! Bland."

    $ quick_menu = False
    window hide

    scene christoph2 with iris_in_out
    play sound sfx.thud

    pause 1.2

    $ quick_menu = True
    window show

    "He drops her like a sack of potatoes."
    extend "\nShe lies there, her eyes open and her throat torn to shreds."
    "Their pupils look at me. It feels like she's still here, even though she's not..."
    "I shiver like a leaf as the monster, looking like one of the humans, wipes his mouth and glares at me."
    "A mix of tears and more goop run down my face. I'm about to cry, but I clench my fists instead."
    play sound sfx.dagger_draw
    "I grab the knife from mom's body."
    extend "\nI know I can't hurt him, but I'll make him pay!"
    extend " Somehow..."

    ch "You...You killed her-"
    
    play sound sfx.weapon_swing
    call screen image_display("vfx/sword_swing.png")
    scene christoph2:
        zoom 1.5
    queue sound sfx.grapple
    with quickflash
    
    extend " Aggh!"
    
    v "If you hadn't ran, she'd be alive."
    
    play sound sfx.slash

    scene image "#f00" with Dissolve(0.2)
    
    ch "{size=+80}{b}AHHHHHHHHH!!!{/b}{/size}" with vpunch
    
    $ quick_menu = False
    stop music
    window hide
    
    jump explanation

    #return