label chapter_two:

    scene black
    with dissolve_scene_full
    play music m1

    $ video_game = False
    $ mystery_caller = False
    $ time_travel = False
    $ amy_spell = False 
    mc "..."
    mc "Man, I'm so tired..."
    r "Hi, [player]."
    mc "Eyyyy, Renpy-sama."
    r "How are you... tired?"
    r "You're body is currently {i}sleeping{/i} right now."
    mc "I don't know man."
    r "It's just your imagination."
    r "Anyways..."
    r "How are you doing with the current set of girlfriends you have right now?"
    mc "Bruh."
    mc "You always... surprise me with what you're giving to me."
    mc "I now have my childhood friend's {i}entire{/i} family."
    s "Hi, [player]."
    mc "Oh speaking of which..."
    show sayori tap casual nerv om at t11 
    if sayori_punch == True:
        s "Sorry about punching you yesterday."
    else:
        s "Sorry about what happened yesterday."

    mc "No worries, Sayori."
    mc "Say, where's Monika?"
    s 1bc "Oh, she said she's tired from all the work she did yesterday."
    show sayori turned casual neut at t11
    mc "I understand."
    mc "By the way..."
    mc "How is your mom going to be a club member?"
    s mi lup "Oh right..."
    s happ om "I think I can fix that..."
    s "Let me just do this..."
    $ run_input ("os.remove/[player]'s Boring Teacher", "NPC deleted succesfully.")
    s "And this..."
    $ run_input ("os.addrole/sayozuki.chr = 'Teacher'", "Added 'Teacher' role to sayozuki.chr.")
    s "And lastly... this."
    $ run_input ("os.set/sayozuki.chr/Intelligence = +2", "Intelligence points successfully added.")
    s "There that should fix her."
    hide screen console_screen
    mc "You do know your stuff."
    show sayori turned laug ce at h11 
    s "Ehehe~"
    s happ om e1f "I always know my stuff."
    s "Sometimes I {i}become{/i} stuff."
    show sayori 4br at h11 
    s "I'm stuff!"
    mc "Whar--"
    mc "Anyways. I'll have to trust the process that you did."
    mc "But why delete an innocent teacher?"
    s 1bl "Ehhhh, he also was a jerk in our class."
    mc "Really now?"
    mc "But hey."
    mc "If that's how you can get your mom in the school..."
    mc "I won't be complaining love."
    r "Sayori is brutal."
    r "She just straight up deleted a teacher."
    r "Well, not important..."
    r "But apparently that teacher is named Mr. Kenny..."
    r "..."
    r "Oh my God... She killed Kenny!"
    r "You bastard!"
    s turned casual anno e4a mi "Oh, shut it, Renpy-sama."
    s "Sacrifices are to be made for the greater good."
    s lup happ om oe "And besides, this would make the story even more interesting, ain't it?"
    r "Alright!"
    r "I won't question your ways."
    r "Monika trusted you."
    r "But let me just remind you, Sayori."
    s 1bc "With great power comes great responsibility."
    s "I rember what Modder said."
    r "Good."
    show sayori 4bx at face 
    play sound "sfx/fall.ogg"
    "Sayori started to hug me."
    s "Time for you to wake up, [player]."
    s 4br "I love you so much!"
    mc "I love you too."
    scene bg bedroom
    play sound "sfx/fall.ogg"
    stop music
    "I woke up."
    mi "Good morning sleepyhead."
    mc "Hi Mizumi."
    mc "How was you're talk with Kotonoha?"
    mi "It's a secret, [player]."
    mi "You'll find out soon enough."
    mi "Let me go and prepare for school."
    mi "Wait for me downstairs."
    "Mizumi went in the showers."
    mc "Well... I guess I'll go use the guest shower downstairs."
    scene bg kitchen
    with wipeleft_scene
    play music t2
    "After a refreshing shower... I hear someone in the kitchen."
    c "Let's see... "
    c "Agh, I can't decide which ones to make for [player]!"
    c "This is my first time cooking for him."
    a "Ah I burned my hand!"
    a "Cursed kettle."
    $ style.say_dialogue = style.edited
    a "Feel the power of my wrath, kettle!"
    $ style.say_dialogue = style.normal 
    c "Please don't break anything, Amy."
    c "[player] will be mad if we break anything."
    a "Oh right, sorry."
    mc "Good morning girls!"
    "I approached the two of them happily."
    show cara 1a at t21
    show amy turned happ om at t22 
    a "Hi, [player]!"
    c 1y "We missed you!"
    a cross sad mg "We're making breakfast for you..."
    a turned mc e1h n3 b1d lneck "But we can't seem to come to a conclusion on what to make for you!"
    show amy happ at t22
    show cara 1a at t21 
    mc "Girls..."
    mc "You don't have to worry about what you're making for me."
    mc "I'd indulge in whatever breakfast you're going to make."
    mc "Want me to help you both?"
    show amy turned mc b1d lback rback at s22 
    a "We would love to but..."
    c turned lbehind rhold be ec mb "We would really love to make something for you that you will be pleased."
    show amy turned happ at t22 
    s "You'll probably need my help then."
    show sayori 1x at l31
    show cara 1a at t32 
    show amy at t33 
    "Sayori shows up in my house."
    show sayori at f31 
    s "I'll help you in whatever you're making."
    show sayori 4r at h31 
    s "I sure know what [player] likes!"
    a 1ke "That's great then!"
    c turned ba ef mb "Alright, let's get to work then."
    hide sayori
    hide amy 
    hide cara 
    with wipeleft 
    "They started to work on the breakfast they're making."
    "Soon me and Mizumi joined in the kitchen and waited for the three of them."
    "We all had a wonderful breakfast together."
    "We ate a lot and hit the road to go to school."
    scene bg residential_day
    with wipeleft_scene
    "All 5 of us are walking together happily down the road."
    menu:
        "So I guess, it's time for me to have some fun!"
        "Ruffle Sayori's hair." if not sayori_punch:
            "I decided to approach Sayori."
            "And carefully ruffled her hair."
            s "Ehehe~"
            show sayori turned sedu mb at t11 
            s "You're turning me on again, [player]~"
            s "We might just skip class and go back to my room instead~"
            mc "..."
            show sayori 4r at h11 
            s "I'm just kidding [player]."
            show sayori 4a at face 
            play sound fall
            s "That is why I love you, [player]."
            s 4r "You never fail to make me feel happy."
            mc "I love you too, Sayori."
            show sayori 1x at t11 
            s "Shall we continue walking?"
            mc "Of course, ma'am."
            show sayori at thide 
            hide sayori 
            "We continued walking until we arrived at the school."
        "Walk with Cara.":
            "I approached Cara."
            "She seemed to be reading a manga from her phone."
            mc "Hey, Cara."
            c "O-oh!"
            show cara 1f at t11
            c "I'm reading 'Parfait Girls' right now."
            c "Natsuki told me there's this mobile app that has all the manga I can read."
            mc "Oh yes."
            mc "You can read manga everywhere nowadays without buying one at the store."
            show cara turned lbehind rhold mb ec be at s11
            c "But I really want a manga collection of my own..."
            show cara 1f at t11 
            c "Just like Natsuki!"
            mc "I'm pretty sure you will, Cara."
            show cara turned lbehind rhold nc ma ee be at face 
            play sound fall
            c "I love you, [player]."
            mc "I love you too."
            show cara 1f at t11 
            c "Alright, shall we continue walking now?"
            mc "Of course."
            show cara at thide 
            hide cara 
            "We continued walking and Cara resumed reading her manga."
        "Hold hands with Amy.":
            $ amy_spell = True
            "I decided to approach Amy."
            "She seems to be chanting something."
            mc "Amy?"
            a "[player]?"
            show amy turned happ om at t11 
            a "Hi, [player]."
            a lspecs "I'm currently practicing a spell I just read in the Dark Arts book I have."
            a "It's a neat spell, but it's {i}really{/i} difficult."
            mc "I'm sure you can do it, Amy."
            mc "You already brought Sayori back to life."
            a ldown mg "This one is really complicated."
            a "But it is {i}very{/i} powerful."
            a "I'll practice it so that I can use it if situations are dire."
            mc "Well, keep practicing!"
            mc "I believe you can do it!"
            a b1d "Thank you, [player]."
            show amy cross happ cm at face 
            play sound fall 
            mc "I love you, Amy."
            mc "You're very important to me, so please be careful with your spells."
            mc "You might turn into a frog or something."
            mc "But I'll love you nonetheless!"
            a blus "I love you too, [player]."
            a nobl ce om "No worries, I won't turn into a frog or whatnot."
            show amy oe at t11
            a "Alright, we need to continue walking now."
            mc "Okay, milady."
            mc "Shall I hold your hand?"
            a ce "You bet!"
            show amy at thide
            hide amy 
            "We held hands as we continued walking."
        "Talk with Mizumi.":
            "I decided to approach Mizumi."
            "She's happily frolicking towards the school."
            mc "Seems like someone's happy."
            mi "O-oh!"
            show mizumi 1a at t11
            mi "Hi, [player]!"
            mi 3i "I didn't notice you approaching."
            mi 1b "I'm just in a good mood today."
            mc "That's great to hear."
            mc "I wonder what future me is thinking right now."
            mi 2b "He's probably proud of you, my love."
            mc "No, my love."
            mc "He's proud of {i}you{/i}."
            mc "You saved his life."
            mc "You saved the others' lives as well."
            show mizumi 3v at s11 
            mi "Ehehe~"
            mi "I'm a bit flattered..."
            show mizumi 1a at face 
            play sound fall
            mc "You don't have to be ashamed on what you did."
            mc "We couldn't have been in this point without you're doing."
            mc "That's why I love you, Mizumi."
            mi 1v "Ehehe~"
            mi "I love you too, [player]."
            show mizumi 1b at t11 
            mi "Alright, we better get going."
            mc "Of course."
            show mizumi at thide 
            hide mizumi 
            "We walked together until we arrived at the school."

    scene bg class_day
    with wipeleft_scene

    "..."
    "It's going to be boring again."
    "Until our principal walked in our room."
    pr "Alright, class."
    pr "For some reason, the main teacher here in this classroom {i}disappeared{/i} without a trace."
    pr "But no worries!"
    pr "You're gonna have a new teacher that'll teach you."
    pr "Please welcome, Ms. Sayozuki!"
    "Wait, what?"
    show sayozuki 1bb at t11 
    sz "Greetings, class."
    sz "I will be the teacher here from now on."
    "Oh... yeah."
    "I remember Sayori deleting our teacher and replacing him with her mom."
    a "[player], she looks very similar to Sayori."
    mi "Yeah, she does awfully look like Sayori."
    mc "That's because she's her mom."
    a "Oh!"
    mi "Well that makes sense then."
    sz 4bb "Ms. Sayozuki..."
    show sayozuki 4be at h11 
    sz "At your service!"
    sz 1bm "Oh... I'm seeing a familiar face..."
    sz 4be "It's [player]-chaa--{nw}"
    show sayozuki 4bq at s11
    pause (0.5)
    show sayozuki at t11
    sz "[player]."
    show sayozuki 1ba at t11 
    "Dear Renpy-sama."
    "That would cause a scene if she did that."
    "One student asked if she knew me."
    sz 1bb "Of course I know him."
    sz 3bb "He's been childhood friends with my daughter."
    sz 1be "I'm gonna say he's a part of our {i}family{/i}."
    sz 4bb "Without further ado, let's go and start our lesson..."
    show sayozuki at thide 
    hide sayozuki
    "Now it's really getting interesting."
    "As far as the lessons she's teaching, she's doing a pretty good job."
    "I enjoyed her teaching so much that I lost track of time."
    "Classes was over before I knew it."
    mc "Amy, Mizumi, let's go to the club!"
    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene
    "As we make our way into the club, someone familiar approached us."
    sz "Hi, [player]-chan."
    play music t4 
    show sayozuki 1ba at t32 
    "Sayozuki seems to be eager in seeing me."
    mc "Hello, Ms. Sayozuki."
    mc "How's your first day of teaching?"
    sz 3bb "It's been great!"
    sz 1be "I'm getting the hang of it."
    sz 1bf "I've only taught my daughters in the home."
    sz 1bg "But I haven't really taught that many people..."
    show sayozuki 1bj at h32 
    sz "I'm really nervous!"
    a "Hi, Ms. Sayozuki."
    show amy turned happ om at t31 
    a "You're Sayori's mom?"
    sz 3bb "Yes, Amy."
    sz "Thanks for being good friends with her."
    mi "Hello, Ms. Sayozuki."
    show mizumi 1b at t33
    mi "How did you become our teacher, by the way?"
    sz 2bb "Well..."
    sz 2bf "Sayori just told me since I'll be moving back with her..."
    sz 4bb "I could be a teacher in this school."
    sz 1be "And what do you know... they have an open spot for teachers!"
    mi 1f "Also..."
    mi "Why did you call our boyfriend {i}'[player]-chan'{/i}?"
    sz 1bf "Oh..."
    sz "So you're also his boyfriend..."
    a cross curi om "...Also?"
    mc "Yes, Amy."
    mc "She's my girlfriend too."
    show mizumi 3c at h33
    show amy turned shoc cm at h31 
    "Both of them were surprised."
    s "Hi, guys!"
    show sayori 1x at l41
    show amy at t42 
    show sayozuki at t43 
    show mizumi at t44 
    "Sayori meets us along the way."
    s 3c "Oh, hi Mom."
    s "You're already with them."
    s 1j "I hope you haven't said or done anything weird."
    mi 2f "Well, your mom {i}almost{/i} called [player] '-chan' in  front of the whole class."
    show sayori 4j at h41 
    s "Mom!"
    s "You shouldn't say that in front of everyone, It's weird!"
    show sayozuki 1bj at h43 
    sz "I'm sorry!"
    show sayozuki 1bh at s43 
    s turned anno ce om lup "Please put on best behaviour, Mom."
    show sayori om at t41
    mc "Sounds like Sayori's the mother here."
    show sayori 1r at t41
    show amy 1ke at t42 
    show sayozuki 1bk at t43 
    show mizumi 1g at t44 
    "The four of us laughed."
    show amy turned neut lspecs om at t42 
    a "By the way Sayori... is it really {i}true{/i} that she's also [player]'s girlfriend?"
    s 2c "Yes."
    s 1x "That's why I'm making sure she's on her best behaviour."
    s turned nerv om "She can be... {w=1.5}{i}too wild{/i}, I might say."
    a ldown happ "Oh okay."
    "Well, we have to get to the clubroom now."
    sy "Wait for me!"
    show sayo 1d2 zorder 2 at t51 
    show sayori at t52
    show amy zorder 2 at t53 
    show sayozuki at t54
    show mizumi  zorder 2 at t55 
    "Sayo runs towards us."
    sy "You're not gonna leave your livvy dunne, aren't you baby gronk?"
    mc "Hi, Sayo!"
    mc "Of course I'm not gonna leave you."
    mc "Let's go now!"
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t3 
    "All 6 of us arrived at the club."
    m "Hello, [player]!"
    show monika 4b at t11 
    m "And It seems we have new members in the club."
    m "Also, Hi, Ms. Sayozuki."
    m 5a "I heard you're the new teacher that we had."
    m lean om ce "Nice to meet you."
    m 3b "Are you gonna be our club supervisor?"
    show sayozuki 1bb at t22
    show monika at t21 
    sz "Yes, Monika."
    sz 3bb "I'm also assigned to supervise Kotonoha's debate club."
    show kotonoha toward happ om at t33
    show monika at t31
    show sayozuki 1ba at t32
    "Kotonoha also walks towards us."
    kt "Oh, so you must be Ms. Sayozuki."
    kt lup "Hello! Kotonoha here."
    kt ce ldown "Looking forward to work with you."
    kt toward oe b1e md lchest "I'm currently running the debate club and being a club member in here as well."
    kt ce "That's how better I am than Monika!"
    m forward anno om "Shut it, Kotonoha."
    m 5a "You joining this club is enough proof that I'm running this club better than you run yours."
    show monika lean happ om ce at h31 
    m "You're probably bored out of your mind in the debate club."
    show monika 5a at t31 
    show kotonoha toward angr ce mb rchip at s33 
    kt "I'm only joining your club because of my boyfriend, [player]."
    kt happ mc b1e e1a "I'm putting up a very good job maintaining my club and still having fun with my boyfriend here."
    kt ce "I'm built {i}that{/i} different."
    sz 3bb "Now, now, you two."
    sz 1be "It would be better if you just get along, okay?"
    sz 1bb "Being the mother of the 3 lovely buns that you see around here is challenging."
    sz 3bf "Before, they argue everyday, even on the simplest things."
    sz 1bb "But look at them now..."
    sz 1be "They're just getting along pretty fine."
    show monika 1a at t31 
    show sayozuki 1ba at t32 
    show kotonoha toward happ at t33 
    "We all look at how Sayori, Sayochi and Sayo arrange the tables in the center for us to sit on later."
    sz 1bb "I say... "
    show sayozuki 1be at h32 
    sz "Let's all get along and be the best boyfriend for [player]!"
    m 1b "Oh, so you're [player]'s boyfriend as well?"
    sz 1be "Yes!"
    m 3b "Alright then!"
    m lean happ om ce "You're more than welcome here in the Literature Club!"
    m 1b "Let me go ahead and do some paperwork for the others."
    show monika at lhide 
    hide monika 
    kt om "Alright, I'll go ahead and talk to the others as well."
    kt e3b "Also... If you don't mind, I'd like you to help me with something."
    sz 1bb "What would that be?"
    kt oe "Me, Sayochi and the others will work with me on something that we're preparing for the school event."
    sz 4bb "Sure, I'll be happy to help."
    kt "Great!"
    kt ce "We'll meet at our special place this Saturday, please do come along with Sayochi."
    kt oe lup "Alright, nice to meet you, Ms. Sayozuki."
    show kotonoha at rhide 
    hide kotonoha 
    show sayozuki at thide 
    hide sayozuki 
    "They also left to do their own thing."
    "Everyone seems to be doing something."
    menu:
        "Who should I spend time with today?"
        "See Monika and the others.":
            "I checked on in Monika and the others."
            stop music fadeout 2.0
            scene bg class_day 
            with wipeleft_scene
            play music t6 
            "Monika is doing paperwork."
            "Ken is still reading a novel beside her."
            "And Sayochi is reading alongside Ken in a nearby desk as well."
            "Hello, girls!"
            show monika 1a at t32
            show sayochi 1 at t31
            show ken 1a at t33
            "All of them stopped what they're doing and looked at me."
            m 1b "Oh hi, [player]."
            k "Hello, [player]."
            k 2b "I'm in a good mood today, so I'll let it slide."
            sc turned mb "Hi, [player]!"
            mc "How are all of you?"
            sc "I'm currently reading a novel that Kotonoha asked me to read."
            sc lpoint "It's pretty good."
            k 1e "Oh yeah."
            k "Cara gave me something to read that she said I'll be interested."
            k "Well, as far as I saw the cover and the first pages, it's a tragic manga or some sort."
            k 2ad "I'm not really interested in manga, let alone tragic stories..."
            k 1e "But she insisted that I read this and give her thoughts in it."
            k "Well, I guess I should be reading it then."
            mc "Ken, it's a good manga."
            mc "Do you want me to read it with you?"
            k 1b "I'm in a good mood right now."
            k "Sure."
            m 3b "And I'm still doing paperwork for Sayo."
            m "Also doing some preparations for the school event next week."
            m 5a "You can go ahead and spend time with Ken here."
            m "She misses you to be honest~"
            k 1f "Monika!"
            k "I don't miss him!"
            m "Oh you just told me yesterday that~{w=1.0}{nw}"
            k "I don't mean it!"
            "She definitely means it."
            mc "Shall we start reading the manga, Ken?"
            k 1ad "Oh fine!"
            k 1j "Just don't be weird again and look at me all the time."
            mc "No worries, I won't."
            hide monika 
            hide ken 
            hide sayochi 
            with wipeleft 
            "We started to read the manga." 
            "She's just quiet reading it, I'm not really sure if she's invested."
            "But she seems to be turning the page a little bit too fast."
            "She finished the book in less than half an hour."
            k "Well..."
            show ken 2b at t11
            k "I'm just gonna say that it's not that bad."
            k 1b "Well, after the club is over I need to return this to Cara."
            k "And give my opinion about it."
            k "I enjoyed it nonetheless..."
            "And Ken softened her voice."
            k 1an "Because I'm with you."
            mc "I enjoyed it too."
            mc "Nobody heard you, no worries."
            mc "I love you."
            show ken 4aw at s11 
            k "Alright fine..."
            "She mutters in a soft voice."
            k "I... love you too."
            show ken 4g at t11 
            mc "Thanks for spending time with me."
            show ken at thide 
            hide ken 
            "Ken smiled slightly as she sat down and laid her head on the desk."
            m "Alright, I'm done doing the paperwork."
            m "Let's all gather together and do something fun!"
            "Oh, club time is almost over."
        "See Cara and the others.":
            "I want to see what Cara and others are up to..."
            stop music fadeout 2.0
            scene bg closet
            with wipeleft_scene
            play music t6
            "I see Cara and Natsuki sitting on one corner reading manga."
            "I also see Sayo sitting on another corner watching DokiTube shorts."
            "I approached Sayo and talked to her."
            mc "Hello, Sayo."
            "Sayo looked up and saw me."
            sy "Hi, baby gronk!"
            show sayo 1d2 at t32 
            "Sayo greeted me with a cheerful smile."
            mc "How's my girl doing so far here in the club?"
            sy 1l "Nothing really interests me that much."
            sy "I prefer watching DokiTube shorts than reading, my rizzler."
            mc "Sayo..."
            mc "That's not how this club works."
            sy 1u2 "But..."
            sy 1w2 "There's no skibidi bathtub action figures to play..."
            sy "No video games to fanum tax victory royale..."
            show sayo 1v2 at h32 
            sy "Nothing to captivate my attention span!"
            sy 1q2 "The two big sis here beside me invited me to read manga..."
            sy "But books don't really pique my interest."
            show sayo 1n2 at t32
            mc "Sayo..."
            mc "The world offers more fun things than just video games and action figures."
            mc "Look at me."
            mc "I was a NEET before meeting all of my girlfriends, including you."
            mc "I thought games and anime are the best thing that I could ever have in my life."
            mc "That's why I don't go out much before."
            mc "Because for me, games and anime is love, games and anime is life."
            mc "But look at me now."
            mc "I'm able to enjoy all the fun the world offers because I stepped out of my box."
            mc "I'm able to be your boyfriend."
            mc "I'm able to meet {i}you.{/i}"
            show sayo 1k2 at t32 
            "Sayo perked up from what she heard from me."
            sy "Really?"
            mc "Yes."
            mc "I'm gonna say this to a term you'll understand..."
            mc "Let's {i}'fanum tax'{/i} the crap of this world of all the fun things it gives!"
            sy 4d2 "You're learning so quick, my baby gronk!"
            sy 1x "Alright, what should we do today then?"
            mc "Let's start by joining Cara and Natsuki read manga."
            sy "Alright, let's do it!"
            show sayo at thide 
            hide sayo 
            "We then approached Natsuki and Cara who are currently engrossed in their manga."
            mc "Hello, girls!"
            "They looked up and saw both of us."
            show cara 1f at t21 
            show natsuki 1a at t22 
            c "Hello, [player]."
            show cara 1a at t21 
            show natsuki 1d at t33
            n "Hello, um... Sayori's sister?"
            sy "Yes, that's me, fam."
            sy "Sayo, the GOAT, the chad, the L99 rizzler god."
            mc "May we join reading manga with you?"
            "Natsuki and Cara perked up."
            show cara turned mb ef ba at h21 
            show natsuki 1z at h22 
            nc "Sure, you can join us!"
            show cara at thide
            show natsuki at thide 
            hide cara 
            hide natsuki
            "All four of us read Natsuki's manga."
            "Sayo is actually invested in it."
            "She's intently looking at the manga."
            "We finished another volume of it."
            show sayo 1d2 at t32 
            sy "That was pretty good."
            sy 4d2 "I liked it!"
            mc "See, Sayo. there's more than just Dokitube shorts."
            show natsuki 1y at t33 
            n "And you'll see more!"
            n 1d "Hey, Cara! let's spar!"
            show cara turned mb bb at tf31 
            c "You bet!"
            show cara at lhide 
            hide cara 
            show natsuki at rhide 
            hide natsuki 
            "Oh, they're sparring again."
            play sound punch
            pause (0.5)
            play sound it
            pause (0.5)
            play sound punch 
            pause (0.5)
            play sound it 
            pause (0.5)
            show sayo 1m at h32 
            sy "Woah!"
            sy "They're going at it!"
            sy "Just like the game I just recently played!"
            sy "Shining Zero!"
            mc "Wait, you had that game already?"
            sy 1x "I just bought it online yesterday!"
            mc "I really wanted to play that game ever since it came out..."
            mc "I just don't have the budget to buy one!"
            sy 1d2 "Well ain't that a coincidence, baby gronk!"
            sy 1y2 "It just so happens that for some reason, I ordered two copies!"
            sy 2c "Well, the first order took too long to arrive so I ended up ordering another one."
            sy "But after the second one arrived, the first order immediately came through."
            sy "And Mom said it's not polite to send these delivery men home refusing the order..."
            sy "So I ended up buying both copies."
            sy 4l2 "I can give one to you if you want it~"
            mc "Are you sure about that?!"
            sy 1z2 "Of course, baby gronk!"
            sy 3y2 "Only if you beat me in a 1v1 match."
            $ video_game = True
            mc "It's a deal then."
            m "Okay, everyone!"
            m "Time to gather together to do something fun!"
            show sayo at thide 
            hide sayo 
            "Oh, club time is almost over."
        "See Sayori and the others.":
            "I'll check on in Sayori and the others."
            stop music fadeout 2.0
            "I approached Sayori."
            "She seems to be reading with Yuri and Amy."
            play music t6 
            s "Oh no... Run away!!!"
            a "Sayori..."
            a "It's not that scary..."
            s "It's so scaweeee..."
            y "Sayori... that's not even the scary part."
            "Typical Sayori."
            mc "Hi, girls."
            s "[player]!"
            show sayori 4p at t32 
            s "I can't take reading 'Portrait of Markov' anymore..."
            show yuri turned anno om e4a lup rup at t31 
            y "Hi, [player]."
            y om "We need your help to calm Sayori down."
            show amy turned worr om lback rback at t33 
            a "She's just like that ever since we started reading."
            show yuri cm at t31 
            show amy cm at t33 
            mc "Sayori..."
            show sayori turned cry at s32 
            "I headpatted her."
            mc "Alright. I'll read with you."
            show sayori om at t32 
            s "But [player]..."
            mc "It's alright."
            mc "Yuri, Amy, you can go ahead and continue reading."
            mc "I'll read with Sayori beside you."
            show yuri at thide 
            show amy at thide 
            hide yuri 
            hide amy 
            "I sat down with Sayori beside Yuri and Amy."
            "I pulled out my own copy of 'Portrait of Markov' and started reading to her."
            mc "What was the page that you we're reading?"
            a "I think it was chapter 4."
            mc "Alright."
            mc "Chapter 4..."
            show sayori at f32 
            s "Noooooooooooo..."
            mc "I'm here, Sayori."
            mc "Let's start reading here."
            show sayori at thide 
            hide sayori 
            "Sayori is really scared."
            "But after a few sentences in, she calmed down."
            "Of course, her boyfriend is here."
            "She's clinging on to me hard."
            "We managed to finish one chapter without any emotional breakdown."
            mc "There."
            mc "You okay, Sayori?"
            s "Yes."
            y "Sheesh."
            a "Thank you, [player]."
            mc "No worries."
            mc "Oh... by the way..."
            mc "How's the manga, Yuri?"
            show yuri turned happ om at t11 
            y "Oh..."
            y lup rup "It was interesting..."
            y ce "I liked it."
            y "I'm looking forward now to their performance."
            mc "Good thing that you liked it."
            y oe mi "I don't hate manga to be honest."
            y neut om ce ldown rdown "It's just not my preference."
            y "I prefer novels that'll take my imagination for a spin."
            mc "I see, I see."
            m "Okay, everyone!"
            m "Let's do something fun together today!"
            show yuri at thide 
            hide yuri
            "Oh, club is almost over."
        "See Mizumi and the others.":
            "Let's check on in Mizumi."
            stop music fadeout 2.0
            play music t6
            "Mizumi seems to be discussing with Kotonoha and Sayozuki."
            "I decided to approach them."
            mc "Hello, girls!"
            "Mizumi was the first one to notice."
            mi "Hello, [player]."
            show mizumi 1b at t11
            mi "How are you doing today?"
            mc "I'm doing great!"
            mc "How about you?"
            mi 1g "I'm doing great as well!"
            show mizumi 1a at t32 
            "Kotonoha and Sayozuki also noticed my presence."
            show kotonoha toward happ lup om at t31 
            kt "Hello, [player]!"
            show sayozuki 1bb at t33 
            sz "Hi, [player]-chan!"
            mc "Hello to the both of you!"
            show kotonoha ldown at f31 
            kt "We're just discussing the things we're doing for the school event."
            show sayozuki 3bb at f33 
            show kotonoha at t31 
            sz "It's a secret."
            sz 1bb "You'll know soon enough."
            show sayozuki 1ba at t33 
            show mizumi 1b at t32 
            mi "We're not spoiling the surprise, you know..."
            mc "It's alright."
            mi "While they're discussing in there, let's spend time together for a bit."
            mc "Oh alright."
            hide kotonoha 
            hide mizumi 
            hide sayozuki 
            with wipeleft
            "They're really hiding something."
            "But I dismissed the thought and talked to Mizumi."
            scene bg class_day
            with wipeleft_scene
            "Mizumi initiated the conversation."
            show mizumi 1i at t11 
            mi "I'm sorry if I had to pull you away."
            mi "It's a surprise."
            mc "It's alright, Mizumi."
            mc "I don't want to spoil it."
            mi 1b "Let's forget about that for a moment."
            mi "I wanted for us to have a date in the future timeline or something."
            mi "And I also wanted to bring everyone else as well."
            mc "That sounds cool and all..."
            mc "But I thought you can only bring one?"
            mi 1f "I'm currently working on harnessing the full potential of this Time Travel Ring."
            mi "I'm going to convert this to a bracelet so that it has more power and range."
            mi "I'm currently gathering the materials needed from the future."
            $ time_travel = True
            mi "Once it is finished, I will certainly take all of us into the future."
            mc "I'm excited and definitely will be looking forward to that!"
            show mizumi 1g at h11 
            mi "Of course you'd be excited!"
            mi 2b "I can't wait for everyone to see the future as well."
            m "Okay, everyone!"
            m "Let's gather around and do something fun!"
            show mizumi at thide 
            hide mizumi 
            "Oh, Monika's calling."
        
    scene bg club_day
    with wipeleft_scene
    stop music fadeout 2.0
    play music t5 
    "Well, it's time for our first activity together with Monika."
    m "Okay, everyone!"
    show monika 1b at t11 
    m "Since the school event is happening around the corner..."
    m 3b "And the Literature Club will be performing a play for the event..."
    m 3k "I think what we're going to do is to try to roleplay a scene on whatever literature you read."
    m 5a "Consider this to be a practice for Natsuki and for the others that help her."
    m lean happ ce om "Let's all help each other so that the club will get merits!"
    e "Okay!"
    show monika at thide
    hide monika 
    "All of us took turns in performing some sort of act in front of everyone."
    "Some reenacted scenes straight from an action film, some romance, and some just reenacted what they did this morning for breakfast."
    "We all had fun."
    "Until club time is over and we have to go home."
    play music t8 
    m "Let's pack up and call it a day, everyone!"
    "I'm ready to go home."
    if time_travel == True:
        mi "[player], I'm going back to the future so that I can continue my project."
        mc "Keep safe my love."
        play sound it
        "Mizumi went back to the future."
    else:
        pass
    show sayori 1x at t11 
    s "Let's go home together, [player]."
    mc "Of course!"
    "We started to walk towards the corridor."
    scene bg corridor
    with wipeleft_scene
    "My girlfirends are waiting for me outside."
    show sayo 1d2 at t51
    sy "Let's go home, my baby gronk!"
    show kotonoha toward happ lup om at t52 
    kt "Mind if I join in walking home with you today?"
    show yuri 1b at t53
    y "I missed walking home with you..."
    show natsuki 4d at t54
    n "Are you ready to carry me again on your back?"
    if time_travel == True:
        show sayori 4r at t55 
        s "This is going to be fun!"
        hide sayo
        hide kotonoha 
        hide yuri 
        hide natsuki 
        hide sayori 
        with wipeleft
    else:
        show mizumi 1b at t55 
        mi "Let's go, my love!"
        s "This is going to be fun!"
        hide sayo
        hide kotonoha 
        hide yuri 
        hide natsuki 
        hide mizumi 
        with wipeleft

    "I'm so happy right now."
    "Being with my girlfriends makes my day."
    "And they're with me everyday, so my day is always made."
    "We started to hit the road home."
    scene bg residential_day
    with wipeleft_scene
    "And here we are again at this moment."
    menu:
        "So I guess it's time for me to have fun!"
        "Talk with Mizumi." if not time_travel:
            "I approached Mizumi."
            mc "Hello, my love."
            mi "Hi, my love!"
            show mizumi 1a at t11
            mi "I'm always happy to see you."
            mc "You will always see me."
            mc "We sleep at the same room, we live at the same house, silly."
            mi 1g "That's why I'm always happy."
            mi 4z "I'm privileged to live the same house as you do."
            show mizumi 1a at t11 
            mc "And I'm privileged to spend time with you everyday."
            mc "Thank you for coming into my life."
            mi 1g "No problem with that, my love."
            show mizumi 1v at face 
            mc "I love you, Mizumi."
            mi "I love you too, [player]."
            show mizumi 2q at t11 
            mi "I'm still waiting for that {i}child{/i} you promised me."
            mc "..."
            mc "Um..."
            show mizumi 1g at h11 
            mi "I'm just kidding!"
            mi "Let's hold hands while walking."
            mc "Okay!"
            "We held hands as we walked home."
        "Walk with Sayo.":
            "I approached Sayo."
            sy "So Big Sis Sayori, how did you meet baby gronk?"
            s "Well..."
            mc "Yeah, Sayori. How did we meet each other?"
            sy "Hi baby gronk!"
            show sayo 1a at t21 
            show sayori 4m at t22 
            s "You caught me off guard there!"
            s tap pout "Meanie..."
            s turned happ om lup "But that aside..."
            s "I met [player] while he was out doing errands."
            s nerv "I'm so silly that time that I bumped into him."
            s "Then for some reason, I scraped my knee."
            show sayori worr ce ldown at s22 
            s "Of course, little Sayori cried."
            show sayori 3x at t22
            s "But he reached out to me and put bandages on my knee."
            s "He apologized and we walked home together that day."
            s 1x "And when he realized our houses are beside each other..."
            s 4r "He's been coming over ever since!"
            show sayori 1a at t22 
            mc "Well, to be fair, I was playing with my BoyGame while walking."
            mc "It is technically my fault as well."
            if video_game == True:
                sy 1k2 "Speaking of games..."
                sy 1x "I hope you're ready to face me in Shining Zero!"
                sy 1d2 "I'm gonna tell you now, I'll be whoopmaxxing your ass!"
                sy 4y2 "Don't think that me being your girlfriend will make me go easy on you!"
                sy 4z2 "HehahehaheHAHA!"
                mc "You're on!"
                mc "We're going to be playing after the school event okay?"
                sy 1d2 "Yeah, sure!"
                sy "You will take the L!"
            else:  
                pass
            mc "Anyways..."
            mc "Care to hold hands with me?"
            sy 1r "You bet, baby gronk!"
            s "Of course, [player]!"
            "We held hands until the rest of the walk."
        "Talk with Kotonoha.":
            "I walked towards Kotonoha."
            mc "Hello, Kotonoha."
            kt "Oh?"
            kt "Hi, [player]!"
            show kotonoha toward happ om at t11 
            kt "I have been practicing my Rock, Paper, Scissor skills."
            kt ce lchest "And I'll make sure that I win this time!"
            show kotonoha oe cm ldown at t11 
            mc "Oh?"
            mc "Well then, Kotonoha."
            mc "I guess it's time to d-d-d-duel again!"
            show kotonoha at thide 
            hide kotonoha 
            "We played a few rounds of RPS."
            "And... she still didn't win."
            kt "This is not fun at all!"
            show kotonoha toward anno om at t11
            kt "How are you winning?"
            kt "Are you cheating?"
            kt happ om "I'm gonna beat you next time, [player]."
            mc "It's not about winning, Kotonoha."
            kt "It's about FUN!"
            show kotonoha toward cm at t11 
            mc "You're learning, Kotonoha."
            mc "If you just think that every game you play is you're having fun, then you wouldn't be sad if you lose."
            mc "Of course, winning is just a bonus."
            kt lchest om "I'll take that advice at heart."
            kt ldown ce "I love you!"
            mc "I love you too!"
            "As we have fun talking, we didn't notice that we're getting close to my house."
        "Talk with Yuri.":
            "I approached Yuri."
            mc "Hello, Yuri."
            "Yuri seems to be talking to someone on her phone."
            $ mystery_caller = True
            y "For the last time, no, I'm not going there!"
            show yuri turned anno at t11 
            "Yuri seems to be annoyed at the person she's talking with."
            y vang om "Screw you!"
            show yuri cm at t11 
            "I haven't seen her this angry."
            show yuri turned vang mp e3a brow at h11 
            $ style.say_dialogue = style.edited
            y "If you lay... your hands on him..."
            y "I'll fucking kill you!"
            $ style.say_dialogue = style.normal 
            show yuri anno ce cm at t11
            "She almost threw her phone away."
            "What made her so mad like that?"
            "Time for me to comfort her."
            mc "Yuri..."
            show yuri neut oe mh at t11 
            y "Oh?"
            y worr om "[player]..."
            mc "Are you ok?"
            y mb "Y-yeah..."
            y "There's nothing to worry about."
            mc "I never saw you angry like that."
            y mg rup lup "Well... it's just some issues."
            y ce "I can handle it on my own..."
            mc "I sure hope so..."
            show yuri at face 
            play sound fall
            mc "I don't want you to be stressed like that."
            mc "I'm here, okay?"
            mc "If you need to tell me something, just tell me."
            y mb "... O-okay."
            mc "I love you."
            y happ om "I love you too."
            show yuri cm at t11 
            mc "Well, let's hold hands while we walk home, okay?"
            y om "Alright."
            show yuri at thide 
            hide yuri 
            "We held hands until we reached my residence."
        "Carry Natsuki in your back.":
            "I approached Natsuki."
            mc "Hey Natsuki."
            "Natsuki looks at me."
            n "Yo."
            show natsuki 1d at t11 
            n "How may I help you?"
            mc "Want to go on my back, just like before?"
            show natsuki turned pout at s11
            n "I... uh."
            show natsuki angr ml at h11 
            n "Why would I want to be on your back?!"
            n 4v "Gross! Gross!"
            mc "Oh? You don't want to?"
            mc "Alright, I guess I'll ask Sayo..."
            n turned pout om "W-wait..."
            n 1x "Khhhhhh..."
            n 4w "I d-didn't say no!"
            n turned anno om "Fine, you win."
            n "Let me in your stupid back."
            show natsuki at thide 
            hide natsuki
            "She climbed on my back and found a comfortable spot in there quickly."
            mc "I thought you don't want to be in my back..."
            n "Sh-shut up!"
            "We continued walking..."
            n "You smell nice."
            mc "Thanks."
            n "[player]?"
            mc "Yes?"
            n "Your back is off limits, okay?"
            mc "Um..."
            n "This is my territory now..."
            mc "Alright..."
            n "Mmmmm~"
            "She continued mumbling until we arrived at our house."
    
    scene bg house 
    with wipeleft_scene
    "The boyfriend stops here."
    mc "Alright, guys."
    mc "I'm looking forward to the school event."
    mc "See you on Monday guys!"
    e "We love you, [player]!"
    "All of them left and went to their respective houses."
    "Alright, time for me time."
    scene bg bedroom 
    with wipeleft_scene
    "Well it was fun nonetheless..."
    "I'm excited for the event this Monday!"
    "I'm looking forward to what my girlfriends prepared for."
    if time_travel == True:
        "I kinda want to spend time with Mizumi today but she's not around."
        "But I'm looking forward to what she's doing in the future."
    else:
        "I approached Mizumi."
        "Hey, Mizumi, care to play some games with me?"
        mi "Okay, my love!"
        if video_game == True:
            mc "I kinda need your help since Sayo wants to play Shining Zero with me."
            mc "We could've played that game in the future, right?"
            mi "Oh, right!"
            mi "You actually taught me how to play Shining Zero!"
            mc "The problem is... I don't have a copy with me, because I can't afford it yet."
            mi "Well, let's go to the future then."
            play sound it
            "We left to go to the future."
        else:
            "We played games and had fun spending time together for the rest of the day."
    
    scene black 
    with dissolve_scene_full
    stop music fadeout 2.0

    return 
