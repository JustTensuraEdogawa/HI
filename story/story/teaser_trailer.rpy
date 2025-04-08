label teaser_trailer:
    scene black
    with dissolve_scene_full

    "..."
    "The time... {w=2.0}{b}has come.{/b}"

    scene bg club_day
    with wipeleft_scene
    play music t100

    show kotonoha toward happ b1e om lchest at t21
    show monika forward anno at t22
    kt "Oh? I'll show you how to be a better girlfriend to [player]."
    m 5b "You're on!"
    kt ce "I'll join your Literature Club and prove to you that I can run the debate club and be a member of your club!"
    "Is she really doing this for me?"
    "I love her already!"

    scene bg residential_day
    with wipeleft_scene
    show sayori 4bh at t32
    $ s_name = "Sayori"
    s "Hey, [player]..."
    s "Are you really sure about this?"
    mc "Yes, I am."
    show sayochi 4bh at t31
    sc "Yeah, my beloved [player]."
    sc 4bi "I'm not really confident about this idea..."
    mc "Just trust me, okay?"
    sc 4bl "Oooookay, I trust you!"
    s 4bj "Sister, don't embarass him."
    show sayochi 1bx at s31
    sc "Awww..."
    show sayori 4ba at t32
    show sayochi 1ba at t31
    show sayozuki 4cg at t33
    sz "I'm really worried about all of us..."
    sz "Love, can you really take all 3 of us out on a date?!"
    mc "Of course!"
    mc "I love all of you, so I should be taking you all out."
    mc "If only the others aren't busy today, I'd be dating {i}all{/i} of you."
    sz 2cn "Whatever you say, [player]-chan!"
    s 4bj "Mom!"
    sz 2ck "I just wanna have fun..."
    show sayori 1br at t32
    show sayochi 1bl at t31
    show sayozuki 1ce at t33
    "We all laughed together."

    scene bg bedroom
    with wipeleft_scene
    show mizumi 1a at t21
    show sayo 4d2 at t22
    "For the first time after Mizumi crushed her soul in gaming, she won."
    sy "Take that L, Big Sis Mizumi!"
    sy "You're soooooo sigma!"
    sy "We can go looksmax at our house with Big Sis Sayori!"
    sy "I would love to show you my skibidi collection of cool stuff!"
    sy "It will make you edge real hard!"
    mi 1g "Cool!"
    mi "I would love you to show me your cool stuff!"
    sy "[player], you can come too, my baby gronk!"
    mc "I would love too my livvy dunne, Sayo!"
    sy 4z2 "HeheheheheHAHA!"

    scene bg corridor
    with wipeleft_scene
    show himari 1h at t21
    show yuri 1a at t22
    h "[player]! We have a surprise for you in the Literature Club!"
    mc "Oh really, Himari?"
    y 1d "Yes, our love."
    y "Let's go to the club now."
    mc "Wait--"
    "Himari and Yuri dragged me to the clubroom."

    scene bg club_day
    with wipeleft_scene
    show canonmc turned happ om at t11
    cmc "Hello!"
    cmc "It's so nice seeing you."
    cmc "You're the one controlling me throughout this game, right?"
    cmc cross happ om "I'm gonna say..."
    cmc "Thanks for guiding me throughout Seasons 1 and 2."
    cmc "You have helped me get {i}all{/i} my girlfriends."
    cmc cross worr blus mc "Even though it's becoming challenging to handle all of them..."
    cmc turned happ om ce "I love all of them!"
    sy "Big Sis Sayori, it's my baby gronk, [player]!"
    show canonmc turned shoc om oe at h11
    s "[player]?"
    n "Let's get him!"
    h "We missed him so much!"
    m "Literature Family, Roll out!"
    cmc "Yikes!"
    cmc "I would like to chat with you longer, but I have to go!"
    cmc mc "Bye!"
    show canonmc at lhide
    hide canonmc 
    pause(1.0)
    show sayo 1a at r31
    show sayori 4a at r32
    show sayochi 1 at r33
    pause(1.5)
    s "No time to waste!"
    show sayo at lhide
    show sayori at lhide
    hide sayo 
    hide sayori
    show sayochi 1a at t32
    pause(0.5)
    show sayochi 1x at s32
    pause(0.5)
    sc "Hah, hah, hah, Wait for meeee!"
    show sayochi at lhide
    hide sayochi 
    pause(1.0)
    show yuri 1a at r41
    show amy 1a at r42
    show cara 1a at r43
    show natsuki 1a at r44
    pause(1.0)
    show yuri at lhide
    show amy at lhide
    hide yuri 
    hide amy 
    pause(0.5)
    c 1f "Natsuki, let's go get [player]!"
    hide natsuki 
    play sound "mod_assets/sfx/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show ssnatsuki 1e zorder 4 at h44
    ssn "He wont escape this time!"
    show cara at lhide
    show ssnatsuki at lhide
    hide cara 
    hide ssnatsuki 
    pause(1.0)
    show mizumi 1a at r21
    show sayozuki 1bj at r22
    sz "[player]-chaaaaaaan!"
    mi 1f "I can see in the future that he goes in that room to hide..."
    mi 1g "Ms.Sayozuki, let's go!"
    show sayozuki at lhide
    show mizumi at lhide
    hide mizumi 
    hide sayozuki
    pause(1.0)
    show monika 1b at r21
    show himari 1a at r22
    pause(1.0)
    m "He's too fast..."
    m forward happ om oe lpoint "But no worries!"
    $ run_input("os.set_speed(characters/mc.chr) = 3", "Successfully set.")
    m 1b "Now we can catch him!"
    hide screen console_screen
    h 1zzzh "[player], here comes your girlfriends!"
    show monika at lhide
    show himari at lhide
    hide monika 
    hide himari 
    pause(1.5)
    call screen dialog("It should've been me, not him! It's not fair!.", ok_action=Return())
    pause(1.0)
    t "Now, now, It's okay."
    t "But anyways, Hi, Modder here."
    t "Since you're watching this, I'm assuming you played Seasons 1 and 2 of my mod."
    t "All I'm going to say is..."
    t "Thanks for playing my mod!"
    t "There will be {i}more{/i} in here than what you just saw."
    t "Expect more girlfriends, more story, and more craziness!"
    t "See you when this mod's released!"
    t "Ta-ta and farewell!"
    return
