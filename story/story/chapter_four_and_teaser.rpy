label chapter_teaser:

    play music m1 
    $ t_name = "Tensura E."
    t "Hello there."
    show chitoge turned mb at t11 
    t "Modder here."
    t "This is just a glimpse of what craziness my mod will become."
    show chitoge turned rhold mb bc at s11 
    t "Sorry if it's a bit rushed..."
    t "I need to finish it before the 2024 Modding Expo submissions deadine..."
    show chitoge rhip ea at t11 
    t "But I'm hoping that even though it's a demo, it's still a good chunk of the mod that you can enjoy."
    t "Thanks for playing, and see you when this mod's released!"
    show chitoge at thide 
    hide chitoge 
    $ show_poem(poem_credits, paper_sound=audio.page_turn, music=False, from_current=False, revert_music=False)
    stop music fadeout 2.0

    pause (2.0)
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ m_name = "Monika"
    $ c_name = "Cara"
    $ k_name = "Ken"
    $ a_name = "Amy"
    $ mi_name = "Mizumi"
    $ kt_name = "Kotonoha"
    $ sc_name = "Sayochi"
    $ sz_name = "Sayozuki"
    $ sy_name = "Sayo"

    if sayori_punch == True:
        scene bg lroom
        with dissolve_scene_full
        "It's a normal Saturday Morning..."
        "Until I received a call..."
        mc "Hmm?"
        "I gently answered the phone."
        s "Help me, [player]!"
        mc "How can I help you, Sayori?"
        s "My bow... It's gone!"
        mc "..."
        mc "Alright, Sayori. I'll come over."
        scene black 
        with dissolve_scene_full
        pause (1.5)
    else:
        pass
    
    if amy_spell == True:
        scene bg lroom2
        with dissolve_scene_full
        a "Finally..."
        a "The Dark Arts Spell I'm practicing... I finally mastered it!"
        a "This is gonna save my boyfriend from imminent danger..."
        scene black 
        with dissolve_scene_full
        pause (1.5)
    else:
        pass

    if time_travel == True:
        scene bg bedroom
        with dissolve_scene_full
        mi "All I need is to put this quartz here and..."
        show white zorder 4:
            alpha 0.6
            linear 0.25 alpha 0.0
        mi "It's all done."
        mi "I can't wait till I take everyone else into the future..."
        scene black 
        with dissolve_scene_full
        pause (1.5)
    else:
        pass

    if video_game == True:
        scene bg lroom2
        with dissolve_scene_full
        sy "I'll go ahead and beat my baby gronk [player] in a game of Shining Zero!"
        s "I wanna see you do it, Sayo."
        sc "We're counting on you."
        sy "Of course Big Sis!"
        scene black 
        with dissolve_scene_full
        pause (1.5)
    else:
        pass

    if mystery_caller == True:
        scene bg residential_day
        "It's a fine Saturday morning."
        "A perfect time for Yuri to stroll..."
        y "It's a wonderful day for me to take a stroll and remove myself from the stress."
        "Until all of a sudden..."
        show black
        play sound fall
        y "Hey, let go of me!!"
        y "Let go--"
        "Yuri passes out."
        scene black 
        with dissolve_scene_full
        pause (1.5)
    
    return

label chapter_four:

    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ m_name = "Monika"
    $ c_name = "Cara"
    $ k_name = "Ken"
    $ a_name = "Amy"
    $ mi_name = "Mizumi"
    $ kt_name = "Kotonoha"
    $ sc_name = "Sayochi"
    $ sz_name = "Sayozuki"
    $ sy_name = "Sayo"

    play music m1

    "..."
    mc "Hello?"
    mc "Anyone here?"
    s "Renpy-sama?"
    show sayori 1ba at t11
    "I see an annoying girl--"
    "Wait, she's not annoying."
    s "Oh hi, [player]."
    s 2bx "How was your day?"
    mc "Pretty standard, I say."
    mc "But now seeing you will make my day right now special."
    s 4br "Sure you would."
    s "I love you!"
    mc "I love you too..."
    s 1bx "I kinda want to meet new people..."
    show sayori 1ba at t11
    mc "Oh yeah."
    mc "I haven't {i}zinged{/i} anyone yet."
    mc "I sure do hope another girlfriend will be added into the club."
    s 4br "I can't wait to meet new people!"
    s 1bx "Should I skip you forward to class?"
    mc "Nah, I should be fine."
    s 1bh "Why not...?"
    mc "Who knows what would've happened during my prep time for school?"
    s 1bx "Okay!"
    s "Alright, [player]. Time for you to wake up."
    s 4br "I love you!"
    stop music 
    scene bg bedroom 
    play sound fall
    "I woke up."
    "Huh, seems like Mizumi already left."
    "I looked at the clock."
    "Holy crap, I'm late."
    "I need to get changed."
    "Hurry, [player]. Hurry."
    scene bg residential_day
    with wipeleft_scene
    "Sure enough, none of my girlfriends ar here."
    "They're probably at school right now."
    "I wish Mizumi could've woke me up."
    "I ran as fast as I could."
    scene bg gate
    with wipeleft_scene 
    "Oh thank God, the gate is still open."
    "I made a run for it until..."
    play sound it
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    $ yn_name = "???"
    mc "Aaaah!"
    yn "Aaaah!"
    play sound "sfx/smack.ogg"
    $ nastya_eyes = 1
    yn "Ow..."
    show nastya turned pani om ce at i11:
        yoffset 500
        easein .75 yoffset 0
    "She got up from the fall."
    mc "Oh I'm so sorry... are you ok?"
    yn anno e1f "You just appeared out of nowh--{nw}"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show nastya turned shoc blus oe ml at h11 
    "{b}ZING!{/b}"
    "Oh..."
    "A new girlfriend."
    "She randomly teleported to me out of nowhere too."
    mc "You're the one who teleported."
    yn nerv om "Oh, yeah... right, sorry."
    mc "It's okay."
    mc "I deserve this because I woke up late anyway."
    yn neut nobl om "I think you can still make it with minutes to spare."
    yn cross om "Where is your classroom anyway?"
    show nastya cm at t11 
    mc "It's in the third floor... almost at the end of the school building."
    yn worr ce om "Oh."
    yn turned sad om "Sorry about that."
    yn neut om oe "Well, I should not be keeping you here."
    yn happ om "Nice meeting you, I'm Yna."
    $ yn_name = "Yna"
    mc "Name's [player]..."
    yn neut om "[player]?"
    yn "I think I heard that name before..."
    yn happ om "But anyways. It's great meeting you, I can't keep you here for long."
    yn ce "Bye!"
    show nastya at lhide 
    hide nastya 
    "She left."
    "Wait, she said she heard my name before..."
    "Eh, I'm not gonna think of that for now..."
    "I need to get to class!"
    scene bg class_day
    with wipeleft_scene
    play music t2 
    "Thankfully, I'm still able to arrive on time."
    a "[player], what happened to you?"
    mi "We we're so worried."
    mc "I woke up late."
    mi "Sorry I didn't wake you up."
    mi "I thought you'd be waking up just fine right on time."
    mc "It's fine."
    mc "Something good happened anyways."
    a "Oh?"
    mc "Yeah."
    mc "You'll find out soon enough."
    sz "Good morning class!"
    show sayozuki 1ba at t11 
    "And just in time our teacher arrived in our class."
    sz 3bb "Let's us start our class today."
    show sayozuki at thide
    hide sayozuki 
    "And thus classes started."
    "Sayori's mom is really good at teaching us."
    sz "Would you like to answer this, [player]-chan?"
    stop music fadeout 2.0
    "Class became quiet."
    "Wait..."
    "Did I hear that correctly?!"
    play music t7 
    sz "Ehhhh..."
    a "Oh no..."
    mi "This isn't good."
    "Ummm... I need help?"
    "Renpy-sama?"
    "Monika?"
    "Sayori?"
    "{b}ANYONE?{/b}"
    $ time_jump = False
    menu:
        "Amy, Help!" if amy_spell:
            stop music fadeout 2.0
            a "I guess I'll try one of the few spells I recently learned..."
            a "..."
            $ style.say_dialogue = style.edited 
            a "Secret Dark Arts Spell: Memory Wipe!"
            show white zorder 4:
                alpha 0.6
                linear 0.25 alpha 0.0
            $ style.say_dialogue = style.normal 
            "Everyone inside the classroom, except her, me, Mizumi and Sayozuki felt like they were in a trance for a while."
            "Then everything went back to normal for them."
            play music t2
            a "Miss Sayozuki... please don't say that again..."
            a "This spell requires a lot of mana from me and I felt drained after that."
            sz "Thanks, Amy. I'm sorry."
            sz "Now then, [player]. Shall you continue coming up the board and answering the question?"
        "Mizumi, Help!" if time_travel:
            stop music fadeout 2.0
            mi "I think I can fix this..."
            $ currentpos = 45.264 - (get_pos() / 2.0)
            $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
            $ quick_menu = False
            play music t6r
            show noise zorder 100 at noise_alpha
            show vignette zorder 100 at vignetteflicker(-2.030)
            show layer master at rewind
            mi "{cps=150}I think I can fix this...{/cps}{nw}"
            "{cps=150}{b}ANYONE?{/b}{/cps}{nw}"
            "{cps=150}Sayori?{/cps}{nw}"
            "{cps=150}Monika?{/cps}{nw}"
            "{cps=150}Renpy-Sama?{/cps}{nw}"
            "{cps=150}Umm... I need help?{/cps}{nw}"
            mi "{cps=150}This isn't good.{/cps}{nw}"
            a "{cps=150}Oh no...{/cps}{nw}"
            sz "{cps=150}Ehhhh...{/cps}{nw}"
            "{cps=150}Did I hear that correctly?!{/cps}{nw}"
            "{cps=150}Wait...{/cps}{nw}"
            "{cps=150}Class became quiet.{/cps}{nw}"
            sz "{cps=150}Would you like to answer this, [player]-chan?{/cps}{nw}"
            $ currentpos = 90.528 - (get_pos() * 2.0)
            $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            $ quick_menu = True
            play music t2
            hide noise
            hide vignette
            show layer master
            $ del _history_list[-28:]
            "Sayori's mom is really good at teaching us."
            mi "Thank me later, [player]."
            mi "Good thing I enhanced the Time Travel ring into a bracelet."
            mi "And it can reverse short amounts of time!"
            sz "Would you like to answer this, [player]--{nw}"
        "Renpy-sama, Help!" if not amy_spell and not time_travel:
            "Renpy-sama, can you help me out of this mess?"
            menu:
                "...":
                    pass
            menu:
                "Why would I help you?":
                    pass
            "Because if you don't..."
            "I'm telling the Modder."
            menu:
                "...":
                    pass
            menu:
                "Alright, fine.":
                    pass 
            menu:
                "This is the last time, [player].":
                    pass
            menu: 
                "My twin sister will kill me if she finds out about this.":
                    pass
            $ time_jump = True 
            stop music 
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause (3.0)
            hide screen tear
            jump after_class
    mc "Yes, Ms. Sayozuki!"
    "I immediately went up to the board."
    "Crisis averted."
    "After that, everything went smoothly."
    "And soon after, class is over."
    "Time for club!"
    scene bg corridor
    with wipeleft_scene

label after_class:
    if time_jump == True:
        scene bg corridor
        "..."
        "What just happened?"
        "That was a woozy trip."
        "But anyways..."
        "Crisis averted, I guess?"
        "Let's just move on."
    else:
        stop music fadeout 2.0
    "All 3 of us walked towards the clubroom."
    "As we walked, I passed by an open room."
    "And saw... {i}her.{/i}"
    "I stopped for a bit."
    mc "Mizumi, Amy, you go on ahead."
    show amy turned happ om at t21 
    show mizumi 1a at t22 
    a "Sure thing, love!"
    mi 1b "Make sure you won't be late!"
    show amy at thide 
    show mizumi at thide 
    hide amy 
    hide mizumi 
    "They walked towards the clubroom."
    "I went inside the room where she is in."
    scene bg class_day
    with wipeleft_scene
    play music t4 
    "Looks like she's tinkering something on her own desk."
    mc "Um... hello?"
    yn "Woah..."
    show nastya turned shoc ml at t11
    "She was stunned after seeing me."
    yn happ om "Oh hi, [player]."
    yn "H-how did you know where I am?"
    mc "Just saw you because this room is open."
    yn neut om "Oh, I see."
    mc "What are you doing right now?"
    yn happ om "I'm making a new invention right now."
    yn ce "And you're gonna be the first one to be testing this thing!"
    show nastya happ cm oe at t11 
    "She held the machine that she's tinkering up."
    yn om "The future is now, thanks to science!"
    yn ce "Behold, my Hug-Enjoy-inator!"
    yn oe "All I need to do is to shoot you with this..."
    yn "And myself..."
    yn "And then..."
    show nastya cm at face
    play sound fall
    stop music fadeout 2.0
    "She hugged me."
    "..."
    "What is this?"
    "I enjoy her hugs..."
    yn ce "Mmmmm~"
    play music t3p
    yn oe om "Are you enjoying it?"
    yn sedu blus mb "I'm kinda enjoying it too..."
    mc "..."
    mc "I'm glad you do."
    yn e1b "Well..."
    yn oe "The moment I met you..."
    yn "I felt something."
    yn "Something that I can't explain."
    yn "Not even this scientific brain of mine."
    yn "But I can only be certain..."
    yn "I... love you, [player]."
    yn "Will you... go out with me?"
    show black 
    with dissolve_cg
    menu:
        mc "..."
        "We're attracted to each other like magnets, so sure!":
            pass
        "Science ain't my thing.":
            "..."
            "I'm not gonna say anything."
            "You're annoying."
            menu:
                "Let's just move on."
                "We're attracted to each other like magnets, so sure!":
                    pass
    
    hide black
    with dissolve_cg
    stop music fadeout 2.0
    mc "I..."
    mc "Sure, Yna."
    mc "I'd love to go out with you!"
    show nastya turned happ nobl om at t11 
    play music t4 
    yn "Yay!"
    yn "I now have a boyfriend!"
    yn ce "Big cous' Monika would be so proud of me!"
    show nastya oe cm at t11 
    mc "Monika?"
    mc "Monika is your cousin?"
    yn neut om "Yes."
    yn cross happ om "I can't wait to tell her about this."
    yn ce "I'm pretty sure she'll be stoked!"
    show nastya turned happ oe cm at t11
    "She is Monika's cousin?"
    "Oh boy..."
    "Am I going to get Monika's relatives too?"
    "Speaking of Monika..."
    "I need to head to the club right now!"
    mc "Yna, I have to go."
    mc "It was fun hanging out with you, but I have a club to attend to."
    mc "See yah!"
    yn om "Bye, [player]. I would like to walk home with you after. Would it be fine?"
    mc "Sure, Yna!"
    yn ce "Okay! See yah!"
    scene bg corridor 
    with wipeleft_scene
    stop music fadeout 2.0
    "I'm running late now..."
    "But it's worth it."
    "For Yna."
    "My new girlfriend."
    "I opened the clubroom door."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Haaah, haah."
    mc "Sorry I'm late."
    s "[player]!"
    show sayori turned sad mi at t11 
    s "Where have you been?"
    show sayori cm at t11 
    show amy turned sad om at t31 
    a "I thought you're gonna be quick..."
    show amy cm at t31 
    show mizumi 1d at t33 
    mi "What happened to you?"
    mc "Ah..."
    mc "Sorry about that."
    mc "I met with someone."
    s shoc om "Really?"
    show sayori 4r at h11 
    s "Is she gonna be a part of our club?"
    show sayori turned happ at t11 
    mc "I hope so."
    mc "Anyways, what did I miss?"
    show amy happ at t31 
    show mizumi 1a at t33 
    s neut lup om "You missed most of the club time."
    s sad ldown mi "That's why we we're worried about you."
    show sayori cm at t11 
    mc "I'm sorry."
    mc "But anyways, I'm here now."
    mc "No worries, nothing happened to me."
    m "Okay, everyone!"
    show sayori at thide 
    show amy at thide 
    show mizumi at thide 
    hide sayori 
    hide amy 
    hide mizumi 
    "Looks like I missed a lot of club time."
    "But I still made it here nonetheless."
    play music t5
    show monika forward happ om at t11 
    m "Since [player] is not here I... {w=1.5}, Oh, you're here now?"
    mc "Hi, Monika."
    mc "Sorry I was late."
    m anno om lpoint "Where have you been?"
    mc "I went somewhere and met with someone."
    m ldown "That's not an excuse."
    mc "I'm sorry."
    m lean happ blus "I'm gonna punish you for that~"
    m ce om "You're coming home with me!"
    mc "I uh..."
    mc "Sure!"
    show monika forward happ oe cm at t11
    "I'm visiting Monika's house?"
    "That's fantastic!"
    m om "As I was saying..."
    m sedu lpoint "I'm punishing you..."
    m lean happ om "You don't back down now, ok?"
    mc "I won't Monika."
    m ce "Great!"
    play music t8
    m forward happ om oe "Okay, everyone!"
    m "I'm gonna dismiss the club early today."
    m lpoint "And I'm borrowing [player] too."
    m ldown "May I have your permission?"
    show sayori turned sedu mb at t33 
    s "Go get him, Monika!"
    show mizumi 1g at t31 
    mi "No problem!"
    show mizumi at thide 
    show sayori at thide 
    show monika at thide 
    hide sayori 
    hide mizumi 
    hide monika 
    "Seems like everyone agreed."
    "Welp, I guess I have no choice..."
    sz "You better {i}discipline{/i} him well, ok?"
    m "I will, Ms. Sayozuki."
    scene corridor
    with wipeleft_scene
    "..."
    "I'm going home with Monika today."
    mc "Monika?"
    m "Yes?"
    mc "Can we wait... for just a few minutes?"
    m "What for?"
    mc "{i}Someone{/i} is walking home with us."
    m "Really?"
    mc "Yeah."
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "As soon as I said that a flash of light emits in front of us... {w=1.0}and there she is."
    show nastya turned happ om at t11
    yn "Hello, [player]! Hello, Big 'cous!"
    show nastya at t21 
    show monika forward happ om at t22 
    m "Yna! What brings you here?"
    show monika cm at t22
    yn cross happ om "Oh I thought it's obvious."
    yn ce "I'm here to walk home with my boyfriend, [player]!"
    show nastya oe cm at t21
    m vsur ml "Whaaaa?"
    show monika at h22 
    m "You didn't tell me anything, [player]!"
    mc "You didn't gave me the time to do so!"
    mc "That's the reason I was late today..."
    mc "I spen't time with her."
    m 3b "Oh... that makes sense."
    m forward happ om "But that doesn't excuse you..."
    m lean happ om "...from being punished~"
    yn worr e1b om "Monika..."
    yn "Please forgive him."
    yn ce "It's my fault anyways."
    m forward happ lpoint "Yna..."
    show monika ldown at t11 
    "She whispers some things to Yna."
    show monika at t22
    yn happ om oe "I see..."
    yn "This is actually a good thing."
    yn ce "You can go ahead, Big cous."
    yn oe "Lead him the way."
    m om ce "Yes, Yna."
    show monika at thide
    hide monika 
    show nastya at thide 
    hide nastya
    "What did she say to Yna?..."
    m "Let's go home together then."
    scene bg residential_day
    with wipeleft_scene
    "Now I'm really nervous with what's going to happen."
    "But nonetheless..."
    "I get to spend time with Yna and Monika today!"
    "We are going to their house."
    "..."
    "Seems like this is going to take a while."
    menu: 
        "Maybe I can have a lil bit of fun!"
        "Walk with Yna.":
            "I approached Yna."
            mc "Hello, Yna."
            yn "Yo."
            show nastya turned happ at t11 
            "Yna looked at me with a sincere, yet devious smile."
            mc "..."
            mc "What did Monika tell you...?"
            yn ce om "It's going to be a secret."
            yn oe "You just have to wait until we arrive home."
            show nastya cm at t11
            mc "..."
            mc "I hope it will be an exciting one."
            yn om "Of course!"
            yn "Big Cous' has something planned for you."
            yn "Let's just wait and see, my love."
            show nastya ce cm at face 
            play sound fall
            "I hugged her."
            mc "I love you, Yna."
            yn om "I love you too!"
            show nastya oe at t11 
            yn "Okay, [player]."
            yn "Shall we keep walking?"
            mc "Of course."
            mc "Monika will punish me again if we slow down."
            yn ce "You bet!"
            show nastya at thide 
            hide nastya 
            "And thus I walked even faster than usual."
        "Walk with Monika.":
            "I walked with a faster pace to get close to Monika."
            "I'm excited and nervous at the same time."
            mc "Monika, wait!"
            m "Huh?"
            show monika 1a at t11 
            "Monika stopped and looked at me."
            m forward sedu om "What's the matter?"
            m "Excited to get punished?"
            show monika cm at t11
            mc "I don't know what you mean by 'punished'."
            m om "You'll just have to find out."
            show monika cm at t11
            mc "I kinda wanna find out and not find out."
            m lean happ om "You have no choice."
            mc "Monika, I'm sorry that I was late, ok?"
            m forward lpoint happ om "A little bit too late."
            m sedu om "You missed the entire club time."
            show monika cm at t11 
            mc "I spent my time with your cousin!"
            m lean happ om "Should've brought her in the club then."
            show monika cm at t11
            mc "I uh--"
            mc "Uh..."
            mc "Damn, you're right."
            mc "Okay, I won't argue."
            m forward happ om "Good."
            m lpoint sedu om "Come along now, we're almost home."
            mc "Yes, Monika."
            show monika at thide 
            hide monika
            "And thus I continued walking, defeated by my own girlfriend."
    
    scene bg house_monika
    with wipeleft_scene

    "Here we are."
    "Monika's house."
    show monika forward happ om at t11 
    m "Come on in, [player]."
    m "This is my house."
    m lean happ om "My cousin also lives with me, her parents died on a car accident since she was young."
    m ce "Make yourself at home, love!"
    mc "Of course."
    show monika at thide 
    hide monika 
    "Monika opened the door for me."
    scene bg lroom3
    with wipeleft_scene 
    "Her living room is neat."
    "Well-kept and tidy."
    m "Just sit on the couch for a moment while I prepare something for you."
    yn "I'll go help you, Big Cous!"
    "Both of them went straight to the kitchen."
    "..."
    "Okay, now I'm kinda bored."
    "I decided to read some of the literature that is displayed on the table."
    mc "..."
    mc "Huh..."
    mc "{i}'Cunning Hearts'{/i}..."
    mc "And {i}'Cunning Hearts 2'{/i}..."
    mc "This seems to be an interesting thing to read..."
    "I laid down on the couch and started to read the first book."
    "And boy this was so interesting to read."
    "I kinda want to borrow both of these books after the 'punishment'."
    "While I was too engrossed with what I'm reading, someone arrived at the house."
    $ hm_name = "???"
    hm "Monika, Yna, I'm home!"
    "Huh...?"
    hm "...?"
    hm "Hello there, young man."
    mc "!"
    "I put down the book that I'm reading as I sit up from the couch."
    show harumi at t11 
    mc "Oh I'm sorry for my manners."
    hm "I guess you're--{nw}"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show harumi turned n2 m6 e4 b2 at h11 
    "{b}ZING!{/b}"
    "..."
    "Umm...?"
    show harumi turned m4 e1 b1 at t11
    hm "You must be Monika's club member."
    mc "Yes, ma'am."
    mc "[player]. Nice to meet you."
    hm m7 "Harumi. I'm Monika's mother."
    $ hm_name = "Harumi"
    hm ce "Nice to meet you!"
    show harumi cm at t11 
    "..."
    "Great, another mom added to the mix."
    hm oe m7 "I've heard that she is your boyfriend."
    hm "And so is everyone else."
    show harumi cm at t11 
    "Wait, what?"
    mc "How did you... know that?"
    hm m7 "Monika has been telling a lot of things to me."
    hm "Don't get me wrong..."
    hm rhip "I kinda feel the same way when I was at your age."
    hm "A lot of boys just couldn't resist me."
    hm "They all even agree to share me just to spend time with me!"
    show harumi cm at t11
    "..."
    "This woman..."
    "Is just like me for real (fr)..."
    mc "Mrs. Harumi."
    hm m7 "Spare the 'Mrs.', honey."
    hm "My husband has been long gone ever since Monika was a child."
    hm "Ms. Harumi is just fine."
    hm b2 m3 "It was... difficult to raise her I might say."
    hm b1 m7 "Now I won't worry about her!"
    hm "You seem to be a fine man perfectly fitting for her."
    hm "I just need you to promise me..."
    hm "Take care of her, okay?"
    show harumi cm at t11
    mc "Of course, Ms. Harumi."
    mc "I will never give her up."
    mc "I will never let her--{nw}"
    hm m7 "Spare that line for her."
    hm ce "I am really glad that my daughter is lucky to be a part of your {i}harem{/i}."
    hm om "I'll go on ahead and get myself some rest..."
    hm e3 m3 "I'm tired..."
    show harumi at rhide 
    hide harumi 
    "She immediately left and went upstairs."
    "... What was that?"
    "She seemed... troubled about something."
    "I wish I could go upstairs and ask her myself..."
    "But I don't think it's a great idea right now."
    "She'll probably open up a bit later."
    "She is my {i}girlfriend{/i} after all."
    "I decided to continue to read..."
    "..."
    "That was a fun read."
    "Cunning Hearts 1 and 2 should be on our club's bookshelf."
    "Might as well read another book here on the desk, I have nothing to do..."
    mc "What's this...?"
    mc "{i}'Relationships in a Foreign Land: Book One'.{/i}"
    mc "By D. L. Pepper..."
    "Who are these writers and where does she get these books?"
    "As I was about to pick up the book, Monika and Yna showed up."
    show monika casual_2 forward happ om at t11
    m "Hello, [player]."
    show monika cm at t21 
    show nastya sweater cross happ om at t22
    yn "Hi, [player]!"
    show nastya cm at t22
    mc "Hello to both of you."
    mc "Monika you look stunning."
    mc "I haven't seen you wear that casual outfit before."
    m lpoint om "New outfit from the Modder for me!"
    m lean happ om ce "I am really grateful for him!"
    m oe "He intricately coded this outfit into existence for me to use."
    show monika cm at t21 
    mc "He really is a good person isn't he?"
    m forward happ om rhip "He indeed is!"
    yn turned neut om "What's with this 'Modder' thingy?"
    show monika cm at t21 
    show nastya cm at t22 
    mc "Yna, the Modder is someone who oversees us in this world."
    yn om "Like a god or something?"
    mc "You can say that he is, yes."
    show nastya pani om ce at s22 
    yn "Anything that is beyond science hurts my brain."
    show nastya sad cm oe at t22 
    mc "Yna, there are some things in this world that couldn't be explained..."
    mc "You just don't have to think about them."
    mc "It'll help your brain to lessen the stress."
    mc "You just have to trust the process."
    mc "I mean, look at me."
    mc "I don't know how your inventions work."
    mc "But I tend to trust it because I knew it would be beneficial to me."
    mc "And it is built by my cute, smart girlfriend."
    show nastya sweater flus blus mc e1b b2b at s22 
    yn "Stop pampering me~"
    show nastya happ om nobl at t22 
    yn "I love you, [player]."
    mc "I love you too."
    show nastya cm at t22 
    m anno om "Hey, what about me?!"
    mc "I wouldn't leave you out, Monika."
    mc "I love you too!"
    m lean happ "Good."
    m forward happ om "Hey, we prepared sandwiches for you."
    yn happ om "Actually, it's just me."
    yn "I tasted her sandwich and... I don't think FDA will approve her consumables."
    yn cross happ om "I whipped out my 'Sandwich Maker 9000-inator' just to make you a sandwich."
    yn "No offense, Big Cous, but you aren't really the cooking type."
    show monika forward pani om e4c at h21 
    m "Hey, I'm improving, okay?"
    show monika angr cm at t21 
    mc "I do understand that."
    mc "I hope I'll get to taste your cooking soon."
    mc "Just learn and improve for me, ok?"
    mc "Don't worry, Monika."
    mc "Not knowing how to cook doesn't make me love you {i}less{/i}."
    mc "Let's just start digging in, shall we?"
    show monika at thide
    show nastya at thide 
    hide monika 
    hide nastya 
    "We all started eating the sandwiches."
    mc "Oh yeah. By the way, your mom arrived minutes ago and went up her room."
    



            



    return 
