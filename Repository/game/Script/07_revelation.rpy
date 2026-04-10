label revelation:

    scene background emissary base with slideleft
    play sound sfx.door_open
    show nick happy at nick_normal_range with dissolve:
        left
    #show caius neutral at caius_normal_range with dissolve:
        #right
    
    $ quick_menu = True
    window show

    "I return and find both Caius and Nick conversing."
    "The pious boy, now masked, looks to me in horror and rushes over.\nNick is as unfazed as always."

    #show caius neutral at caius_normal_range with dissolve:
        #hop
    ca "A-Are you alright?!"

    gr "Take your hand off of me. These wounds aren't fatal."
    
    ni "Oof, what happened? Vampire?"
    
    gr "I don't know what the hell he was, but he's dead. Now give me a drink!"

    play music bgm.another_day fadein 0.8
    hide nick with easeoutleft
    #show caius at caius_normal_range with dissolve:
        #hop

    "Caius recoils as a wooden mug, filled to the brim with blood, is placed before me."
    "I down it all immediately. The pain in my body eases to a dull tingle in place of the agonizing throb. I feel as if I'm drunk as both fatigue and drowsiness finally set in."

    gr "With a day of rest, I'll be as right as rain.\nMy body isn't feeble unlike yours, monk."

    #show caius snide at caius_normal_range with dissolve:
        #flip
    ca "I'm, I'm not a monk..."
    
    gr "You look and fight like one."
    
    ca "And you look like you're in a foul mood."
    
    gr "You have {i}your friend{/i} to thank for that!"
    
    #show caius neutral at caius_normal_range with dissolve:
        #flip_r
    ca "Oh, Jory must still be upset..."
    
    gr "No, but I wish he was."
    
    #hide caius with dissolve
    show nick happy at nick_normal_range with easeinright:
        right
        flip

    "That elf has a stupid grin on his face. I glare at him and it only grows."
    "I then take notice of the mask shrouding Caius's forehead.\nIt looks like its glued to his skin."
    extend " Didn't Nick mention this earlier?"

    gr "What's with the headwear?"

    ca "It's to restrain my mana..."
    
    gr "Nick?"
    
    show nick happy at nick_normal_range with move:
        center
    ni "Well, it keeps his mana from erupting, at least. Otherwise it'd burst like a geyser if something upset him."
    extend " He'll be able to fight and channel mana. This will just keep him from exploding."
    
    ca "And it's stuck to my face..."
    
    gr "Yeah, why is that?"
    
    show nick happy at nick_normal_range:
        hop
    ni "So that it attunes to his mana. Can't have Justice dislodging it."
    extend " He now has a trump card. The inhibitors will vanish if he rips it off. You might want to run when that happens~."
    
    gr "...Do you mean to tell me this boy I met just a day ago is now a ticking time bomb?"

    show nick happy at nick_normal_range:
        flip
    ni "Something like that."
    
    ca "I'm twenty, Griswyr."
    
    gr "And {i}very{/i} sheltered."

    play sound sfx.door_open
    
    hide nick
    #hide caius
    #show buzz at buzz_normal_range with moveinright:
        #center

    "Suddenly, a batlike monster, the size of my palm, flies inside." 
    play sound sfx.lunge
    extend "\nCaius leaps into action, but I block him from advancing."

    ca "Th-That's an imp! We have to-"
    
    gr "Calm yourself. This is Nick's familiar."
    
    ca "Wh-what?! But we just fought a devil! Why does he-"

    gr "Stop shouting." 
    extend "\nNick summons devils to fight devils."
    
    bu "Good evening! Buzz brings reconnaissance~."

    #show buzz at buzz_close_range with moveinright:
        #center
    "This ugly, devilish cockroach gives me a migraine."
    extend "\nOh Ishmael, how much more will you test my patience tonight?!"

    "Nick chuckles faintly. He isn't amused, he's guilty."
    extend " Whenever he's done something foolish, he acts like this. A sane mortal would dread my wrath, but Nick's lust for pain encourages it."

    gr "Caius, fetch me a broom."
    extend "\nOn second thought, a broom won't cut it. Grab me that staff over there."
    
    ca "Umm, okay...?"
    
    ni "Alright Buzz, tell them what we saw."

    bu "Oooh yes, city destroyed! Burned! Blood and ash everywhere!"
    extend "\nMany dead knights, with red and brown armors scattered about!\nIt was hilarious! Favorite mission so far~!"
    
    gr "Hmm, so those Exorcists perpetuated that..."

    ni "Yep... They lacked the numbers to face the Celestials, so they sacked Thrycia."
    ni "I guess they believed their attack wouldn't warrant retaliation. Thrycia was technically independent."

    gr "I do not understand why we cling to this peace."
    extend "\nIt's only a matter of time before those peons attack again."
    
    #show buzz at buzz_close_range with moveinright:
        #hop
    bu "Unlikely! All of them are dead hahahaha!"

    ca "W-wait, you were there at Thrycia?!"

    #show caius snide at caius_normal_range with easinleft:
        #left

    "Caius eagerly passes me the staff. His eyes are filled with desperation, hoping that his friend was not responsible, I imagine."
    "The imp eyes him like a slab of meat. I guess devils big and small can't resist corrupting souls as virtuous as his."

    gr "Nick, keep your pet under control or you'll need a new one."
    
    #show buzz at buzz_close_range with moveinright:
        #hop
    bu "Aiieee... Buzz continue."
    
    ca "Did you see a dretchling? Any survivors?"

    bu "Nope~. Buzz said everyone dead." 
    extend"\nHowever...Buzz found a charred silhouette on the ground~. Only devils could broil the earth like that. 
    We explode when slain."
    
    gr "Oh really? Tell us more..!"

    play sound sfx.light_grapple
    #hide caius
    #hide buzz 
    #with dissolve
    show nick happy at nick_normal_range with dissolve:
        center

    "The wood creaks in my palms and Nick gulps in excitement."
    
    show nick happy at nick_close_range with dissolve:
        center
    
    "I arch forward, already knowing what that imp is going to say.\nI only await confirmation..!"

    bu "Buzz know mana signature of the deceased. Yes yes, the hellknights were not alone. In fact, some corpses were nice and crispy~.\nElectrocuted, hmhmhm!"
    bu "Buzz detect powerful mana. Very malicious and sadistic.\nWe devils enjoy torturing others, but this one's bloodlust is unrivaled."
    
    show nick elated #further than before
    
    extend "\nYes, Buzz detect what you mortals call; a pain devil-"

    play sound sfx.wood_break
    hide nick with quickflash

    "It's instantaneous. The staff breaks on the first strike."
    
    play sound sfx.wood_break
    with quickflash

    extend "\nBuzz darts to the ceiling and Caius watches, horrified, as I proceed to beat Nick with the splintered staff."
    
    play sound sfx.wood_break
    with quickflash
    "Small giggles escape him each time my boot bludgeons his chest.\nI'm almost happy he's enjoying it, because I don't need to worry about breaking him."

    ca "St-Stop! You're going to kill him!"
    
    gr "{size=+80}{b}GOOD!{/b}{/size}" with vpunch #center text via textbox

    show nick at nick_close_range with easeinbottom:
        center
    ni "Hehehe... It could be any pain-"

    play sound sfx.wood_break
    with quickflash

    extend " Ouch!" 

    play sound sfx.wood_break
    with quickflash
    extend " Ouch!"

    play sound sfx.wood_break
    with quickflash
    extend " Ouch, hehehe!"
    
    gr "Behold, monk!"

    play sound sfx.grapple

    hide nick with fade
    #show caius snide at caius_close_range with fade:
        #center
    
    "I yank Nick up by his hair and make him face Caius."
    "Ishmael knows what godforsaken expression is on Nick's face.\nI never understood Caius's fixation on joining us."
    extend "\nEither way, here's his chance to quit!"

    gr "Thrycia was your home, right? \nRemember how your friend was blamed for its destruction?"
    gr "Well, you can thank this maniac for that!" with vpunch
    extend "\nYes, the leader of us Emissaries is an irresponsible lunatic who summons devils! He is who you'll be working under."
    gr "That pain devil that destroyed Thrycia was {i}his{/i} doing! He could've banished too, and now she's loose..."

    ca "...If you understood how destructive this monster could be, why would you bind her?"
    
    ni "She's useful."

    gr "Worst of all, she's going to want revenge, and you and I will be the ones to hunt her down!" 
    extend "\nIf you thought Persephone was bad, oh Ishmael... You are not prepared!"
    
    ni "Devils take years to revive. We have tim-"
    
    play sound sfx.wood_break
    with quickflash
    
    gr "Be quiet, swine!" with vpunch
    gr "If this tomfoolery teaches you anything, monk, let it be that you should leave."
    extend "\nGo join the Celestials if you want to play the hero."
    
    ca "Hmm..."

    "He squints at us both." 
    extend " As dumbfounded as he seems, I'm impressed with how quickly he regains his composure. Especially considering how he just lost his hometown because of an idiot."
    "Granted, Caius has a level head despite being so green.\nHe only loses himself when his past is brought up, a weakness the banshee exploited..."
    
    ca "...You summon fiends, does that mean you know how to defeat them?"

    show nick at nick_normal_range with easeinright:
        right
        flip
    ni "Of course. It's my passion. A really bad passion hehehe, but I know just about everything when it comes to devils."
    
    gr "He's only escaped the noose because he's useful.\nEven {i}the Third{/i} had to put up with him."

    play music bgm.marching_forward fadein 0.8

    ca "Tell me Nick, can you track down my friend."
    extend "\nIf you can bind devils, perhaps you can seek out a dretchling?"
    
    gr "You don't need this fool's aid. Consult the Reverend."

    #show caius neutral at caius_close_range with fade:
        #hop
    ca "But fiends are drawn to dretchlings like moths to a flame. Maybe this pain devil was after him."
    
    #show buzz at buzz_normal_range with moveinleft:
        #left

    bu "Buzz knows~! Two mana signatures were detected."
    
    gr "...And you waited to share this fact because?"
    
    #show buzz at buzz_normal_range with moveinleft:
        #hop
    bu "You-You attack Buzz master!" with vpunch
    
    ca "Please continue, Buzz."

    bu "Second signature was weak. No corpse detected."
    extend "\nIt was a fiend, a very powerful fiend~!"

    hide nick 
    #hide buzz 
    #hidde caius
    with dissolve

    "I groan as Caius's eyes expand. He has a one track mind, this monk..."
    "He'll be a liability, at this rate. All some monster has to do is capture his friend, and Caius will surrender."
    extend " Besides, we Emissaries are not saviors."

    gr "Monk, heed my words."
    extend " If you think I'm about to partake in some rescue mission, do us both a favor and abandon all hopes of joining us."

    #show caius neutral at caius_close_range with dissolve:
    ca "...I know it might be foolish of me. However, Nick has no trace on Persephone's whereabouts. So I wonder if she might be involved somehow?"
    
    gr "Do you honestly believe some dretchling would attract the banshee?"

    ca "The fiendish presence was powerful, and we both know how deadly she is."
    extend " Frankly, I plan on going to Thrycia with or without you. It was what I wanted to do before, you know..."
    
    gr "Thrycia is a week's travel by horseback. Unless you plan to walk..."
    
    show nick happy at nick_normal_range with easeinleft:
        left
    ni "I can arrange a carriage."
    
    gr "Be quiet-"
    
    show nick happy at nick_normal_range:
        hop

    ni "Nah. I think Caius has a point."
    extend " More importantly, there's another powerful fiend on the loose. We probably need to stop it."
    
    gr "Do not fill his head with fantasies, Malconvoker! \nHe's barking up the wrong tree."
    
    ni "He doesn't think so. Otherwise, he would've fled to the reverend once he learned it was my fault."
    extend " You're misreading him, Griswyr. Yes he wants to save his friend, but he also wants to fight devils."

    #show caius neutral at caius_close_range:
        #flip
    ca "That, and I believe that the Celestials aren't addressing the root of our problems."
    extend "\nI'd much rather cleanse the source, even if I have to get my hands dirty..."

    show nick elated at nick_close_range with dissolve

    ni "And besides vampire, someone needs to keep you in-"

    $ quick_menu = False
    window hide

    play sound sfx.hurl

    hide nick with moveoutright

    play sound sfx.pottery_break
    with quickflash

    $ quick_menu = True
    window show

    "I toss him into the wall. I've heard enough of his nonsense."

    gr "Very well, you are hereby my suboordinate."
    extend " But understand this.\nWe will do things {i}my{/i} way. I'm not interested in rescuing damsels, or your friend."
    gr "In fact, I plan to kill him if he's aiding fiends, and I expect you to back me up."
    
    ca "I'm aware..."
    
    gr "Elf, make arrangements. Once my wounds are healed, we depart."
    extend "\nAs for you, monk..."
    
    ca "Why do you keep calling me that...?"

    gr "Start trying to get that mana of yours under control.\nIf you're truly able to wield Justice, we'll need that firepower."
    gr "More importantly, I don't want to have to protect you from yourself.\nI expect you to make the most of your respite."
    
    #show caius happy at caius_close_range:
        #hop
    ca "You don't have to tell me twice."
    
    bu "Buzz accompany you~. Act as eyes and ears for master."
    
    ni "Yes, try not lose your temper on him, Griswyr."
    
    gr "I make no promises..."

    $ quick_menu = False
    window hide

    scene image "#000" with pixellate

    play sound sfx.drop_clothes

    $ quick_menu = True
    window show

    "I rest on one of the beds, throwing the blanket over my face so I don't have to see either of them any longer."
    "My mind races. I still can't believe that I channeled Sin in place of Malice.  Does this development imply I'm getting soft? I sure hope not..."
    "I clench my fists, still irate at what Jory said."
    extend "\nThat \"kindness\" nearly cost me my life. Am I to be food for monsters because I'm sentimental now? I'd sooner die!"
    "Besides, I'm going to have to keep that monk from getting himself killed. It isn't a matter of when our enemy exploits his piety, but {i}when{/i}."
    extend "\nIf anything, I need to toughen up on the-"

    stop music fadeout 0.8

    vi "Hey Snowflake! We need to chat." with vpunch

    "A voice booms into my ear. No one else has arrived here, or Caius and Nick would've reacted by now. And our base is littered with alarm wards. So it must be telepathy."
    "That, and only one person addresses me with that name..."

    gri "Banshee. To what do I owe the displeasure?"

    $ quick_menu = False
    window hide

    play music bgm.mother_of_the_damned fadein 0.8

    show persephone angry at t_alpha(0.3) with Dissolve(1.0): #t_alpha makes her sprite transparent
        center

    pause 1.0

    $ quick_menu = True
    window show
    
    pei "So I did some digging, and you're a liar. You weren't jinxed, you fed on a child... You turned him into a freak, {i}after{/i}, you devoured his mother in front of him!"

    gri "Heh, do my ears betray me, or does {i}the banshee{/i} have a bleeding heart?"
    gri "The fact that you fell for such a fib betrays your ignorance.\nPerhaps you aren't as clever as I thought."

    pei "Yeah, well, here's something to chew on. If I see you again, it's on sight!"
    extend " And here I was pitying you, willing to take you under my wing.\nYou're disgusting, and that's coming from me..."

    gri "Oh no, the Banshee doesn't approve of me.\nI'm certain to lose so much sleep."
    gri "Especially when you and your broodmother's henchman murdered thousands. People still suffer because {i}the Reckoning{/i}.\nAnd you don't scare me, heh, it's quite the opposite."
    gri "If you're so offended, then stop hiding. We'll find you eventually."
    
    show persephone smirk at t_alpha(0.3)

    pei "In due time, Snowflake. Your days are numbered all the same.\nYou'll beg for death when Mother gets her hands on you."
    
    gri "My days have been numbered. Do you have anything new to share?"

    window hide

    hide persephone with dissolve

    window show

    "She stops responding. I opt not to inform my comrades.\nWe can't trace telepathy anyway."
    play sound sfx.dagger_draw
    "I reach for my hatchet and view my bloodied reflection."
    extend "\nI gather a streak of the blood on my finger and lick it, treating myself to the sight of a monstrous grin."

    gr "Wonderful! That's just the way I wanted it, banshee!"

    window hide

    ##############################
    ### Roll credits.
    ##############################

    $ quick_menu = False
    window hide
    
    call screen cinematic_credits_screen()

    # Update flag used to determine if the ending has been seen once.
    # From this point forward, the credits can be skipped.
    $ persistent.ending_watched =  True

    #pause 3.0

    ##############################
    #### Game ends
    ##############################

    stop music fadeout 0.8

    return