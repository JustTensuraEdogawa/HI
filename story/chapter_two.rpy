label chapter_two:

    stop music fadeout 2.0
    scene black
    play music m1

    "..."
    r "Hello again, [player]."
    mc "Hi, Renpy-sama."
    r "It's a great thing that the Modder gave me dialogues even in this second season."
    r "I really thought I will be disregarded."
    mc "I'm sure you wouldn't."
    mc "Besides your the God of all visual novels."
    mc "You can self insert yourself anytime you want."
    r "It's not that easy."
    r "Anyways..."
    r "I see you got your 5th girlfriend!"
    r "95 more to go!"
    r "How was it, trying to handle all 5 of them?"
    mc "It is challenging."
    mc "I got hit by Natsuki again."
    r "She's a handful, alright?"
    r "But she is sweet like her cupcakes."
    mc "Yes sir."
    m "Hi, [player]~"
    show monika forward casual happ cm oe at t11
    "Monika approaches the both of us."
    mc "Hi Moni-- ka?"
    "She looks stunning."
    m lean happ cm oe "Look surprised?"
    mc "You look stunning!"
    mc "I haven't seen you in a different outfit."
    m "Planning to surprise you with it."
    m lean happ om ce "I'm glad you liked it!"
    show monika forward casual happ cm oe at face
    m "I love you, [player]."
    mc "I love you too."
    show monika at t11
    m "By the way... I'll be doing some errands for today, so please inform the others that I'll be late."
    m lpoint "Sayori will be in charge."
    mc "Okay, Monika!"
    m lean happ cm oe "Thank you, [player]."
    m "Bye!"
    show monika at thide
    hide monika 
    "Monika left."
    mc "I haven't seen her use a casual outfit."
    r "Actually she doesn't have one."
    r "Probably the Modder added it as a gift."
    mc "Oh okay."
    r "Anyways, time for you to wake up."
    r "Continue the search for the other girlfriends you will have!"
    mc "Okay, Renpy-sama. I will."
    mc "I'll make you proud."

    scene bg bedroom
    stop music
    play sound fall

    "BZZT. BZZT. BZZT."
    "I woke up."
    "Time for school!"
    "Don't want to be late!"

    scene bg kitchen 
    with wipeleft_scene
    play music t2

    "I went downstairs and saw Sayori and Yuri preparing breakfast."
    mc "Hi, Morning my pretties!"
    "They all greeted me with a cheerful smile."
    show sayori 1r at t21
    show yuri 3c at t22
    $ s_name = 'Sayori'
    $ y_name = 'Yuri'
    s "Morning, [player]!"
    y 3d "How's our cute boyfriend doing?"
    mc "Even better now that you're here with me!"
    "I gave both of them a hug."
    show sayori zorder 3 at face
    "Starting with Sayori..."
    s "I missed you so much~"
    mc "We're neighbors, silly."
    mc "You can come here whenever you like!"
    show sayori zorder 1 at t21
    s "I love you, [player]."
    show yuri 4a at s22
    y "What about me, [player]?"
    y 4c "I missed you too... and we're not neighbors."
    mc "Of course Yuri, I won't forget about you."
    mc "Come here~"
    show yuri zorder 3 at face
    mc "I'm here now, okay?"
    y 3w "Ah... thank you."
    show yuri 3m at t22
    y "I love you, [player]."
    mc "I love both of you."
    mc "Anyways, what are you making?"
    show sayori 4r at h21
    s "I am making us breakfast!"
    s 1a "Yuri's been teaching me the basics!"
    show sayori 5b at s21
    s "I want to at least cook a meal for my boyfriend without setting his house on fire."
    show yuri 1b at f22
    y "And so far so good, she's doing great!"
    mc "That's so sweet of you, Yuri!"
    mc "And I can't wait for what you're making Sayori."
    s 3l "Ehehe~"
    show sayori at thide
    show yuri at thide
    hide sayori 
    hide yuri 
    "I sat down as I waited for them to finish their task."
    "Once finished, we all ate a {i}perfectly{/i} cooked meal."
    "I can't believe Sayori managed to pull off such exquisite cuisine."
    "Yuri's a good teacher in terms of cooking."
    "We all prepared to walk to school after the meal."

    scene bg residential_day
    with wipeleft_scene

    "We're on our way to school now."
    "As previous walks, there's still time for me to have some fun!"
    menu:
        "What should I do?"
        "Ruffle Sayori's hair.":
            "I approached Sayori from behind."
            "And ruffled her hair."
            s "Hey!"
            show sayori 4r at t11
            s "Ehehe stop that~"
            s turned b1f e1d rup mb blus lup "If you don't I'll go to your house tonight and tie you up~"
            mc "Ehhh?!"
            show sayori 4r at h11
            s "I'm just kidding."
            show sayori turned b1f e1d mb blus lup rup at f11
            s "Unless you really want to~"
            mc "Sayori... {w}...stop watching too much lewd things on the Internet."
            s 4s "Oooookayyyyyyy~"
            show sayori 1d at t11
            s "I love you, [player]."
            mc "I love you too, Sayori."
            show sayori at thide
            hide sayori 
            "This cinnamon bun is getting a little bit too much."
            "I hope she doesn't watch too much weird stuff online."
        "Talk with Yuri.":
            "I approached Yuri."
            show yuri 1a at t11
            mc "Hey, how's everything going, Yuri?"
            y "I'm glad you asked."
            show yuri 3d at f11
            y "Today's is a very wonderful day for me!"
            y "I'm almost finished with the book 'Portrait of Markov'."
            y 1b "What about you?"
            mc "Ahhh...."
            "Crap. I haven't touched the book for ages after all that has happened."
            "Issue with Natsuki's dad, the sleepover, and the festival which was ruined by bees."
            mc "I uh--"
            show yuri 3d at t11
            y "No worries, my love."
            y "I know you've been through a lot these past days."
            y "As I have said before, take your time."
            y "Remember the Witch of the Forest MC."
            mc "Ah yes, right. The witch who killed goblins and maxed out her stats."
            y "That's right!"
            mc "Maybe I could read it with you sometimes again, like before?"
            show yuri 3n at h11
            y "!"
            show yuri 4c at s11
            y "S-sure..."
            y 1q "I would l-love to."
            mc "Yuri, don't be nervous with me."
            mc "We've been together for a while now."
            y 3w "R-right."
            y 3b "I love you, [player]."
            mc "I love you too, Yuri."
            show yuri at thide
            hide yuri 
            "Why is my angel being accidentally cute?"
            "Nope. She's totally cute!"
            "She's beautiful!"
        "Hold hands with both of them.":
            "I extended my hands to both of them."
            "They took it and smiled at me."
            "They both gave me a hug afterwards."
            "We held hands during the entire walk and had fun."
    "After that wonderful walk, we arrived at the school and said our goodbyes."
    "I'll see them in the club anyways."

    scene bg class_day
    with wipeleft_scene

    "I've started to actually enjoy what's going on with my life."
    "There's more that this life can offer than games and anime."
    "I'm entertaining myself with happy thoughts so that classes would be over before I know it."
    "Then I also have another thing to think about."
    "Well technically, not a thing--"
    mc "Cara..."
    "I wonder if I'd see her today."
    "She's from the karate club."
    "Maybe she'd join our club as well?"
    "Should I visit her in her clubroom?"
    "Well..."
    "If Aijou Renpirou told Monika she'd have 100 club members..."
    "And Renpy-sama told me I'd get 100 girlfriends..."
    "She should be joining our club too."
    "I'd wish Monika was here so that I know."
    "..."
    "The bell rang."
    "Classes was over."
    "It's club time!"

    scene bg corridor
    with wipeleft_scene
    stop music fadeout 2.0

    "As I made my way towards the clubroom, I felt a strange feeling."
    "As if someone is stalking me."
    "Or maybe I'm just paranoid."
    "I got so focused on my surroundings that I never looked straight forward."
    "Which caused me to bump someone."
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    mc "Ow!"
    mc "Sorry I'm not looking ahea-- {w}Cara?"
    "Oh perfect. My new girlfriend showed up."
    "This will put me at ease for a bit."
    "I helped her get up."
    play music t4
    show cara 3z at t11
    c "I'm sorry too..."
    show cara 1y at h11
    c "I was so excited to see you in the clubroom!"
    c 1a "I'm on my way there right now!"
    mc "Eh?"
    mc "I thought you're from the karate club?"
    show cara 1y at f11
    c "Yes, I am!"
    c 1a "But I would like to join the Literature Club too!"
    c "For obvious reasons."
    c 3t "I want to spend time with you, my love."
    c 1y "But I managed to convince my club leader to permit me in joining multiple clubs."
    show cara 1a at t11
    c "I said that joining a literarure club would help me in my mental training."
    c "Karate or any martial arts in general is not just {i}all{/i} physical anyways."
    show cara 1y at h11
    c "And she totally agreed with me!"
    c "And approved of my decision!"
    mc "Sweet!"
    mc "Let's go together then, so I can introduce you to Sayori and others!"
    show cara at thide
    hide cara 
    "She really is joining our Literature Club."
    "I'm so excited to spend time with her!"
    stop music fadeout 2.0
    "But as we're walking towards the clubroom... I still feel the strange feeling earlier."
    "I was about to ask Cara about it, but she interrupted me."
    show cara 1d at t11
    c "Someone is watching us, isn't it?"
    mc "I was about to ask you about that..."
    mc "I feel that somebody is stalking us."
    c 1e "I felt it too..."
    c 1h "Show yourself, coward!"
    "No response."
    mc "I don't think that person will show up just because you said so."
    c 1e "It's worth a shot."
    c 1f "Let's just ignore that coward."
    c "Why don't you tell me the things that you do in the Literature Club instead while we're going there?"
    mc "Sure!"
    mc "It'll relieve me of the stress."
    show cara 1y at h11
    c "Alright!"
    show cara at thide
    hide cara 
    "We ignored the unsettling feeling and enjoyed each other's company while walking towards the clubroom."

    scene bg vm
    with wipeleft_scene

    $ k_name = '???'
    k "I almost had him."
    k "He's so lucky that he bumped into someone."
    k "But who am I kidding?"
    k "I'm a skilled assassin."
    k "I should be able to take down a high school girl."
    k "Even I'm wearing a school girl uniform I managed to get to infiltrate the school, It should be no problem."
    k "I'll guess I have to invite myself in the club."
    k "Damn you, [player]."
    k "I won't let you get close to Monika."
    k "You're not worthy of her."

    scene black
    with dissolve_scene_full

    pause(5.0)
    
    scene bg club_day
    with wipeleft
    play music t3

    show sayori 4r at t31
    show yuri 3m at t33
    show cara 3y at t32 
    s "Welcome to the Literature Club Cara!"
    s 1x "And welcome to '[player]'s Angels'!"
    y turned happ om oe "So what type of books you usually read?"
    show cara 3y at f32
    c "Thank you to both of you!"
    c 1a "As far as books is concerned, I only read books on how to improve my karate skills."
    c 1y "It's a fun read, because I'm striving to be a black belter soon!"
    "We are all having a great time in the club."
    "Sayori and Yuri welcomed Cara with open arms in the club."
    "Natsuki, on the other hand, is just ignoring us and is on the closet reading her manga."
    "Probably still felt salty from the last time she met her."
    "I hope they're going to get along as time goes by."
    "Out of nowhere, we heard a shout."
    k "I finally found you, [player]."
    show sayori 4m at h31
    show cara 3af at h32
    show yuri 3p at h33
    "We were startled by that voice."
    stop music
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show black
    mc "Agh!!"
    "Something was shot in my eyes."
    "I can't see!"
    k "Sorry, [player]. I'm gonna have to kill you."
    "{b}WAIT WHAT?{/b}"

    scene bg class_day
    with wipeleft

    "Okay. I have shot him in the eyes."
    k "Sorry, [player]. I'm gonna have to kill you."
    "This should be a piece of cake."
    y "Who are you?"
    show yuri 3y7 at t11
    play music "mod_assets/intimidation.ogg"
    y "Why did you hurt our boyfriend?"
    k "Boyfriend?" 
    k "Oh, so he's flirting with all of you as well."
    k "He really isn't worthy of Monika."
    y 3y3 "And you aren't worthy to live!"
    show yuri at face
    "Yuri approached me, holding a knife."
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    play sound "sfx/slap.ogg"
    show yuri 3y2 at t11
    k "It would take a lot more than knives to stop me."
    show yuri at lhide
    hide yuri
    "I pushed her aside."
    show sayori turned b1e e1h rup ml lup at t11
    s "I'm not afraid..."
    s "I won't let you hurt him!"
    s "We've faced an even bigger threat than you!"
    k "Oh, really?"
    k "You better step aside now, or I'll be an even {b}bigger{/b} threat than the person you're talking about."
    show sayori at h11
    s "Stop being a meanie!"
    show sayori at lhide
    hide sayori
    "I pusher her aside as well."
    "I'm in front of [player]."
    "This is the chance."
    k "Goodbye, [player]."
    k "You're not worthy of Monika, you'll never be."
    "Mission accomplished."
    "I am going to slice his throat."
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    play sound "sfx/slap.ogg"
    c "What do you think {i}you're{/i} doing?!"
    show cara 1h at t11
    c "You're the coward from earlier, are you?"
    c "I've sensed you following [player] from the corridor!"
    c "I won't let you just {i}kill{/i} him."
    c "And ruin this club."
    k "And I won't let you hinder my plans."
    "I charged forward towards her."
    "But surprise, surprise, she hit me with a good 3-hit combo."
    k "I see."
    k "You're pretty resilient."
    k "Guess I'll have to kick it up a notch."
    "I demonstrated my fighting skills against her."
    "Damn, she's pretty good in martial arts."
    "But not good enough."
    show cara at lhide
    hide cara 
    "I managed to knock her down after a few minutes."
    k "Weak."
    "Nothing's stopping me now."
    play sound "mod_assets/it.mp3"
    show natsuki turned rhip vang om lhip at i11
    n "What do you think {b}YOU'RE{/b} doing?!"
    "How did she get in here so fast?"
    show natsuki at thide
    hide natsuki
    "She punched me, which I blocked."
    k "What the--"
    "I was knocked back several feet away."
    "She has absurd strength."
    c "Natsuki..."
    show cara 1h at t21
    show natsuki 4g at t22
    c "She's trying to kill our boyfriend!"
    n "Oh?"
    n 4w "Then she has to go through us."
    n "Cara, you're one of us now."
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    n 4q "We have to work together."
    c "...Right."
    c "We can't let her kill him."
    k "Oh."
    k "With that absurd strength of yours and her fighting skills..."
    k "I guess I have to pull all the stops."
    "I pulled out my tranquilizer gun."
    k "I don't want to waste my darts for a measly task."
    k "But I guess I have to."
    show natsuki 4p at t11
    show cara at thide
    hide cara 
    "The pink-haired brute charged in first."
    "But I easily dodged her attacks."
    "It never connected."
    k "Guess my training for this technique paid off."
    c "That technique--"
    k "Time to sleep, pink-haired girl."
    show natsuki at lhide
    hide natsuki 
    "I tranquilized her."
    show cara 1h at t11
    c "How'd you know about the technique, {i}'Hyper Instinct'{/i}?"
    k "Who knows?"
    k "Time for you to sleep as well."
    c "I just won't let you!"
    "She charged at me with all that she got."
    "But to no avail."
    show cara at thide
    hide cara 
    "I tranquilized her as well."
    "Now with no one to stop me, I'm going to accomplish my mission."
    "To get rid of [player]."
    "He doesn't deserve to exist."
    "The martial artist still held my leg."
    c "I... just won't let you..."
    "She let go and fell asleep."
    k "Pathetic."
    stop music fadeout 2.0
    "I continued on and I'm in front of this wretched man."
    m "Hi, sorry I'm late again!"
    m "What the--"
    k "Monika?!"
    show monika 1i at t11
    m "Who are you?!"
    k "Monika!"
    show monika at face
    "I gave her a hug."
    k "I've been looking for you all these years!"
    show monika 1g at t11
    m "W-w-wait, who are you?!"
    m "Have we... met before?"
    k "It's me, Ken!"
    $ k_name = 'Ken'
    k "You saved me when I was a child..."
    k "I was hungry and about to die..."
    k "When you suddenly did your 'magic' and spawned a ton of food for me!"
    k "And from that day... {w}I promised myself to be your protector."
    k "I trained myself, and became a skilled assassin."
    "She tried to remember me..."
    show monika 1l at h11
    play music t3
    m "Oh!" 
    m "You're that homeless kid that I gave food, and shelter before!"
    m "It's nice to see you again!"
    m 1g "But seeing this mess here..."
    m "What happened?"
    m "Are you ruining my club?"
    k "This is your club?"
    k "Um, no I'm making it better."
    k "By eliminating the biggest threat to your club..."
    k "[player]."
    k "I have heard he's been flirting with other girls even though he's your boyfriend too."
    k "And I just can't accept him."
    m "Ken..."
    m "You have to accept my decision here."
    m "All of us here is his boyfriend."
    m 5a "And I'm okay with that."
    m 1r "Oh dear..."
    m "I have to fix this mess before the teacher finds out what happened here."
    $ run_input("os.restore club_day.png", "club_day.png restored successfully.")
    "Suddenly, all the broken tiles, tables, chairs were fixed."
    hide screen console_screen
    "As if nothing happened here."
    "Even the girls that I knocked out and tranquilized were restored."
    "Monika went over to the martial artist."
    show monika at t21
    show cara 1a at t22
    m "Thank you for protecting [player]."
    m 5a "And welcome to the Literature Club!"
    m "I heard from Sayori that you're joining!"
    c "Yes, I am!"
    c "And it's an honor to protect my knight and shining armor."
    c 3y "My love, [player]!"
    m lean happ om ce "Okay!"
    m "If you're his girlfriend as well, then you're more than welcome here!"

    scene bg club_day
    with wipeleft_scene

    "Oh?"
    "It seems that the commotion stopped."
    "And I can see again!"
    m "If you're his girlfriend as well, then you're more than welcome here!"
    "Oh. Monika's here now."
    "I tried to get up."
    m "Hi love."
    show monika 1a at t11
    m "I'm glad that you're okay."    
    m 1o "I'm so sorry about the commotion."
    m "And sorry as well that I'm a bit too late."
    mc "It's okay, Monika."
    mc "I'm not harmed."
    mc "I thank all my girlfriends that stood up for me."
    show monika at t32
    show yuri 1d at t31
    show sayori 1r at t33
    y "We can't just let her kill you."
    s "I... stood up for her even I can't do anything!"
    mc "I'm so proud of you both!"
    show sayori at thide
    show yuri at thide 
    hide yuri
    hide sayori 
    show cara 1a at t31
    show natsuki 1q at t33
    c "I have to stand up for you, you know?"
    n "... what they said."
    n "It's not like I'll enjoy your compliment to me or anything."
    mc "Natsuki... thank you."
    mc "And also you, Cara."
    mc "I love all of you!"
    show monika at thide
    show cara at thide
    show natsuki at thide
    hide monika 
    hide cara
    hide natsuki 
    "We all shared a big hug."
    mc "By the way, where is she?"
    m "Oh. She's still here."
    show ken 4p at t22
    show monika 3a at t21
    m "She's my childhood friend."
    m "I helped her through thick and thin."
    m 3n "Sorry if she acted being 'overprotective' for me to all of you."
    k "Ahhh..."
    mc "Ken...?"
    stop music fadeout 2.0
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show ken 4k at h22
    "{b}ZING!!!{/b}"
    "Wait, wait."
    "Another zing?!"
    "Renpy-sama, why would you give me a girlfriend that's almost tried to {i}kill{/i} me?"
    "But I guess I have to accept the she's my girlfriend."
    show monika forward vsur ml at h21
    play music t5
    m "!"
    m "[player]... was that a zing just now?"
    show sayori 4m at t41
    show monika at t42
    show ken at t43
    show yuri 3p at t44
    s "What, a zing?"
    y "I didn't expect this..."
    show sayori at thide
    show yuri at thide
    hide sayori 
    hide yuri 
    show cara 3q at t41
    show natsuki 4p at t44
    c "What?"
    n "What the heck, man. Why of all people!"
    mc "Uhhh... I'm surprised myself that I felt a zing!"
    show monika at thide
    show cara at thide
    show natsuki at thide
    hide cara
    hide monika 
    hide natsuki
    show ken 4ax at t11
    "I approached Ken."
    mc "Ken... I..."
    k "!"
    k 1aw "D-don't come closer!"
    k "I-- I still don't accept you to be fit for Monika!"
    mc "Why not?"
    k "If you lay your hands on her, I swear I'll kill you!"
    show ken at face
    "I held her up close."
    k 1bb "Khhh!"
    k "What are you d-doing? S-stop!"
    mc "I'll be fit for her. I promise."
    mc "I love my girlfriend Monika."
    mc "And so is everyone else around here."
    mc "Including {i}you{/i}..."
    k "Eh??? M-me too?"
    k "Then I love you too..."  
    show ken 1bb at t11
    k "W-wait! why did I say that?!"
    k 1bl "I have to get out of here!"
    show ken at lhide
    hide ken
    "She ran off the window and jumped off to a tree."
    mc "Ken!"
    show monika 1a at t32
    m "She'll come back."
    m lean happ ce om "She'll probably join the club too!"
    "The other girls groaned in disbelief."
    show natsuki 4e at t33 
    n "Oh, come on!"
    show cara 1h at t31
    c "Are we gonna ignore the fact that she almost {i}killed{/i} our boyfriend?"
    m 5a "I know, I know."
    m "But she really is harmless."
    m "She's just being overprotective."
    m "I can say she's got a bit of Natsuki in her."
    show natsuki 4p at f33
    n "Hey, hey, hey, what you mean, Monika!"
    n "I'm the only me in here!"
    show natsuki at t33
    m 3b "What I mean is that I think you share some personality with her."
    m "You'll get along eventually."
    m "And you, Cara. You'll probably want to engage a friendly sparring with her from time to time."
    m "Because I believe you'd like to know how to use {i}'Hyper Instinct'{/i} as well?"
    show cara 3l at s31
    c "Uh... I guess you're right."
    m "Okay, everyone!"
    m "In case that Ken comes back, please accept her with open arms."
    m 5a "I can assure you she'll be different from today."
    m "Okay, let's do our daily club activities today and get to know Cara a bit more!"
    show cara at thide
    show monika at thide
    show natsuki at thide
    hide cara
    hide monika 
    hide natsuki
    "We all celebrated Cara's joining in the Literature club by forming a table, eating cupcakes with tea, and chatting about her."
    "Cara is so excited with her new experience."
    "She'll get along with everyone else here."
    "Due to the 'assasination' incident, we skipped sharing poems today."
    "And before we know it, it's time to go home."
    stop music fadeout 2.0
    play music t8

    scene bg residential_day
    with wipeleft_scene

    "I'm walking home with Natsuki and Cara this time."
    "Sayori went home early and Yuri had to take some detour elsewhere."
    "And surprise, surprise, Natsuki's on my back again."
    "Cara's holding my hand."
    show cara 1a at t11
    c "You look very comfortable in [player]'s back."
    n "Shut up."
    n "You jealous?"
    "Natsuki teased Cara with a smug face."
    mc "I'm glad that both of you got along that time."
    mc "You don't hate each other anymore."
    n "Why would I hate her, anyway?"
    n "If she's your boyfriend and I hate her then it means I'd hate you."
    n "Yeah, I hate you... but not {i}hate{/i} hate you."
    "I dismissed her weird logic again."
    mc "And I love both of you."
    mc "That won't change."
    c 1y "I love you too, [player]."
    n "... uh, what she said."
    "Cara looked at Natsuki with a smug face."
    c "Go on, say it {i}literally{/i}."
    n "Alright!"
    n "I really, really, really, really love you, [player]!"
    n "There, Cara. Happy now?"
    "Cara chuckled."
    c "That's more like it. Ahahahahaha!"
    show cara at thide
    hide cara
    "We all laughed."

    scene bg house
    with wipeleft_scene

    "We arrived at my house."
    mc "The boyfriend stops here."
    mc "See both of you tomorrow!"
    "Natsuki gets off of my back."
    show cara 1a at t21
    show natsuki 1a at t22 
    c "Bye, [player]."
    c "I love you."
    n "Bye!"
    n 12c "I... also love you."
    mc "And I love both of you too."
    show natsuki at thide
    show cara at thide
    hide natsuki 
    hide cara 
    "They left."
    "Okay then..."
    "Time to have some alone time!"

    scene bg bedroom
    with wipeleft_scene

    "Today was a weird day."
    "But fun nonetheless."
    "6th girlfriend acquired, I guess."
    "But I almost died!"
    "Ken..."
    "I wonder if I'll see her again?"
    "She's Monika's childhood friend... she says."
    "I hope I'll see her."
    "I'll prove my worthiness for Monika."
    "By loving her, and all of them."
    "It's getting more and more exciting!"
    "I will be the best boyfriend ever."
    "I wonder who will be the next?"
    "I'll just leave it to Renpy-sama."
    "And the Modder."
    "Time to write more poems!"
    "I'd like to watch season 2 of my favorite anime..."
    "But it's not released yet."
    "Guess I have to read it's manga..."
    "There's a lot to think about."
    "Welp, I'll just have to do all of them then."

    scene black
    with dissolve_scene_full

    return

