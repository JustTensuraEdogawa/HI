label missing_bow:

    $ s_name = "Sayori"
    $ sc_name = "Sayochi"
    $ sz_name = "Sayozuki"
    $ sy_name = "Sayo"

    scene bg lroom
    with dissolve_scene_full
    "It's a normal morning..."
    "Until I received a call..."
    mc "Hmm?"
    "I gently answered the phone."
    s "Help me, [player]!"
    mc "How can I help you, Sayori?"
    s "My bow... It's gone!"
    mc "..."
    mc "Alright, Sayori. I'll come over."
    "Sayori lost her bow?"
    "I need to help her find it then..."
    scene bg sayori_bedroom
    with wipeleft_scene
    mc "Sayori? Where are you?"
    play music sm
    "I see a girl knelt down, looking for something."
    "She looks a little similar to Sayori..."
    show sayori turned no_bow casual cry om at t11 
    s "[player]..."
    show sayori lup rup mj at face 
    play sound fall
    s "I lost my bow..."
    mc "Excuse me... do I know you?"
    show sayori rdown vang om at t11
    play sound "sfx/slap.ogg"
    s "You meanie, it's me, Sayori!"
    show sayori ldown e1g mj at t11 
    mc "Oh, right, sorry."
    mc "I couldn't recognize you without the bow..."
    show sayori tap casual no_bow angr om e3 at s11 
    s "Here I am crying because I lost my bow, and there you are... insulting me with your not so funny jokes..."
    show sayori m2 e4 at t11
    mc "Sayori..."
    mc "I'm sorry, ok?"
    s "..."
    s e2 "Hmph..."
    mc "..."
    "I made her feel bad."
    mc "Alright, Sayori... I'll help you find it."
    show sayori pout cm at t11
    "She looks at me rather upset."
    s om "Please don't do that again."
    s "I demand a {i}lot{/i} of cookies for that."
    mc "Yes, Sayori."
    s turned casual no_bow happ om "Okay!"
    s sad om "But my bow..."
    mc "We'll find it."
    mc "Also..."
    mc "Can you just make another bow?"
    s neut om "I mean, I can."
    s sad om "But that bow has {i}sentimental{/i} value to me."
    mc "Alright."
    mc "I'll help you find it."
    show sayori sad mb at t11 
    s "Thanks, [player]."
    show sayori at thide
    hide sayori 
    "We started to look for her bow..."
    "We can't find it here in her room."
    mc "Sayori, where did you last... remove your bow?"
    s "I only remove my bow when I'm taking a shower..."
    mc "Well, we better look for it in there."
    scene bg shower 
    with wipeleft_scene
    s "I'm going in first."
    mc "I'm... not going in there with you."
    "Sayori went inside the showers."
    s "... Aw... I can't find it here!"
    s "[player]... care to help me..?"
    mc "What? I'm not going in there..."
    s "But you said..."
    mc "It's just weird..."
    s "You don't have to feel weird about it~"
    "She dragged me in the compact shower."
    mc "Ahhhh!"
    play sound fall2
    "I stumbled upon her as she dragged me in."
    mc "Geez, it's so cramped in here..."
    s "Let's find my bow."
    mc "Alright..."
    "After a few more minutes of searching, they found nothing."
    mc "It's not here either, Sayori."
    s "That can't be..."
    mc "You may have misplaced it somewhere else."
    s "My bow..."
    "Sayori starts to sniffle."
    mc "We're gonna find it, okay?"
    mc "But we need to get out of here first..."
    stop music fadeout 2.0
    "I started to open the door handle."
    "..."
    "It's stuck?!"
    s "What's going on?"
    mc "The door is stuck."
    play music t7
    s "Wait, what?"
    mc "I can't open it!"
    "I tugged harder on the door handle..."
    "It won't budge!"
    s "I'm sorry, [player]."
    mc "..."
    mc "It's okay, Sayori."
    mc "Maybe this is the punishment I get from teasing you."
    mc "We're stuck here until someone opens the door for us."
    mc "Wait..."
    mc "Can you bust us out of here?"
    s "I'm still new to Monika's console."
    s "So no."
    mc "Damn..."
    mc "Well, I guess we have to wait."
    mc "Let's sit down for a while."
    stop music fadeout 2.0
    "I sat down besides Sayori."
    mc "Geez it's so cramped in here."
    "After a few moments of silence, Sayori started to speak."
    s "[player]..."
    show sayori turned no_bow casual sad om at t11
    play music t9
    s "I'm sorry for being troublesome."
    mc "No, it's okay."
    show sayori ma at t11
    "Sayori smiled."
    s mb "That bow... was the only memento my father left me."
    show sayori ma at t11
    mc "Your father?"
    s mb "Yeah. Before he went to get milk."
    s om "So you see..."
    s e1b "My father bought that bow for me when I was a kid."
    s mc "I really love wearing that bow."
    s oe om "If I don't wear it, I feel like a big part of me is missing."
    s "[player]..."
    s cry om "I don't want to lose the {i}only{/i} remembrance I have of him..."
    s "Please help me find it!"
    show sayori cm at t11
    mc "..."
    mc "We'll find it, no worries."
    mc "If we get out of this bathroom."
    s nerv om "...Yeah."
    stop music fadeout 2.0
    show sayori at thide 
    hide sayori 
    "We sat there in the bathroom for {i}hours.{/i}"
    mc "Sayori?"
    play music t9
    show sayori turned casual no_bow om at t11
    s "Yes, love?"
    show sayori cm at t11 
    mc "How are you feeling right now?"
    s om "What do you mean?"
    show sayori cm at t11
    mc "You said you were... depressed."
    s worr om "Oh."
    s mc "Yeah."
    s sad om "But I already told you, [player]."
    s mb "Being by your side, my boyfriend who loves me so much..."
    s e4e lup rup "No amount of depression can surpass the happiness that I experience being with you."
    show sayori e1h at h11 
    s "I really, really, really, really love you, [player]!"
    show sayori e4e ma at face 
    play sound fall 
    "Sayori hugged me."
    mc "Sayori..."
    "I'm going to enjoy this moment with her."
    "Until she pushed me with her body, causing me to step on a soap which is conveniently in the ground."
    mc "Wait-- aaaaah!"
    hide sayori 
    stop music 
    play sound fall2
    "As we fell, I accidentally turned on the shower faucet."
    "Water is spraying on the both of us."
    mc "Sayori!!!"
    s "Sorry... ehehe~"
    mc "We're both wet now."
    s "That could mean... two things~"
    mc "What the..."
    play sound closet_open
    sy "I need to take a dump..."
    sy "..."
    show sayo 1bm at t11
    play music t7 
    sy "Big Sis? [player]?"
    sy "Are you doing a private goon sesh here?!"
    mc "Uhh..."
    sy "Mom! Big Sis Sayochi!"
    sy "[player] and Big Sis Sayori is in the bathroom all wet!"
    stop music fadeout 2.0 
    show sayochi turned casual eb mh at t31 
    show sayozuki 1am at t33 
    sc "[player]! Sister!"
    sz 1ag "Are both of you okay?"
    mc "We're fine, Ms. Sayozuki."
    play music sm 
    show sayozuki 1ah at t33
    show sayochi mc bb lpoint at h31 
    sc "That's very sneaky, Sayori!"
    sc "You're getting most of [player] all to yourself!"
    show sayori turned casual no_bow nerv om at t44
    show sayochi ma at t41 
    show sayo 1bo at t42 
    show sayozuki at t43 
    s "As much as I want to do that..."
    s "No worries, It's just an accident."
    s "[player] was helping me look for my bow..."
    s sad om "We still couldn't find it though..."
    sc ba mg ldown "Your bow?"
    sc "Didn't you left your bow in the washer because it was dirty when it fell one time?"
    show sayochi md at t41
    show sayori curi cm at t44 
    s "..."
    show sayori vsur lup rup om at h44 
    s "Wait, I rember now!"
    s tap casual no_bow happ om "Silly me, [player]."
    mc "..."
    mc "Seriously Sayori?"
    mc "Anyways..."
    mc "I need to change..."
    show sayochi ea nc at t41 
    show sayo 1be at t42 
    show sayozuki 1ar at t43 
    show sayori turned casual no_bow blus at t44
    "They suddenly changed their look towards me."
    mc "..."
    "I think I need to get out of here."
    play sound it
    show sayori vsur om b1a lup rup nobl at h44 
    s "He's getting away!"
    sy 4be2 "Let's chase our baby gronk, everyone!"
    e "Yeah!"
    show sayochi at lhide 
    show sayo at lhide 
    show sayozuki at lhide 
    show sayori at lhide
    hide sayochi 
    hide sayo 
    hide sayozuki 
    hide sayori 
    "And they are chasing me."
    "Great."
    stop music fadeout 2.0
    scene bg bedroom
    with wipeleft_scene
    "Phew."
    "I still managed to get away."
    "I need to change my wet clothes real quick."
    "I went to the showers and took a quick shower, then changed clothes."
    "Suddenly, I heard a knock on my door."
    "I... wonder who that could be."
    play music sm 
    scene bg house
    with wipeleft_scene
    "Oh it's Sayori."
    "She's alone."
    "Is she still gonna chase me?"
    show sayori tap happ casual om at t11 
    s "Sorry about earlier."
    s "I wouldn't have known that I put my bow in the washroom."
    mc "Well..."
    mc "I'm just glad that you found your bow."
    mc "You don't have to worry about it."
    s turned happ om lup rup "I promise I'll make it up to you, ok?"
    mc "Okay, Sayori."
    mc "I'll be looking forward to that."
    show sayori ce cm blus at face 
    play sound fall
    "I hugged her."
    s e1f om "Thanks for your help."
    s oe om "I enjoyed the time you gave to me today."
    s ce "I love you!"
    mc "I love you too."
    show sayori oe cm at t11 
    mc "See you in club!"
    s lup om "Sure, [player]."
    show sayori at thide 
    hide sayori 
    "She went to her house."
    "..."
    "Whew, this day is really something."
    "I'm looking forward to things like this happening to me."
    scene black
    with dissolve_scene_full

    return

