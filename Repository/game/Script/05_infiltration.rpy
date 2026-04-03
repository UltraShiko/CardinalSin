
label infiltration:

    play music bgm.winter_ambience loop
    hide celestial 
    hide celestial_2
    with moveoutright #Idk how to have the hide command apply to one of the sprites
    "I chortle darkly as I slip past the demoralized hallowmen."
    "Seeing that pig's delusions reminds me of my own.\nJudge him as I may, I wasn't much different..."
    "The hallucinations vary based on our desires.\nI thought I could fly out of this god forsaken empire. My hardships were caused by {i}the Recknoning's{/i} impact."
    "Thanks to that archfiend, all I knew was poverty and sadness.\nSanguine Paste gave me everything I ever wanted, and took everything else..."
    "It's odd that the addict turned to the drug for \"Charlotta\", but I suppose it fits. Escape is the goal."

    stop sound fadeout 0.8
    "I find the door with the deer's skull in no time."
    extend " I don't need heightened senses to sniff out the drug. The scent creeps through the door, and I imagine it's going to be overpowering inside..."
    "I consider my options. I could kick down the door and start swinging, but some of his clients may try to defend their plug."
    extend " Not that I couldn't handle them, however I mustn't take risks with another vampire around."
    "Christoph will probably figure out what I am with a glance.\nI could slip in, or..."
    extend " I can face him head on and see why he has such a hold over me." with vpunch
    
    play sound sfx.knock_and_open
    pause 1.8
    show villager with dissolve

    "An elf, with the grace and dexterity of a three legged horse, meets my gaze."
    extend " He's trying so hard to be intimidating. He'd break like glass if he tried to attack me. He's so skinny, I can see his skeleton."
    "I can probably guess what his wages are paid with..."

    m "Who are ya?"

    gr "I heard I could find paste here. I would like to indulge."
    
    m "...Ya don't look like one of us. Where'd ya get the cloak?"
    
    gr " Not all addicts are bottomfeeders. Some of us can {i}control{/i} our use."
    
    m "Hmph! Follow me."

    window hide

    scene background christoph house with Dissolve(0.8)

    play sound sfx.door_open

    stop music

    play music bgm.something_amiss fadein 0.8

    pause 1.0

    window show
    "I almost pity just how simple he is. I wonder if he knows what plane he's on now. Christoph should consider a sober watchhman next time."
    "He doesn't confiscate my weapons. They're out of sight, but any decent guardsman would search me at least."
    "The house is cramped. Not because it's small, but because of the mess."
    "The place is bereft of homely items such as furniture.\nInstead, it's filled to the brim with trash such as empty bottles, cigarette butts, and general junk."
    "I expect rats and vermin to scurry across my boot with each step I take.\nI see a hallway leading back to what I guess is a bedroom, barricaded by more trash."
    "The \"residents\" weren't much better off."
    extend " Several disheveled men and women sit in a circle, ogling at whatever fantasy they were trapped in."
    "How has this place not been searched sooner?\nEven if the Celestials have their hands full, where are the city guards?"
    "Hmm, I wonder how many of them are in this circle? Or have been bribed?\nMortals are weak in the face of sinful temptation, after all..."

    show christoph happy at christoph_normal_range with dissolve:
        center
    "I'm escorted past them to a sickly green goblin lounging in a chair too regal for this dump. This must be my prey."
    extend " He looks up at me and grins, jagged teeth meeting my eyes."
    "My heart pounds. As I predicted, I've met him somewhere. But when?"

    ch "Well well, what have we here?"

    m "He claims he wants to buy."
    
    show christoph happy at christoph_normal_range:
        hop
    ch "Yes, yes, buy a lot more than my average customer, I'm assuming."
    extend "\nHehehehe, to whom do I owe the pleasure for his patronage."
    
    gr "My name is of no importance to you."

    play sound sfx.coins
    show christoph happy at christoph_normal_range:
        hop
    ch "Oooooh!!!"

    "I slap down a sack of coin, much more than I paid the smith."
    "The goblin's eyes expand. This must be more money than he's ever seen in his life. I see a long, slender tongue lick his lips."
    
    show christoph happy at christoph_close_range with dissolve:
        center
    "I take the time to examine him. He lacks the traits I do, and I'm {i}certain{/i} my tongue isn't as hideous..."
    "His entire body is lanky, emaciated, yet doesn't appear hindered." 
    extend "\nHis long fingers tenderly toy with their spoils, each equipped with grisly nails at their tips. Whatever he is, we're not the same."
    "My chest grows heavier."
    extend "\nI can't pinpoint when or where I've encountered Christoph. This amnesia is beginning to irritate me..!"
    "But he doesn't appear to recognize me either."
    show christoph happy at christoph_close_range with dissolve:
        flip
    extend "\nHe reverts his gaze from his spoils, flashing a toothy smile."


    show villager at left with easeinleft:
        zoom 0.8
    ch "Start him off. We're having him over for the night.\nIt is our duty to cater to our guests~."
    
    m "Hmph."

    hide christoph with quickblinds
    show villager at left with easeinleft:
        zoom 1.2
    "The elf takes a a wad of paste from his pocket and dumps it into my hands."
    "I shouldn't be surprised but I'm repulsed all the same. Ishmael knows what else lies in those breeches."
    extend " Though addicts rarely care..."
    
    hide villager with moveoutleft
    "If I use, I will hallucinate but not be incapacitated."
    extend " \nMy cravings have evolved to blood, and paste is now only a recreation rather than a hindurance."
    "Perhaps I can use it to tap into my memories, help me decipher why this fiend matters so much to me."
    
    play sound sfx.zap
    camera at invert_camera
    "I reach for my hatchet. The thought of hurling it at the goblin's head causes my hand to twitch."

    camera at revert_camera
    extend " As expected, violence is off the table.\nFor now..."

    show christoph happy at christoph_normal_range with easeinright:
        right

    ch "Go on, take a whiff. You have the entire night. No need to hurry."

    gr "..."
    extend "Who are you?"
    
    show christoph neutral at christoph_normal_range with easeinright
    ch "Eh?"
    
    gr "I feel like we've met somewhere."
    show christoph neutral at christoph_normal_range
    ch "Perhaps we have. My business isn't appreciated. I've become a wanderer of sorts. I've been at this for several years now."
    show christoph happy at christoph_normal_range
    extend " Though... I feel as if we've met as well. Mayhaps you were one of my earlier clients?"
    
    gr "Hmm. I have used for a long time... It isn't impossible."
    extend "\nSay, if I were to help you, where would I go to acquire more paste?"
    
    show christoph happy at christoph_normal_range:
        hop
    ch "Hahahaha, an opportunist! I respect that, but I think we should get to know each other more first."

    show christoph happy at christoph_close_range with dissolve:
        center
    "He too, pulls out a wad of paste."
    extend " Would he be debilitated by snorting it? Many see goblins as feral, and he indeed looks well past having humanity."
    extend " Either way, I need to play along."
    "I lift the paste to my nose and inhale deeply."

    show christoph happy at christoph_close_range:
        hop
    ch "Yes! {b}YES!{/b} That's more like it!" 

    "I only witness him indulge before my vision grows hazy."
    extend " Ugh, no wonder this stuff is addictive. It acts quicker than I remember. If I were still mortal, I'd be beyond helpless."

    hide Christoph
    scene image "#000" with pixellate
    stop music fadeout 0.8
    "The world shifts. It's as if I'm traveling to a new reality. The dank smell and dirty flooring leave my senses."
    extend " I shudder. This is the feeling of flight I had craved long ago."
    "I hate it!" with vpunch
    "But I know how this drug works. It pulls us into our deepest desires.\nAnd with my awareness, maybe..."

    gr "Who is Christoph?"

    "Damn, even though I'm conscious, I have little control over what I witness."
    extend " This drug is truly insidious. I'm vulnerable, both in my body and my mind. I can only hope Christoph is just as incapacitated."
    "Yet I perservere. Perhaps if I keep my mind on Christoph, I can at least learn something."

    gr "Who are you, goblin?"

    w "Christoph, can you fetch the firewood? Let's get a roaring fire going!"

    "I still see nothing, but can hear voices now."

    ch "But it's sooo cold outside. Can you do it this time?"
    
    w "Hehe, you asked me the same thing last time. And besides, fire is so breathtaking isn't it?"
    
    "Ahh, this must be his mother."

    ch "Ugh, but I'm so tired..."

    w "So am I. You'll understand when you have kids. Now hurry alone~."

    ch "Fine..."

    window hide

    scene background forest with Fade(0.7, 0.8, 0.7, color="#fff")

    pause 1.0

    window show
    "I am now standing outside a window. They don't see me."
    "My mouth waters. Both of them look so scrumptuous!\nAnd I've heard the blood of a child is {b}DIVINE!{/b}"
    "It'll be so easy. This foolish mother is trusting him outside as the sun sets. She {b}deserves{/b} to lose him." 
    extend " Later I'll feast on her too as punishment."

    gr "(Ngh...these thoughts aren't my own. Is this the drug's handiwork too?)"

    play sound sfx.door_open

    play music bgm.lethal_suspense fadein 0.8
    show villager at center:
        zoom 0.8
    "The young goblin tuggling on his fur jacket, shambles outside."
    extend " Being of the forest, their eyes are more accustomed to the dark. But so are mine."
    "I leave the window. Trailing him is child's play.\nHe doesn't even look over his shoulder. A wolf could pounce on him at any moment."
    extend " How fortuitous for me!" with vpunch 

    play sound sfx.rustle
    queue sound sfx.rustle
    queue sound sfx.rustle
    "I dart from tree to tree, waiting for him to find his firewood.\nAs he does, he devotes his focus to gathering it. My mouth waters."
    "He bends down and I arch forward, eager to pounce."

    play sound sfx.mana_charge
    with maliceflash
    extend " My muscles brace as my Malice flows."
    extend "\nHe is {b}MINE!{/b} His feeble matron can't save him, even if she was here!"
    "My mouth waters, eager to taste his delectable blood.\nMy thirst is overwhelming! I cannot wait!!!"
    extend "\nI inch forward. In Three..."
    extend " Two..."

    window hide #simulates a pounce
    play sound sfx.weapon_swingh
    show villager at center:
        zoom 1.5 ypos 1.3
    pause 1.0
    camera at revert_camera
    stop music
    window show
    gr "(I've seen enough.)"

    window hide

    play sound sfx.glass_shatter
    scene background christoph house with Fade(0.7, 0.8, 0.7, color="#fff")

    window show
    
    "Like glass, the illusion shatters. I'm now back in Christoph's den."
    extend " I guess since I channeled mana, I must've been able to break free of its grip."
    "I understand now. Christoph is the only prey I've ever spared.\nAs I sank my fangs into him that day, I realized just how low I had sunk."
    "Shortly after, a band of Celestials stormed the house.\nThey must've heard his mother's screams."
    extend " I didn't resist. I was to be burned for my heinous offense, and then I met Nick."
    "He convinced me to put my instincts to good use, and that I would be able to feed as much as I wished. I accepted."
    "My sin is irredeemable. Only Hell or oblivion await me in the afterlife."
    extend "\nI have no regrets. Tis a fitting end for someone like me."

    w "Ngh, what are you doing?!" with vpunch
    
    show christoph angry at christoph_normal_range:
        center
    ch "Sniveling wretch! You know what happens if you cannot pay!" with vpunch

    "I see an enraged Christoph pinning one of the addicts to a wall."
    extend "\nI grab my hatchet, my resolve somewhat restored. It's not an intent to save her that drives me. She put herself in this position."

    call screen image_display("vfx/sword_swing.png")
    play sound sfx.hurl
    queue sound sfx.slash 
    with quickblood

    ch "{size=+80}{b}GRAHHHHH!!!!{/b}" with vpunch 

    "Christoph, however, is another matter."
    hide christoph with quickblinds
    extend "\nHe recoils, the gash on his cheek painting his hand crimson.\nHis feral eyes lock on mine and he snarls."

    show christoph combat angry at christoph_normal_range with quickblinds:
        center
    ch "How dare you! What is she to you?!" with vpunch
    
    gr "No one. But this is over, Christoph."

    play music bgm.reckoning_I fadein 0.8
    play sound sfx.drop_clothes
    "I throw off my cloak, revealing my dark red breastplate."
    extend "\nTheir stupor prevents the denizens from descending into fright.\nOur occupation is one that inspires terror."
    play sound sfx.door_open
    "Christoph's pet elf bolts for the door, and the goblin's anger only grows stronger."
    extend " His bony face, twisted in both pain and rage, turns to mine."

    jump confrontation

    return