label chapter_seven:

    play music m1

    "I hear Renpy-sama chanting some sort of weird chanting spell or something."
    r "{b}Three days later...{/b}"
    "I approached him."
    r "Oh hello, [player]."
    mc "Hi, Renpy-sama."
    r "Now you have 8 girlfriends."
    mc "Yeah..."
    mc "And long time no see to you."
    r "Yeah."
    r "The Modder wanted me to narrate time cards."
    r "So I'm taking on that job."
    mc "Oh."
    mc "Well, I don't know what to say to you."
    mc "Good luck, I guess?"
    r "I'm about to say that to you to be honest."
    r "I'm pretty sure Mizumi already warned you."
    mc "About what?"
    mc "The Literature Club in shambles?"
    r "Yes."
    mc "We prevented that already."
    r "That's not how it works."
    r "Yes you prevented what should happen in the future."
    r "But this is a different timeline already."
    r "Different timelines are sometimes identical to the main timeline."
    r "There are only slight differences with what happened."
    r "So pretty much, the Literature Club could still going to be in shambles."
    mc "Oh..."
    mc "But hey."
    mc "I'll take that slight difference."
    mc "If that slight difference saves the Literature Club, then I'll be happy."
    mc "If that saves all my girlfriends, then I'm happy."
    r "Alright, [player]."
    r "Time to wake you up, I guess."
    r "Hopefully you can handle all of this."

    stop music 

    scene bg bedroom
    play sound fall

    "I woke up."
    mc "Mizumi?"
    "She woke up as well."
    mi "Yes, my love?"
    mc "We need to get back to the present."
    mc "The Literature Club could still be in jeopardy."
    mc "I dreamt about it."
    mi "Oh..."
    mi "Yeah."
    mi "Let's check and see them."
    mi "Let me get my uniform..."
    mi "Alright."
    show mizumi 1a at t11 
    mi "Hold my hand, [player]."
    mi "Here we go."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause (2.0)
    hide screen tear
    show bg ts
    "We are back in the time stream."
    mc "I'm still worried."
    mi "They're going to be fine."
    mc "I hope so."
    mi "And now here we are."
    show bg residential_day
    with dissolve_cg
    play music t2
    "We arrived at our residential area."
    mc "Let's head straight to club."
    mc "We're late, we already skipped school."
    mi 5i "Sorry, [player]."
    mi "It takes a while traveling across the time stream."
    mi 3b "But hey, let's head there!"
    show mizumi at thide
    hide mizumi 
    "We headed straight to the school."
    
    scene bg corridor
    with wipeleft_scene

    stop music fadeout 2.0
    "As we approached the clubroom, Sayori greeted us."
    show sayori 1a at t11
    s "Oh, [player]! Mizumi! You're back!"
    s 1r "Perfect timing!"
    s 2x "I was just about to inform you that the clubroom changed location!"
    mc "Eh?"
    mi "Changed location?"
    s 4r "Yeah!"
    mc "O-okay."
    "Something's off here."
    show sayori 1x at f11 
    s "Come, follow me, [player]!"
    s "You too Mizumi!"
    show sayori at thide
    hide sayori
    "We dejectedly follow Sayori across the school and at the end of the corridor - a section of the school I never knew about, only because it's so unused it's almost like it's abandoned."
    "Sayori, full of energy, swings open the classroom door."
    scene bg club_day
    with wipeleft 
    show sayori 4x at l41 
    s "Hey everyone, [player] and Mizumi's here!"
    play music t3
    mc "Sayori what is going on--"
    "And I knew it."
    "Something is {i}totally{/i} off."
    show cara 1a at t21
    show natsuki 1a at t22
    c "Hello, [player]! Hello Mizumi!"
    show natsuki 1d at f22
    n "Welcome to Literature Club 2.0!"
    show natsuki 1a at t22
    show cara 1b at f21 
    c "I'm glad you chose us."
    show cara 1a at t21
    mc "Chose... you?"
    mi "Literature Club... 2.0?"
    "And there is the thing."
    c 3u "Oh... About that..."
    show cara 3m at t11
    n 5k "Didn't Sayori explained everything to you?"
    mc "Um... No?"
    n 5y "And she called herself President..."
    mc "W-w-w-wait... President?"
    n 1k "Yes."
    n "She's the president of this club."
    mc "Mizumi, did we get lost in a different timeline?"
    mi "No!"
    mi "I'm pretty sure this is still our own timeline."
    mc "Where's Monika and the others?"
    show cara 1h at f21
    c "Hey! The word or name 'Monika' is banned in this club."
    c "Choose your words, or we'll kick you out."
    n 5d "Yeah! And I mean literally."
    mi "What?"
    show sayori 1x at t31
    show cara at t32
    show natsuki 5a at t33
    s "Soooo, Natsuki my Vice President, Hows the cupcakes going?"
    n "All ready, Sayori."
    stop music fadeout 2.0
    mc "Sayori, let's talk."
    s "Eh?"
    s turned ce anno mg "Oh... fine."
    s oe mi "Let's have a chat here..."
    scene bg class_day
    with wipeleft_scene
    "Mizumi and I followed Sayori towards her desk."
    show sayori turned anno oe cm at t11
    mc "Care to explain what's going on?"
    show sayori turned ce anno mg at s11
    "She let out a deep sigh, then spoke."
    show sayori 1h at f11 
    s "The Literature Club... split."
    mc "What?"
    mi "I thought we had dealt with that?!"
    s 1l "I thought so too."
    show sayori 1v at t11
    s "But Monika is just a meanie."
    show sayori 1w at f11 
    s "She called out Cara and Natsuki not doing literature related activities..."
    s "Which is sparring."
    s "But I knew for a fact that they read Manga before doing their sparring session."
    s "I stood up for them as Vice President."
    s "But..."
    s "Monika didn't listen to me."
    s "I said they already read manga before sparring."
    s "I don't know if she's on her... {w}{i}you know...{/i}"
    s "But it escalated quickly."
    s "Natsuki started to argue and used pretty harsh words towards her."
    s "Monika was contemplating to use her God powers or something..."
    s "But she chose to indefinitely suspend both."
    s "I was annoyed by it."
    s "So I said, I'm going with them, form a literature club of our own where we can express ourselves freely."
    s "Monika didn't stop me."
    s "She just sighed."
    s "[player]..."
    s "Have I done anything wrong?"
    

