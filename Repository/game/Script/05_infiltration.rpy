
label infiltration:

    play sound sfx.footsteps_snowf fadein 0.8 loop
    hide celestial 
    hide villager
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

    #show Christoph happy
    #Sprite is in development. Will be added later. Ragyuo, feel free to use whatever
    "I'm escorted past them to a bluish green goblin lounging in a chair too regal for this dump. This must be my prey."
    extend " He looks up at me and grins, jagged teeth meeting my eyes."
    "My heart pounds. As I predicted, I've met him somewhere. But when?"

    ch "Well well, what have we here?"

    m "He claims he wants to buy."
    
    ch "Yes, yes, buy a lot more than my average customer, I'm assuming.\nHehehehe, to whom do I owe the pleasure for his patronage."
    
    gr "My name is of no importance to you."

    play sound sfx.coins
    ch "Oooooh!!!"

    #hide Christoph moveoutleft
    "I slap down a sack of coin, much more than I paid the smith."
    "The goblin's eyes expand. This must be more money than he's ever seen in his life. I see a long, slender tongue lick his lips."
    "I take the time to examine him. He lacks the traits I do, and I'm {i}certain{/i} my tongue isn't as hideous..."
    "His entire body is lanky, emaciated, yet also agile. His long fingers tenderly toy with their spoils, each equipped with grisly nails at their tips. Whatever he is, we're not the same."
    "My chest grows heavier. I can't pinpoint when or where I've encountered Christoph. This amnesia is beginning to irritate me..!"
    "But he doesn't appear to recognize me either. He reverts his gaze from his spoils, flashing a toothy smile."

    #show Christoph happy
    ch "Start him off. We're having him over for the night.\nIt is our duty to cater to our guests~."
    
    m "Hmph."

    "The elf takes a a wad of paste from his pocket and dumps it into my hands."
    extend " I shouldn't be surprised but I'm repulsed all the same. Ishmael knows what else lies in those breeches. Though addicts rarely care..."
    "If I use, I will hallucinate but not be incapacitated.\nMy cravings have evolved to blood, and paste is now only a recreation rather than a hindurance."
    "Perhaps I can use it to tap into my memories, help me decipher why this fiend matters so much to me."
    #have screen flash inverse tint
    "I reach for my hatchet. The thought of hurling it at the goblin's head causes my hand to twitch."
    extend " As expected, violence is off the table.\nFor now..."

    #show Christoph happy with zoomin
    ch "Go on, take a whiff. You have the entire night. No need to hurry."

    gr "..."
    extend "Who are you?"
    
    ch "Eh?"
    
    gr "I feel like we've met somewhere."
    
    ch "Perhaps we have. My business isn't appreciated. I've become a wanderer of sorts. I've been at this for ten years now."
    extend " Though, I feel as if we've met as well. Mayhaps you were one of my earlier clients?"
    
    gr "Hmm. I have used for a long time... It isn't impossible."
    extend "\nSay, if I were to help you, where would I go to acquire more paste?"
    
    #maybe have sprite bounce once to demonstrate joy?
    ch "Hahahaha, an opportunist! I respect that, but I think we should get to know each other more first."

    "He too, pulls out a wad of paste."
    extend " Would he be debilitated by snorting it? Many see goblins as feral, and he indeed looks well past having humanity."
    extend " Either way, I need to play along."
    "I lift the paste to my nose and inhale deeply."

    ch "Yes! {b}YES!{/b} That's more like it!" with vpunch

    "I only witness him indulge before my vision grows hazy."
    extend " Ugh, no wonder this stuff is addictive. It acts quickly. If I were still mortal, I'd be beyond helpless."

    #hide Christoph
    scene image "#000" with pixellate
    stop music fadeout 0.8
    "The world shifts. It's as if I'm traveling to a new reality. The dank smell and dirty flooring leave my senses."
    extend " I shudder. This is the feeling of flight I had craved long ago."
    "I hate it!" with vpunch
    "But I know how this drug works. It pulls us into our deepest desires.\nAnd with my awareness, maybe..."

    gr "Who is Christoph?"

    "I focus on the image of him. I hone in on the nostalgia, his voice, and anything else that might help me remember."
    "My mind transfigures my thoughts into Christoph's image."
    extend " I see. With enough effort, I'm able to morph these illusions into whatever I fancy.\nIf I wished, I could use this substance to its fullest."
    "But I'm beyond such fruitless endeavors.\nWhat good will these dreams do me outside of now?"

    gr "Who are you, goblin?"

    "The illusions continue to wobble and ripple like water."
    extend " And then I see a green woman with the same ears as Christoph. She too, sparks familiarity within me."

    #I do not know if we necessarily need silhouettes for these two
    w "Christoph, can you fetch the firewood? Let's get a roaring fire going!"

    ch "But it's sooo cold outside. Can you do it this time?"
    
    w "Hehe, you asked me the same thing last time. Now hurry along~."
    
    gr "(Ahh, this must be his mother.)"

    window hide

    scene background forest with Fade(0.7, 0.8, 0.7, color="#fff")

    pause 1.0

    window show
    "I'm now standing outside a window. They don't see me."
    "My mouth waters. Both of them look so scrumptuous!\nAnd I've heard the blood of a child is {b}DIVINE!{/b}"
    "It'll be so easy. This foolish mother is trusting him outside as the sun sets. She deserves to lose him. Later I'll feast on her too as punishment."

    gr "(Ngh...these thoughts aren't my own. Are they related to these memories?)"

    play sound sfx.door_open

    play music bgm.lethal_suspense fadein 0.8
    #show goblin_silhouette at center with dissolve
    "The young goblin tuggling on his fur jacket, shambles outside."
    extend " Being of the forest, their eyes are more accustomed to the dark. But so are mine."
    "I leave the window. Trailing him is child's play.\nHe doesn't even look over his shoulder. A wolf could pounce on him at any moment."
    extend " How fortuitous for me!" with vpunch 

    #maybe we can zoom in one certain parts of the camera to simulate this?
    "I dart from tree to tree, waiting for him to find his firewood.\nAs he does, he devotes his focus to gathering it. My mouth waters."
    "He bends down and I arch forward, eager to pounce."

    #have screen tint red
    extend " My muscles brace.\nHe is {b}MINE!{/b} His feeble matron can't save him, even if she was here!"
    "My mouth waters, eager to taste his delectable blood.\nMy thirst is overwhelming! I cannot wait!!!"
    extend "\nI inch forward. In Three..."
    extend " Two..."

    #revert screen tint
    stop music
    gr "(I've seen enough.)"

    window hide

    scene background christoph house with Fade(0.7, 0.8, 0.7, color="#fff")

    window show
    
    "Like glass, the illusion shatters. I'm now back in Christoph's den."
    "I understand now. Christoph is the only prey I've ever spared.\nAs I sank my fangs into him that day, I realized just how low I had sunk."
    "Shortly after, a band of Celestials stormed the house.\nThey must've heard his mother's screams."
    "I didn't resist. I let them bind and gag me. I was to be burned for my heinous offense, and then I met Nick."
    "He convinced me to put my instincts to good use, and that I would be able to feed as much as I wished. I accepted."
    "My sin is irredeemable. Only Hell or oblivion await me in the afterlife.\nI have no regrets. Tis a fitting end for someone like me."

    w "Ngh, what are you doing?!" with vpunch
    
    #show Christoph angry
    ch "Sniveling wretch! You know what happens if you cannot pay!" with vpunch

    "I see an enraged Christoph pinning one of the addicts to a wall."
    extend "\nI grab my hatchet, my resolve somewhat restored. It's not an intent to save her that drives me. She put herself in this position, after all."

    play sound sfx.hurl
    queue sound sfx.slash 
    with quickblood

    ch "{b}GRAHHHHH!!!!{/b}" with vpunch 

    "Christoph, however, is another matter."
    #hide Christoph with zoomout
    extend "\nHe recoils, the gash on his cheek painting his hand crimson.\nHis feral eyes lock on mine and he snarls."

    #show christoph combat with zoomin
    ch "How dare you! What is she to you?!" with vpunch
    
    gr "No one. But this is over, Christoph."

    play music bgm.reckoning_I fadein 0.8
    play sound sfx.drop_clothes
    "I throw off my cloak, revealing my dark red breastplate."
    extend "\nTheir stupor prevents the denizens from descending into fright.\nOur occupation is one that inspires terror." 
    "Christoph's pet elf bolts for the door, and the goblin's anger only grows stronger."
    extend " His bony face, twisted in both pain and rage, turns to mine."

    jump confrontation

    return