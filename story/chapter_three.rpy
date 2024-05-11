label chapter_three:

    stop music fadeout 2.0
    scene black
    play music m1

    r "Hello, [player]."
    mc "Hi, Renpy-sama..."
    r "So... how was the 6th girlfriend?"
    mc "You almost got me killed!"
    r "Killed?"
    mc "I didn't expect you'd give me a skilled {i}assassin{/i}."
    r "She was an assassin?"
    r "I'm sorry, I thought she was Monika's childhood friend!"
    mc "She is, but yeah, she's an assassin."
    r "Oh, okay."
    r "But hey, I think that's okay to spice things up a bit."
    mc "Yes, I'm okay with that."
    mc "You gave me all of the girlfriends, can't complain."
    mc "I wonder if I can keep up with 100 of them."
    r "You're fine!"
    mc "I hope so..."
    m "Yeah, you're fine, my love."
    "And Monika's here again."
    show monika forward casual happ cm oe at t11
    m "I'll make sure you'll be fine even if you have 200."
    mc "I... don't want to even think about it."
    m e1b b1b "You don't want to be with us anymore?"
    mc "No, no, no."
    mc "I want to be with all of you!"
    mc "I love you all!"
    show monika happ ce om at h11
    m "Yes!"
    m b1b e1d rhip mb lpoint "And I understand too."
    m "It's kinda exhausting to handle all 6 of us now."
    m awkw ce "And yeah, I'm sorry about yesterday."
    mc "Monika, it's okay."
    mc "I just have to adjust."
    mc "I'll be the best boyfriend ever!"
    m e1a blus "Awww~"
    m "Come here~"
    show monika at face
    "I hugged her tightly."
    mc "I love you, Monika."
    show monika at t11
    m "Well, time for you to wake up!"
    m lean happ ce om "See you in the club!"
    m "I love you too!"

    scene bg bedroom
    stop music
    play sound fall

    "BZZT. BZZT. BZZT."
    "I woke up."
    "Time to go to school!"

    scene bg kitchen
    with wipeleft_scene
    play music t2
    
    "I went to the kitchen to get something to eat."
    "As I went, I hear 2 voices."
    "Sounds like their arguing."
    k "Ahhh, Monika, that's not how you do that."
    m "EH?"
    k "You're going to make the taste worse if you do that."
    m "Alright..."
    k "Geez..."
    k "Why are we in here anyways?"
    k "Not that I want to..."
    m "To make breakfast for our boyfriend, silly."
    k "I'm not his boyfriend."
    m "Yeah, right."
    m "After what I heard--"
    k "Monika, stop it."
    k "I-It's just the environment there, OK?"
    m "Whatever you say~"
    "I decided to greet them."
    mc "Hello, girls."
    show ken 1a at t21
    show monika 1a at t22
    m "Hello!"
    k 1u "...Hello."
    "Ken and Monika is in my kitchen, making something."
    "Probably breakfast."
    mc "Good morning to both of you."
    mc "I assume that you want to walk with me to school?"
    m 3j "Of course!"
    k "I'm just here because Monika is here."
    k 2ad "I don't want you to be with her alone."
    k "Not t-that I care about y-you."
    mc "Ken, I'll make myself worthy of Monika."
    k "You'll never be!"
    m forward b3b ce me lpoint "Ken..."
    m 5a "Why don't {i}you{/i} make breakfast for all of us then?"
    m lean happ ce om "And show [player] here how he can be worthy for both of us!"
    k "Me?"
    k 1s "Alright fine!"
    k "I'll show you how to do it, [player]."
    k "And I also get to cook for you Monika."
    show ken at lhide
    hide ken
    "Ken started to work on the kitchen."
    "I sat on the table with Monika."
    show monika at t11
    m "Sooo... [player]..."
    m 1b "I know I said, see you in the club..."
    m "But I came to your house."
    m "I missed you to be honest~"
    mc "It's okay, Monika."
    mc "I missed you too."
    mc "You've been busy yesterday."
    "I held her hand."
    mc "And I thank you for this opportunity."
    play sound "sfx/slap.ogg"
    "My hands we're swatted away."
    k "Watch where your hands are."
    show ken 1ad at t21
    show monika 1a at t22
    "Ken set down the meal she prepared."
    "Mushroom soup."
    "She started to sit down beside Monika."
    mc "Smell's nice."
    k 2r "Of course."
    k "I have to learn how to cook to survive on my own."
    k 1a "After... Monika gave me my life today."
    k "I would've died of starvation back then."
    k 2ab "She then spent time with me, played with me."
    k 4ag "I had no friends before. She was my only friend."
    k 2ad "That's why... I'll be by her side. And protect her."
    k 1f "Why am I sharing this to you?!"
    k "It's none of your business."
    k "Let's just eat, okay?"
    show ken at thide
    show monika at thide
    hide ken 
    hide monika 
    "It was getting interesting..."
    "But I can't push her buttons now."
    "It's getting late for school."
    mc "Ken, you're cooking is very good."
    mc "You'd be a great wife someday."
    k "I-I'm not interested to be a housewife."
    k "No one's going to be an assassin and a housewife at the same time."
    mc "Well I know someone."
    mc "Not in this reality, but in an anime I watched."
    mc "'Family Spy Z'."
    mc "Yin Fordheart is secretly an assassin."
    mc "And she had Leon Fordheart as her husband, who is a spy."
    mc "And they even had an adopted kid, Alina."
    k "D-don't push your logic to me."
    k "I ain't buying it!"
    "Still, she is resilient."
    "We just finished our meal and prepared our way to school."

    scene bg residential_day
    with wipeleft_scene

    "I am currently walking with Monika and Ken today."
    "Sayori seemed to have already left her house."
    "And Yuri, Natsuki, and Cara probably went their own way."
    "Well, as I always say... it's a long walk."
    menu:
        "So It's time to have some fun!"
        "Boop Monika.":
            $ cuffed = False
            "I approached Monika."
            "And booped her in the nose."
            show monika forward b2b e4c ml at t11
            m "Ahhh!"
            show death zorder 4
            k "Serious series..."
            pause(3.0)
            hide death
            hide monika
            show ken 1f at i11
            k "You piece of sh--"
            m "Ken, stop that!"
            show ken at t21
            show monika 1q at t22
            "Monika stopped her."
            show monika at f22
            m "[player], I'm sorry."
            m 4k "I loved your boop!"
            m lean happ cm ce "You're so silly~"
            mc "It's okay, Monika."
            mc "I can tank her hits if I can tank Natsuki's punches."
            show monika 5a at h22
            m "Yeah, right!"
            show ken 1j at f21
            k "Don't do that... again!"
            mc "Ken, I can't do that."
            mc "Or... do you want me to boop you too?"
            show ken 2ai at t21
            k "N-No! Thank you!"
            show ken at lhide
            hide ken 
            "Ken ignored us and continued walking."
            show monika 1l at t11
            m "I'm pretty sure she'll get along with the others..."
            mc "Hope so..."
            mc "Given the fact that she immobilized all of them..."
            mc "But in due time, Monika."
            show monika at thide
            hide monika 
            "We continued our walk."
        "Hold Ken's hand.":
            $ cuffed = True
            "I approached Ken."
            mc "Ken?"
            "I offered her my hand."
            show ken 1j at t11
            k "What will I do with that?"
            mc "I'm offering my hand to hold, milady."
            k 1ad "No, thank you."
            mc "Eh?"
            mc "Okay, I'll hold Monika's hand instead."
            show ken 1r at f11
            k "Give me your stupid hand."
            "She took my hand."
            k 2r "You can't hold her hand."
            k "You're hand is stuck with me!"
            "She pulled a pair of handcuffs and cuffed my hand with hers."
            mc "Hey!"
            k 1s "Now, You can't pull any tricks on me!"
            mc "Geez..."
            show ken at thide
            hide ken
            "My hand is stuck with hers for the rest of the walk."
    "We arrived at the school."
    if cuffed == True:
        "Ken took the key out of her pocket and uncuffed me."
        k "That should do it."
        "He stormed off and jumped to a tree and hid there."
    else:
        pass
    "Ken immediately rushed and jumped to a tree and hid there."
    "I waved goodbye to Monika."
    "Guess it's time for class."

    scene bg class_day
    with wipeleft_scene

    "Class time again."
    "Soon it'll be over and it becomes club time!"
    "There's 2 new members in the club."
    "Cara and Ken."
    "Well I don't know yet if Ken is joining."
    "But if Monika says so and she is one of my girlfriends..."
    "It's fair to say she is."
    "But will they get along?"
    "She really did a commotion yesterday."
    "Hopefully there will be no more chaos in the club."
    "I can't wait to be with them!"
    "And... class is over."
    "Okay let's go to the club!"
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t3

    "I arrived at the club."
    "I saw 4 of my girlfriends already doing their stuff."
    show sayori 1a at t11
    s "Hello, [player]!"
    s 4r "I missed you!"
    mc "I missed you too, Sayori."
    mc "Sorry if I didn't walk with you to school today."
    s 1a "Oh it's okay!"
    s "I have Yuri with me walking!"
    show yuri 1a at t22 
    show sayori 1a at t21
    y "Hello, [player]."
    y "How's your reading?"
    mc "I actually had time to atleast finish a few chapters!"
    show yuri 3d at f22
    y "I'm glad you're still reading!"
    show yuri 2q at t22
    y "Given the fact that you're busy thinking about all of us..."
    mc "Yes, and that's what makes me read it, because I think about you!"
    n "Hey, how about my manga?"
    n "Are you thinking about my manga too?"
    show sayori at t31
    show yuri 1a at t32 
    show natsuki 5d at t33 
    mc "Why, of course I am."
    mc "I am actually still waiting for the next volume."
    mc "You never had a chance to give it to me."
    n 5e "Why didn't you say so?"
    n "I'll go get it for you."
    show natsuki at thide
    hide natsuki 
    "She went back to the closet and looked for the next volume for me to read."
    c "Hello, my love!"
    show cara 1a at t33
    mc "Hi, Cara."
    mc "So how's your first days here in the club?"
    show cara 1y at f33
    c "It was wonderful!"
    c 1f "Sayori and Yuri welcomed me."
    c 1y "And Natsuki's cute demeanor towards me make it even better!"
    n "I'm not cute!"
    show natsuki 4e at t44
    show sayori at t41
    show yuri at t42
    show cara at t43
    "Natsuki is back from the closet, holding the manga."
    n "You want a piece of me again, Cara?"
    c 1a "I'm not backing down on a challenge."
    c 1f "You're on!"
    n "Here, [player]."
    n "Take good care of it or else."
    "She handed me the next volume."
    n "Now, if you'll excuse us..."
    show natsuki at thide
    show cara at thide
    hide natsuki
    hide cara 
    "They both went to the closet."
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "She's at it again."
    show sayori turned b1d rdown mq lup at f41
    s "Just don't break anything!"
    m "Hello everyone! Sorry, we're late!"
    show sayori 1a at t41
    show monika 1b at t43
    show ken 1a at t44
    "Monika and Ken arrived as well."
    mc "Hello, Monika and Ken."
    k 4k "Hi..."
    k "Sorry... for yesterday."
    k 4ai "Sorry to all of you."
    k "I'll join the Literature Club as punishment."
    k "And you can have me do {i}anything{/i} you want."
    k 2z "I'll be your personal butler."
    k 1a "Please be forgiving."
    k "I won't do it again."
    show monika forward b1f e1d rhip mb lpoint at f43
    m "Did you say, {i}anything{/i}?"
    show monika at t43
    show ken 1b at f44
    k "Yes, {i}anything{/i}. Especially if it's you, Monika."
    m lean happ ce om "Well then!"
    m 4b "I would like you to be [player]'s girlfriend!"
    show ken 1j at h44
    k "H-hey, Monika!"
    k "That's not--"
    m "Well you said, {i}anything{/i}."
    m "And I think everyone here will agree to this."
    m 1k "Right?"
    show sayori 4r at h41
    s "Yeah!"
    s 1x "If you'll be a part of '[player]'s Angels', then you'll be pardoned since you are a member."
    show yuri 3m at f42
    y "I don't see a problem with that."
    y 3d "She'll be accepted here is she loves whom we love."
    y "Which is [player], nonetheless."
    show yuri at t42
    show sayori at f41
    s "I'll be able to convince those two as well."
    "Sayori points at Natsuki and Cara."
    s "So.... what do you say, Ken?"
    "Ken looks at me, then the others."
    "There's a moment of silence."
    show sayori at t41
    show ken 1ah at f44
    k "Khhhh, Alright! Fine!"
    k "I'll do it so you can forgive me."
    k "I'll do it for Monika."
    s "Yay!~"
    "All of them laughed except Ken."
    show ken at t11
    show sayori at thide
    show yuri at thide
    show monika at thide
    hide sayori 
    hide yuri
    hide monika 
    k 1ag "Ugh..."
    mc "It's alright, Ken."
    mc "I want you to love me genuinely."
    mc "Not being forced into a corner like this."
    k 2ad "Well..."
    stop music fadeout 2.0
    "She approached me."
    show ken at face
    k "I... kinda felt it anyway."
    k "I'm just... against it because of Monika."
    k 1r "You're not worthy of her."
    k "My mind is telling me to not associate with the likes of you."
    k "Or associate you with Monika either."
    k "But... if your love towards Monika will be as {i}genuine{/i} towards the others..."
    k 4an "Then... I would give you my blessing."
    k "Will you be able to promise me that?"
    mc "Ken..."
    mc "That's a very easy task to fulfill..."
    mc "Of course my love is genuine to {i}all{/i} of them."
    k "H-how about... me then?"
    mc "You?"
    k "Will I also be a part of your love?"
    "And... there we go."
    "Hopefully she changes."
    show black zorder 4 with dissolve_cg
    menu:
        "And of course, my response to her would be--"
        "You're also a part of my love, Ken.":
            hide black with dissolve_cg
            pass
        "You tried to killed me. That love died. We can still be friends though.":
            scene white
            play music t100
            show intro with Dissolve(0.5, alpha=True)
            $ pause(2.5)
            hide intro with Dissolve(0.5, alpha=True)
            show splash_warning "What the heck are you choosing you stupid piece of garbage? I swear to Renpy-sama that I will find you and do ugly things to you, you degenerate being!" with Dissolve(0.5, alpha=True)
            $ pause(2.0)
            stop music
            show black zorder 4
            menu:
                "This is the only choice for you."
                "You're also a part of my love, Ken.":
                    scene bg club_day with dissolve_cg
                    show ken 4an at face
                    hide splash_warning
                    pass
    
    mc "Of course, Ken."
    mc "I can show you how genuine my love towards Monika."
    mc "By making you experience it as well."
    k 4ar "Words ain't convincing to me."
    show ken 1be at t11
    k "You have to show it by your actions!"
    k 1ah "This is embarassing..."
    k 2ad "Monika, are we done here?"
    k "I'm already at my breaking point."
    k 4ai "I just want to curl up and die."
    show ken at lhide
    hide ken
    play music t3
    "Ken rushes off towards Monika."
    m "Alright!"
    show monika 3a at t11
    m "That settles it!"
    m lean happ ce om "Okay, everyone!"
    show monika 3a at t21
    show ken 1a at t22
    m "We now welcome our newest club member, Ken!"
    "All four of us applauded her."
    m 2b "Since you are our newest member, anything literature-related that you'd like to do here?"
    show ken 1b at f22
    k "Maybe I'd like to read some action-filled novels."
    m "Cool!"
    show ken at t22
    m "Come over here near my desk. I think I have the perfect books for you to read..."
    show monika at lhide
    show ken at lhide
    hide monika 
    hide ken
    "They went to the bookshelf near her desk and looked for the books Ken liked to read."
    show sayori 1x at t21
    show yuri 1a at t22
    s "In that case, Yuri and I will be reading together in the corner!"
    s 2x "I'd like to read Portrait of Markov with you Yuri..."
    y 3j "Uh... sure, but are you going to be okay with it?"
    y "It's a whole lot creepy and violent than what you usually read."
    s 4r "I would like some change of pace!"
    show sayori 1l at s21
    s "Just make sure you make it less scary when you storytell it to me."
    y 3m "I'd be more than happy to do so..."
    y "Let's go!"
    show sayori at thide
    show yuri at thide
    hide sayori 
    hide yuri 
    "And with that they went to the corner where Yuri reads her book."
    "..."
    "It seems like everyone is occupied."
    "Of course I want to spend time with all of them!"
    "Sooooo, I have to make a move now."
    
    label club_time_1:

        play music t5

        $ sytime_done = False
        $ cntime_done = False
        $ mktime_done = False
        $ clubtime = 0

        label club_loop:
        if clubtime == 0:
            $ clubtext = "Who should I spend time with first?"
        elif clubtime == 3:
            jump clubtime_end
        else:
            $ clubtext = "Who should I spend time with next?"

        menu:
            "[clubtext]" 
            "Sayori and Yuri." if not sytime_done:
                $ clubtime += 1
                $ sytime_done = True
                call sayori_yuri_time
            "Cara and Natsuki." if not cntime_done:
                $ clubtime += 1
                $ cntime_done = True
                call cara_natsuki_time
            "Monika and Ken." if not mktime_done:
                $ clubtime += 1
                $ mktime_done = True
                call monika_ken_time
        
        jump club_loop

    label sayori_yuri_time:

        "I guess I'll go with Sayori and Yuri."
        "After all, I'm kinda interested with the change of pace Sayori is making."
        "What could go wrong, right?"
        "I mean, Yuri taught her how to cook without setting my house on fire."
        "I decided to approach both of them."
        mc "Sayori? Yuri?"
        y "Oh, hello, our beloved [player]."
        show sayori 1a at t21
        show yuri 1a at t22
        "Sayori and Yuri stopped reading and focused on me."
        show sayori 3x at f21
        s "Hi, [player]!"
        s "I've been listening to Yuri read me the novel."
        s 3r "And it's a different experience!"
        show sayori 1a at t21
        show yuri 3b at f22
        y "She's doing alright, [player]."
        y "I'm trying to narrate the novel to her in the most simplest way."
        y "There are a lot of sophisticated words here that she totally won't understand, so I'm translating that so she can comprehend."
        s 4x "And I didn't understand anything she said!"
        mc "Typical Sayori."
        show sayori turned happ om ce at t21
        show yuri turned happ om ce at t22 
        "All of us laughed."
        "I listened to them as they continue to read the novel."
        y 1l "{i}And as the young woman makes her way to escape, she runs frantically-- erm... she runs in panic towards the exit only to find she is cornered by the group of-- meanies to do sorts of bad experiments again on her.{/i}"
        show sayori 4p at s21
        s "No!!! Don't let the meanies catch you! Fight back!"
        mc "Yuri, you seem to be storytelling to a 5-year old."
        show sayori 4u at t21
        show yuri 3d at f22
        y "It's okay, [player]."
        show sayori tap b2 m4 at t21
        s "Hey, I'm no 5-year old."
        mc "Okay, You're a 4-year old."
        s ce "That's even worse!"
        mc "Just kidding, Sayori."
        mc "You're cuteness and being a ball of sunshine is what's making me love you."
        show sayori turned b1b e1e mb blus lup at t21
        "I gave her headpats."
        show sayori at f21
        s "H-hey~"
        s turned b1f e1d mb blus "I told you that I'll tie you up in your bed tonight if you did it again~"
        show sayori at t21
        show yuri 3p at f22
        y "Tie [player] up?"
        show yuri 4b at s22
        y "I wanna do it t-too..."
        $ style.say_dialogue = style.edited
        y 3y1 "I want it..."
        $ style.say_dialogue = style.normal
        mc "Okay... no one's tying me up."
        mc "I love the both of you. It's nice seeing you read together."
        mc "You wouldn't mind me reading with the both of you, would you?"
        show sayori 4r at f21
        show yuri 3d at f22
        s "No, we wont mind!"
        y "No objections, [player]."
        show sayori at h21
        s "Yeah! the raccoon doesn't mind too!"
        y 3r "For the last time, Sayori. I am {i}not{/i} a raccoon!"
        show sayori at thide
        show yuri at thide
        hide sayori 
        hide yuri 
        "I sat down with them and I pulled out my copy of Portrait of Markov."
        "I read with them and had a great time!"
        "After our reading session, I bade them farewell."

        return

    label cara_natsuki_time:

        "I decided to go for Cara and Natsuki."
        "Hopefully they haven't broken anything yet."
        "I went over to the closet to see how they're doing."

        scene bg closet
        with wipeleft_scene

        show cara 1b at t21
        c "Natsuki, you're strong!"
        c "How are you really strong given your physique?"
        show natsuki 4y at t22
        n "Well it's just about--"
        n 4q "Actually, I don't know why."
        "She really has no idea that she's a Salien, like her dad."
        "I decided to appraoch them."
        mc "Hello my lovely girlfriends."
        "They turned their attention to me."
        show cara 1f at f21
        c "Oh, hi, [player]!"
        show cara at t21
        show natsuki 1l at f22
        n "Hello, [player]!"
        n "You missed me?"
        show natsuki at t22
        show cara 1y at f21
        c "We both know that he misses me more, you know."
        show cara at t21
        show natsuki 4p at f22
        n "Hey, what you say fool?!"
        show cara at f21
        c "It's true!!"
        show natsuki at t22
        show cara at t21
        mc "Hey, hey, I missed both of you!"
        mc "That's why I'm here to spend time with you."
        "I reached out to my bag to get the manga Natsuki lent to me."
        mc "This is a literature club, not a fight club."
        mc "Let's do something literature related, okay?"
        show natsuki 5z at f22
        n "It's about time that you're making the right decision!"
        show natsuki at t22
        "Suddenly I got startled by Cara's reaction."
        show cara 3f at hf21
        c "Is that... 'Parfait Girls'?"
        c "I've been looking to read that since my older sister gave me the 1st volume when I was a child!"
        c "She only had the 1st volume though. I want to read the rest!"
        show cara at t21
        "Natsuki started to flash her teeth."
        show natsuki 5d at f22
        n "Ho, then not to brag, Cara..."
        n 5z "But I have a complete set of this manga!"
        n 5d "Want to read it with us?"
        show cara 1y at hf21
        c "You bet I am!"
        show cara at thide
        show natsuki at thide
        hide cara 
        hide natsuki 
        "We all sat down on the floor as Natsuki grabbed the volume of manga from my hand and started opening the book."
        "We all enjoyed our time as we read page after page."
        "We're so engrossed that we finished the volume in few minutes."
        show natsuki 1a at t22 
        n "Alright. Now we've finished reading..."
        play sound "mod_assets/powerup.mp3"
        show white zorder 4:
            alpha 0.6
            linear 0.25 alpha 0.0
        show natsuki 4d at h22
        n "Cara, where we're we?"
        show cara 1a at t21
        c "Right! Let's continue to spar!"
        show natsuki at thide
        show cara at thide
        hide cara
        hide natsuki 
        "I just can't stop these two from sparring."
        mc "Just don't break anything!"
        mc "Or Sayori will be mad!"
        "I decided to just let them be."
        "I can't stop those two without getting bruises anyway."

        scene bg club_day
        with wipeleft_scene

        return

    label monika_ken_time:

        "Well, I'll go for Monika and Ken this time."
        "Besides I'd like to interact with Ken and get to know her more a little bit."
        "I decided to approach them near Monika's desk."

        scene bg class_day
        with wipeleft_scene

        mc "Hello?"
        "I was greeted by Monika and Ken."
        "Monika is doing some paperwork in her desk."
        "While Ken is reading a novel beside her."
        m "Oh! I didn't see you coming [player]."
        m "Ken, our boyfriend's here."
        "Ken stopped reading and greeted me."
        show monika 1a at t21
        show ken 1a at t22 
        k "Hi, [player]."
        k 1ah "I'm not used to this..."
        mc "Just be yourself."
        k 2s "My usual self towards you is {i}killing{/i} you or getting you away from Monika."
        k "You're a damn masochist if you're going that route."
        mc "No thanks."
        mc "I'm not a masochist, but I've gotten used to it when Natsuki punches me for fun."
        show ken 2e at f22
        k "Oh, that pink-haired girl?"
        k 1aa "I can tell she's abnormally strong given her physique."
        mc "Yes... she is."
        show ken 1a at t22
        show monika 3b at f21
        m "That's because she's a Salien."
        k "Say what now?"
        m 3k "A Salien!"
        m "Those special humanoid creatures that sells planets like hotcakes!"
        k "I see... {w}wait a minute..."
        show monika 3a at t21
        show ken 4e at h22
        k "So that's what my {i}sensei{/i} is called..."
        k "My sensei is the one who taught me {i}'Hyper Instinct'{/i}!"
        k "He said he was about to conquer this planet when he was young..."
        k "But his head got hit and forgot about his origins."
        k "Well, my sensei passed on after contracting a heart virus."
        k "I can't believe there is another Salien living in here."
        k "I've heard from him that his race were wiped out."
        k "And that's all I know about him."
        "Another Salien that taught Ken 'Hyper Instinct'?"
        "Why are people allowing such beings to live here?"
        "Not that I'm complaining..."
        "I have Natsuki."
        "I dismissed the conversation and moved on to another topic."
        mc "Well, since I'm here, anything literature related that I could do with you girls?"
        m 5a "Well~"
        m lean happ ce om "Since I'm doing a bunch of paperwork for Cara and Ken here..."
        m 5a "Maybe you'd like to read with Ken here~"
        mc "Oh sure, no problem."
        k 1ah "Oh, tch fine!"
        k "Come here, [player]."
        show monika at thide
        show ken at thide
        hide ken
        hide monika
        "I sat beside Ken and read the action novel she was reading."
        "She looks... cute and more woman-like if you take a closer look."
        k "H-hey! Focus on the book!"
        mc "Sorry..."
        "I enjoyed reading with Ken."
        "It was satisfying."
        "After that little reading session, I bade them farewell."

        scene bg club_day
        with wipeleft_scene

        return

    label clubtime_end:

        m "Okay, everyone!"
        show monika 1b at t32 
        m "It's time to share poems!"
        m "Since Cara and Ken are our newest club members here, They are excused from our poem-sharing time!"
        m 3b "But next time, make sure you write a poem of your own to share with us!"
        show monika at thide
        hide monika 
        "We all shared our poems."
        "I kinda missed this type of interaction with my girlfriends."
        "As usual they are impressed with my works of art."
        "Time passes."
        pass
    
    stop music fadeout 2.0
    "The poem-sharing ended."
    "It's time to go home."

    play music t8
    scene bg corridor
    with wipeleft_scene

    show sayori 1a at t11
    s "[player], ready to go?"
    mc "Yes!"
    show sayori 4r at h11
    s "Excellent!"
    s "All 6 of us are waiting for you!"
    s "I missed walking with you and all of my friends!"
    mc "I missed it too..."
    mc "Except, only 6 of us are walking."
    show sayori 1m at f11
    s "Ehhhhh?"
    s 2h "Are you being a meanie to someone?"
    mc "No!"
    mc "It's 6 of us..."
    mc "Since Natsuki is on my back, she's not walking!"
    "I approached Natsuki."
    mc "Come on, hop on my back."
    mc "I know you want it~"
    show natsuki 1u at t22
    show sayori 1a at t21
    n "Ugh!"
    n 12c "But fine..."
    n 5x "Hmph..."
    "She climbed on my back."
    c "You're making me jealous, Natsuki."
    c "You're the only person who can piggyback on [player]."
    n 5u "SHUT UP!"
    show sayori at thide
    show natsuki at thide
    hide sayori
    hide natsuki 
    "We all laughed."
    "We left the school building."

    stop music fadeout 2.0
    scene bg vm
    with wipeleft_scene

    $ a_name = '???'
    $ style.say_dialogue = style.edited
    a "Target sighted."
    a "A perfect group to add to my army."
    a "I guess they're going to be 'sleepless' tonight."
    a "A H A H A H A H A H A H A H A H A H A H A H A H A H A H A!"
    $ style.say_dialogue = style.normal

    scene bg residential_day
    with wipeleft_scene
    play music t8

    "All of us walked back home."
    "We had a very good time talking with each other."
    "A perfect day, that is."
    "Cara and Ken was the first to go to their separate ways."

    scene bg house
    with wipeleft_scene

    "The boyfriend stops here."
    show monika 1a at t41
    show sayori 1a at t42
    show yuri 1a at t43
    show natsuki 1a at t44
    mc "I guess it's time to go home now."
    mc "See you tomorrow!"
    hide monika
    hide sayori 
    hide yuri 
    hide natsuki 
    with wipeleft
    "They all said their goodbyes as I went inside my house."
    s "W-what is this?"
    "She picked up a very weird item."
    s "H-hey , [player]. I think you left--"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    play sound "sfx/s_kill_glitch1.ogg"
    pause(1.0)
    s "AAAAAAAAAAH!"

    scene black
    with dissolve_scene_full

    pause(1.0)

    scene bg bedroom
    with dissolve_scene_full

    "Whew..."
    "That was a very enjoying day."
    "It's a good thing Ken was accepted wholeheartedly."
    "Now we have 7 members in the club!"
    "And I have 6 girlfriends!"
    "94 to go!"
    "I wonder who's next?"
    "Renpy-sama is giving me weird girlfriends..."
    show cara 1y at t21
    "A martial artist..."
    show ken 4a at t22 
    "And an assassin."
    show cara at thide
    show ken at thide
    hide cara 
    hide ken
    "What is next? A cowgirl?"
    "A pirate?"
    "A witch or a familiar?"
    "Wait... those are really weird people."
    "In a school setting, I mean."
    "But I'll love them nonetheless!"
    "Maybe this is like how to be Aijou Rensho..."
    "I need to be strong!"
    "I need to be fair to all!"
    "Time to write poems, watch anime, read manga, and everything else!"
    
    stop music fadeout 2.0
    scene black 
    with dissolve_scene_full

    return
