image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nThis is not real.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat

label mod_script_5:

    scene black

    play music m1

    r "Hi [player]."
    mc "Hello, Renpy-sama."
    r "How is everything doing?"
    mc "I've liked it pretty much."
    mc "Sayori's been cheerful ever since I became his boyfriend."
    mc "Natsuki's been very happy whenever she's beside me."
    mc "Yuri is getting a bit more confident when I'm around."
    r "Great!"
    r "It's been 3 days and you're doing a fantastic job!"
    r "Anyways, time to wake you up."
    r "I have nothing to say to you as of this moment."
    r "Until then, [player]."
    r "Make them all happy."
    r "Because there is happiness in the Literature Club."
    r "You are their happiness."

    scene bg bedroom

    stop music

    "BZZT. BZZT. BZZT."

    # if enlightened_mc == True:
        # "I woke up."
        # "I looked at a clock."
        # "I really did miss school."
        # "I prepared myself and get ready for club time."
        # "Those things that I saw in my dream..."
        # "Is it really true?"
        # "Or Renpy-sama is just messing with me?"
        # "But anyways, I have a bit of informantion gathered with what I saw."
        # jump day_4_club
    # else:
        "I woke up."
        "Another wonderful day for me with my girlfriends today!"
    "I prepared myself and got ready for school."

    scene bg kitchen
    with wipeleft_scene

    "Surprisingly I didn't see any of my girlfriends here."
    "Well, I'm not always expecting them to be here."
    "I prepared my breakfast and got ready to go to school."

    scene bg residential_day
    with wipeleft_scene

    play music t2

    "As soon as I stepped out, I was greeted by a very cheerful cinnamon bun."
    show sayori 4r at t11
    s "Morning, [player]!"
    mc "Morning, Sayori!"
    mc "How's my girlfriend doing?"
    show sayori 1a at f11
    s "I've been very cheerful today, [player]!"
    s "It's all because you are my sunshine over my rainclouds."
    s "Let's walk to school together!"
    show sayori 1a at t11
    "She's so adorable early in the morning."
    mc "How sweet of you Sayori."
    mc "And of course, I'd love to walk to school with you!"
    "As we are about to start walking, somebody from behind is running towards us."
    n "Heeeeeey!"
    "I see a cutesy tsundere girl running toward us from the distance."
    "That girl is Natsuki, my girlfriend."
    "We decided to wait for her, of course."
    show sayori 1a at t22
    show natsuki 1a at t21
    n "Aren't you forgetting someone?"
    mc "Morning, Natsuki. How's your ankle?"
    show natsuki 1a at f21
    n "It's fine now, [player]."
    n 4y "Seems like you're expecting to carry me again, right?"
    n "Well you're wrong!"
    n "I am definitely not going to piggyback on your back again! EVER!"
    show natsuki 1a at t21
    y "Oh please."
    y "You were complaining to me yesterday that [player]'s back is way better than mine."
    y "And you told me that you wanted to piggyback on him again!"
    "I looked around and saw Yuri walking towards us as well."
    show sayori 1a at t33
    show natsuki 1a at t32
    show yuri 1a at t31
    mc "Morning Yuri."
    mc "How was your day?"
    y 3m "It was a very wonderful day for me."
    "I can see Natsuki getting all flustered again."
    n 4w "N-no it's not true!"
    n 42c "I don't w-want to!"
    mc "Don't worry, Natsuki. I won't force you."
    mc "But I'd be happy to do that if you want to, milady."
    show natsuki 1o at f32
    "Natsuki gets flustered once more."
    n 1z "...buuuut, if you insist..."
    n "I'd let you carry me again!"
    n 4y "It's not like I enjoyed that experience or anything anyways!"
    show natsuki 4y at t32
    mc "Alright, fine, fine."
    mc "Let's all go together again shall we?"
    hide yuri
    hide natsuki
    hide sayori
    with wipeleft
    "I laughed."
    "I really enjoyed my time with these girls."
    "There's nothing wrong that will spoil this pleasant day."
    "And we're still far from school."
    
    menu:
        "It's time to have some fun!"
        "Boop Sayori.":
            "I approached Sayori."
            "She really is oblivious while walking."
            "She always looked out of focus."
            mc "Boop!"
            show sayori 1p at t11
            s "Ahhh!"
            s 5c "You meanie!"
            mc "Sorry. You don't want me to boop you?"
            s 2a "No, not at all."
            s "Why only boop me?"
            show sayori 4q at face with dissolve_cg
            "She immediately came closer and hugged me."
            s "When you can hug me?"
            mc "Wooah--"
            "She hugged me tightly."
            "I hugged her back."
            "She let go of me after a few moments."
            show sayori 1a at t11
            s "I love you, [player]."
            mc "I love you too."
            show sayori 1a at thide
            hide sayori
        "Ask Natsuki to carry her.":
            "I approached Natsuki."
            mc "Natsuki..."
            show natsuki 1a at t11
            n "Yes, [player]?"
            mc "Want me to carry you, right?"
            n 1p "N-no!"
            n "I don't want to!"
            show natsuki 4y at f11
            n "But... If you really want to so bad..."
            n 4z "Then I'll guess I have to comply!"
            mc "You really wanted to climb on my back again."
            show natsuki 42c at t11
            n "N-no!"
            n "Just carry me, ok?"
            show natsuki 42c at thide
            hide natsuki
            "I carried her on my back again."
            n "You smell nice, [player]."
            mc "Thank you. You too."
            n "I love you."
            "Natsuki said in a soft voice that no one can hear."
            "But I can hear her loud and clear."
            mc "I love you too, Natsuki."
        "Hold hands with Yuri.":
            "I walked beside Yuri."
            mc "Hi Yuri."
            show yuri 1a at t11
            y "Hello, [player]."
            y "So how are you doing in terms of reading the book I gave you?"
            mc "I am doing great actually."
            mc "I have read a bunch of chapters"
            mc "And it's really enticing to read more."
            y 3m "It's good that you are picking up on literature."
            y "Hopefully we can discuss more things about it!"
            mc "Yes, ma'am!"
            mc "By the way..."
            mc "Want to hold hands with me?"
            "Yuri seems to be delighted at my offer."
            y 3c "I cordially accept your offer."
            y "I love you, [player]."
            mc "I love you too."
            "She took my hand and held it the rest of the walk."

    scene bg class_day
    with wipeleft_scene

    "And thus we arrived at our respective classes."
    "It was a fun walk always with those three."
    "And it's always short."
    "Why does time flies when you're having fun?"
    "And when it comes to boring classes like this..."
    "It just goes on forever?"
    "Ugh."
    "Anyways..."
    "I'll just have to think of happy thoughts."
    "And with my thoughts, classes were soon done and I hurried to the clubroom."
    mc "Time for club!"
    
    stop music fadeout 2.0

label day_4_club:
    
    scene bg club_day
    with wipeleft_scene
    play music t3

    "I opened the clubroom door and saw everyone hanging out already."
    mc "Hi, Everyone!"
    "I greeted all of them enthusiastically."
    n "Hi [player]!"
    "I see Natsuki approaching me."
    mc "Ho, you're approaching me?"
    show natsuki 4z at t11
    n "I can't beat the crap out of you without getting closer."
    mc "Ho, ho, then come as close as you like."
    "As she approached me even closer, I hugged her."
    n 1v "Eyaaaah!"
    show natsuki 1p at f11
    n "That's not fair, [player]!"
    mc "All is fair in love and war."
    "I let her go."
    mc "Oh yeah, I read the manga that you gave me"
    mc "And it was great!"
    n 4z "Told you it was great!"
    show natsuki 4a at t11
    n "Time to give you the next volume!"
    show natsuki 4a at thide
    hide natsuki
    "She disappeared and went to the closet."    
    "It seems like everyone has their duties today."
    "Natsuki is looking for her manga."
    "Yuri is reading her book."
    "And Sayori and Monika seems to be talking in one corner."

    stop music fadeout 2.0

    play music t6
    
    s "[player], [player]!"
    "Sayori suddenly comes up to me."
    show sayori 1x zorder 2 at t11
    s "I'm gonna go get some supplies from another classroom."
    s "Want to come with me?"
    mc "Supplies?"
    mc "What for?"
    s 2a "Well, you know how the festival is coming up?"
    s "Me and Monika were gonna make some posters and stuff."
    s "So I need to go find some crayons, and markers, and glue sticks..."
    mc "Ah, I see."
    mc "Sure, I'll go with you."
    s 4q "Yaay~"
    s 4x "Okay Monika, we'll be back soon!"
    show sayori zorder 2 at t22
    show monika 1a zorder 3 at f21
    m "Ah, are you going with [player] to get the supplies?"
    m "There's no need to trouble yourself."
    m "I'd be happy to go with him."
    show monika zorder 2 at t21
    show sayori 1h at s22
    s "Aw, but I wanted to go!"
    s "It's so much fun exploring empty classrooms and stuff!"
    show monika zorder 3 at f21
    m 2j "Hehe, okay, okay."
    m 2a "It was just a suggestion."
    m "See if you can find poster paper too, okay?"
    show monika zorder 2 at t21
    show sayori zorder 3 at f22
    s 1r "Okaay~!"
    s 1a "Ready, [player]?"
    mc "Yep, let's go."
    scene bg corridor
    show sayori 4a zorder 2 at t11
    with wipeleft_scene
    "Sayori and I exit the clubroom."
    "I follow behind as Sayori hums and skips around the hallway."
    "Honestly..."
    "It feels like I'm taking a kid to the mall or something."
    "Sayori finds pleasure in the simplest things sometimes."
    "But it's okay for me."
    "Sayori being an adorable ball of sunshine makes my day anyway."
    mc "Hey, Sayori..."
    mc "What exactly are we doing for the festival, anyway?"
    mc "I'm not sure how you would make an event out of literature..."
    s 1q "Ehehe!"
    s 1x "Me and Monika have it all planned out!"
    s "Don't you worry~"
    mc "Is that so...?"
    s "Yup!"
    s "We're gonna do a poetry performance!"
    mc "A performance...?"
    mc "Of what kind?"
    s 1c "Well..."
    s "Everyone is gonna take turns on stage..."
    s 1x "And recite their favorite poems!"
    mc "Ah..."
    mc "That sounds..."
    "...Kind of dull?"
    s 1h "[player]!"
    s "You're not thinking about it the right way at all!"
    s "It's not just about reading poems..."
    s 1x "It's about performing them!"
    s "Like, you say the lines of the poem like..."
    s 2j "{i}Between my feet...{/i}"
    s "{i}The last remaining flower beckons to me.{/i}"
    s 1c "{i}I twist the stem, freeing it from its clinging roots...{/i}"
    s "{i}Caressing the final joyous moment between my fingers.{/i}"
    s 3g "{i}But to what ends have I summoned this joy?{/i}"
    s "{i}For now when I look in every direction...{/i}"
    s 1j "{i}The once-prosperous field before me...{/i}"
    show sayori at h11
    s 4m "{i}Is but a barren wasteland!{/i}"
    s "..."
    s 1r "Like that!!"
    mc "Sayori..."
    "How do I put this..."
    mc "I'm sure it's just me, but it's impossible for me to take you seriously when you talk like that..."
    show sayori 5c at s11
    s "Ehhh?"
    s "You meanie!"
    s "I'm working super hard on this, you know!"
    mc "Ah, I know, I know!"
    mc "I just meant that it's a pretty unordinary contrast to your cute self."
    show sayori 4s zorder 2 at t11
    s "Ahaha! Don't say that, it's embarrassing!"
    s 4y "But I guess that means I'm doing a good job~"
    mc "Yeah, I guess so..."
    show sayori at h11
    s 4r "Aaah, I'm so excited!"
    s "The festival is going to be so much fun~"
    "Sayori spins herself around in the hallway again."
    s 1x "Hey, [player], this classroom over here is empty!"
    s "Let's begin the mission!"
    show sayori zorder 1 at thide
    hide sayori
    mc "The mission, eh...?"
    "It's been a long time since I've spent time with Sayori like this."
    "But in the end, she hasn't changed one bit."
    "She's nothing but a ball of sunshine, drawing happy vibes from the world around her."
    "It's a pretty nostalgic feeling for me."
    "As the years went by, I began to hole myself up in my room more and more."
    "So going adventuring with Sayori brings about a special sort of feeling I forgot I had in me."
    scene bg class_day
    with wipeleft_scene
    "The two of us enter the classroom."
    "Sayori heads straight to the closet, and I follow."
    show sayori 1b zorder 2 at t11
    s "Let's see what we have in here..."
    s 4x "...Crayons!!"
    "Sayori pulls a box full of crayons off the shelf."
    s "They're the best brand, too!"
    s 1b "They're kind of dirty, though..."
    "Sayori starts pulling various crayons out of the box, reading the color names."
    mc "Alright, that's one down."
    mc "Don't get distracted, we still need to find--"
    s 1a "Wait, I'm looking for my favorite color..."
    mc "Fine, fine..."
    mc "Then at least move aside so I can look for the poster paper."
    s 1b "Ah, I dropped one by accident--"
    play sound "sfx/smack.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 2p at h11
    "{i}Smack!{/i}"
    hide white
    s "Kya--!"
    "Sayori bends over and smacks her forehead right into the shelf."
    "She falls to the floor, and the crayons spill all over her lap."
    show sayori 4p at s11
    s "Owowowowow..."
    mc "You okay?"
    s "My forehead..."
    "Sayori clutches her forehead."
    mc "Jeez, Sayori..."
    mc "That's just like you, isn't it?"
    mc "C'mon, let me see."
    "Since Sayori is sitting on the floor, I grab her by the waist and pull her out of the closet."
    mc "You have to move your hands, Sayori..."
    s 4g "But it hurts..."
    mc "Just do it for a second."
    scene s_cg2_base1
    show s_cg2_exp2
    with dissolve_cg
    "Sayori slowly releases her hands from her forehead."
    "I gently brush her bangs to the side."
    show s_cg2_exp1 at cgfade
    show s_cg2_exp3 at cgfade
    s "Ow--!"
    mc "Sorry..."
    "There's a huge red mark on the center of her forehead."
    "A bump is starting to form, as well."
    mc "Man, that's gonna swell up."
    mc "I should find you some ice..."
    hide s_cg2_exp3
    hide s_cg2_exp1
    s "[player]..."
    mc "Where would I even find ice around this time...?"
    mc "Ah, I guess a cold drink would do..."
    s "You don't have to--!"
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    s "I'm fine with--looking like a unicorn--"
    "Even wincing from the pain, Sayori makes a silly joke."
    mc "Ahaha, what are you saying?"
    mc "I'll be right back, okay?"
    s "O-Okay..."
    stop music fadeout 1.0
    scene bg corridor with wipeleft_scene
    "I pat Sayori on the shoulder and run out into the hallway."
    "I locate the nearest vending machine."
    mc "What should I get...?"
    "It doesn't really matter, since it will be used as an ice pack, rather than to drink."
    "But I know Sayori likes apple juice, so I purchase that one."
    "In just a moment, I'm already returning to the classroom where I left Sayori."
    scene s_cg2_base1
    show s_cg2_exp2
    with wipeleft_scene
    play music t9
    "She has one palm on her forehead and is using the other hand to clumsily scoop crayons back into the box."
    s "At least they were already in the wrong spots before I spilled them..."
    mc "Sayori, here."
    show s_cg2_base2 behind s_cg2_exp2 at cgfade
    "I hand Sayori the bottle of apple juice."
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    s "It's nice and cold..."
    "Sayori opens the cap and starts drinking from it."
    mc "Sayori, what are you doing?!"
    mc "It's for your forehead, dummy!"
    show s_cg2_exp3 at cgfade
    s "Ah--"
    s "Sorry, I forgot~"
    s "Ahahaha!"
    mc "How hard did you hit your head...?"
    "Sayori places the bottle against the bump on her head."
    show s_cg2_exp1 at cgfade
    s "It stings..."
    mc "Just bear with it, it'll feel better soon."
    mc "Looks like you cleaned up most of the crayons, so that's good."
    hide s_cg2_exp1
    hide s_cg2_exp3
    s "Hey, [player]..."
    s "This kind of reminds you of growing up, doesn't it...?"
    mc "Eh? What do you mean?"
    s "You know how we used to play outside all the time..."
    s "I would always try to keep up with you."
    s "You were kind of oblivious in some ways..."
    s "Like I usually fell behind or had trouble climbing on the things you did..."
    s "But sometimes when I tried to do things I couldn't, I would get myself hurt."
    s "I'd fall and scrape myself, or get a bump..."
    s "And I would start crying really hard."
    show s_cg2_exp3 at cgfade
    s "Ahaha!"
    s "And you would rush over as quick as you could."
    hide s_cg2_exp3
    s "You would try really hard to get me to stop crying."
    s "It was almost like you blamed yourself and were afraid of getting in trouble if someone found out..."
    s "Even though it really wasn't your fault at all, you know?"
    mc "Did I really do that...?"
    s "Yeah...you don't remember?"
    mc "Come to think of it, maybe I do remember a bit..."
    mc "I guess I was always so focused on my games that I didn't pay enough attention to you."
    mc "So in a way, it was my fault."
    mc "Kind of like this time, too..."
    mc "If I wasn't rushing you out of the closet, you probably wouldn't have hit your head."
    s "[player]..."
    s "I don't think you realize it, but you're always thinking about other people."
    s "Even after all these years..."
    s "You're rushing to help me, even though I'm just being clumsy."
    show s_cg2_exp3 at cgfade
    s "You're really a sweetheart..."
    mc "No-- not really..."
    mc "And I don't really do this kind of thing all the time..."
    mc "I guess when it comes to you, it just feels natural."
    mc "Before I even know it, I'm treating you like that."
    mc "I guess that's what happens when you've been friends for so long."
    hide s_cg2_exp3
    s "Really...?"
    s "Maybe you're right..."
    s "[player]..."
    s "I'm so glad that nothing's changed between us."
    s "Do you think it'll be like this forever?"
    mc "Forever...?"
    "If I'm honest to myself..."
    "There's no telling where we'll each end up for college, or after that."
    "So it wouldn't be fair for me to make any promises."
    "But..."
    mc "Well, I hope so."
    mc "It's been this long already, right?"
    mc "I can't imagine you ever changing, so my hopes are up."
    s "I'm so happy..."
    "Sayori has a whimsical expression in her eyes."
    "We remain silent for a moment."
    "She's so silly and clumsy on the outside that when I see her deep in thought like this..."
    "It makes me not want to disturb her."
    s "I guess we should go back..."
    s "I don't want to worry Monika, you know?"
    mc "Good luck with that."
    mc "She's gonna see your forehead either way."
    s "Not if I hide it under my bangs~"
    play music t8 fadeout 1.0
    scene bg class_day
    show sayori 1a zorder 2 at i11
    with dissolve_cg
    "Sayori hops to her feet."
    show sayori 4p at s11
    s "A-Aaahh--!"
    "She clutches her forehead again."
    mc "Don't stand up so fast after hurting yourself!"
    s "Uuuu..."
    mc "Well, I guess it's too late now..."
    mc "Anyway, let's go."
    scene bg corridor
    with wipeleft_scene
    "I follow Sayori out of the classroom."
    "Sayori plays with her bangs to try to hide the bump, but without much success."
    "In a moment, we make it back to the clubroom."
    scene bg club_day
    show sayori 1a zorder 2 at t21
    show monika 1b zorder 2 at t22
    with wipeleft_scene
    show monika zorder 3 at f22
    m "Ah, you're back!"
    m "Good timing, I was just about ready to start with sharing our poems."
    m 1d "Eh? Sayori, your forehead..."
    show monika zorder 2 at t22
    mc "She's fine, don't worry about--"
    show sayori 4r zorder 3 at f21
    s "I was playing with the crayons and smacked my forehead into the shelf!"
    show sayori zorder 2 at t21
    mc "..."
    show monika 3m zorder 3 at f22
    m "..."
    m 3l "...Well, anyway!"
    m 1a "Were you able to find everything we needed?"
    show monika zorder 2 at t22
    show sayori 1x zorder 3 at f21
    s "Uh-huh! I have it right--"
    s 1n "...Eh?"
    "Sayori frantically glances around herself."
    show sayori 4m zorder 3 at hf21
    s "I...forgot all of the stuff!!"
    show sayori zorder 2 at t21
    mc "Calm down, Sayori."
    mc "I have it all right here."
    mc "I found the poster paper, too."
    show sayori 4b
    show monika 5a zorder 3 at f22
    m "Ahaha!"
    m "Sounds like you ended up doing all the work, [player]."
    show monika zorder 2 at t22
    mc "Ah, well, Sayori--"
    "I fail to come up with an excuse for Sayori."
    show sayori 1q zorder 3 at f21
    s "I made it an adventure!"
    show sayori 1a zorder 2 at t21
    mc "...Yeah, that."
    mc "And I don't mind really."
    mc "Spending time with Sayori like this makes me happy either way."
    show monika 1j zorder 3 at f22
    m "Ahaha, okay, okay."
    m 1a "In any case, good work!"
    m "I'll start working on the posters tonight."
    show monika zorder 2 at t22
    show sayori 4x zorder 3 at f21
    s "Me too!"
    show monika zorder 2 at t11
    show sayori behind monika at thide
    hide sayori
    m 4b "...Okay, everyone!"
    m "Are you ready to share your poems?"
    mc "Guess I should grab mine..."
    "After making sure the crayon box is closed tightly, I return to my seat."

    stop music fadeout 2.0

    play music t5

    "It's time for poem sharing."
    "Again, as always, I prepared all 4 poems that I have."
    show sayori 1a at t41
    show natsuki 1a at t42
    show yuri 1a at t43
    show monika 1a at t44
    "It's as usual as before."
    "It makes them speechless."
    show natsuki 1h at f42
    n "You really are trying hard to impress us."
    show natsuki 1h at t42
    show yuri 3j at f43
    y "And I say, you're very good at impressing us."
    show yuri 1a at t43
    show sayori 2x at f41
    s "That's why we love you, [player]."
    show sayori 2a at t41
    show monika 3b at f44
    m "Well done, [player]."
    show monika 5a at h44
    m "You've been doing great in making your poems!"
    show monika 1a at t44
    mc "Thank you girls."
    mc "I'll improve in my poem making for all of you!"
    mc "Maybe... It's time for you to show your poems to me!"
    "They showed me their poems."
    "And that concludes the poem sharing."

    stop music fadeout 2.0

    play music t8

    "I am ready to go home."
    "I packed my things."
    "I saw Sayori approaching me, inviting me to walk home."
    show sayori 1a at t11
    s "Ready to go home?"
    s "The others are waiting as well."

    jump usual_walk

    return


label mod_script_5_1:
    
    $ enlightened_mc = False

    mc "I'd love to hear the reason."
    mc "But I think I'd pass."
    mc "You changed the 'script' anyways, right?"
    mc "So I think there's no reason to show it to me."
    mc "I'm happy with whatever is happening."
    r "Alright, [player]. Suit yourself."

    return

label mod_script_5_2:
    
    $ enlightened_mc = True

    mc "I'm kind of curious."
    mc "Yeah, sure Renpy-sama."
    mc "I wanted to know what this real reason is."
    r "Cool."
    r "Welp you're in for a bumpy ride, [player]."
    
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up, but decided that's a little too much."
    "Meanwhile, the preparations for the event should be nearly complete."
    "Natsuki's cupcakes should be a masterpiece."
    "And Yuri's banner and decorations should also be top-notch."
    "I decided to walk alone to school."
    "I can't be late."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    "I say that, but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful, knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But..."
    "Maybe I should have gone to wake her up after all?"
    m 1k "Ahaha."
    m 4b "You should take a little responsibility for her, [player]!"
    m "You kind of left her hanging this morning, you know?"
    show monika 4a
    "Hanging?"
    mc "Hanging?"
    m 3l "Oh, ahaha never mind that~"
    mc "Jeez..."
    m 2j "Don't worry."
    m "Don't mind me here."
    mc "Eh...?"
    "Monika is being as friendly as usual, but for some reason I felt a chill down my spine after hearing that."
    m 5 "Hey, do you want to check out the pamphlets?"
    m "They came out really nice!"
    mc "Yeah, sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah, they really did."
    mc "Something like this will definitely help people take the club more seriously."
    m "Yeah, I thought so too!"
    show monika zorder 1 at thide
    hide monika
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page, giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the one she practiced."
    "It's one that I haven't read before..."
    call showpoem (poem_s3, music=False)
    mc "Ah--"
    "What is this...?"
    "Reading the poem, I get a pit in my stomach."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "What's wrong?"
    mc "Ah, nothing..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "I-I changed my mind!"
    mc "I'm going to go get Sayori, so..."
    m "Ah--"
    m 1b "Well, alright!"
    m "Try not to take too long, okay?"
    scene bg corridor with wipeleft
    "I quickly leave the classroom."
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."

    scene bg residential_day with wipeleft_scene
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."

    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    mc "Sayori?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15

    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "What the hell...?"
    "{i}What the hell??{/i}"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    stop music fadeout 2.0
    scene black with dissolve_cg
    "I suppress the urge to vomit."
    
    play music m1

    mc "Renpy-sama {b}WHAT THE HELL?{/b}"
    mc "What was that?"
    r "Yep. What you see is what will happen to her without me and the Modder's interference."
    r "Basically, Sayori's been depressed her whole life, and she..."
    r "... ended herself at the festival day."
    mc "..."
    mc "I never knew that."
    mc "I'm so naive."
    mc "She's my best friend."
    mc "I should've known it back then!"
    mc "If I didn't shut myself in and became a NEET, this would've never happened."
    mc "I don't deserve to be his boyfriend now."
    r "Now, now, [player]..."
    r "Don't beat up yourself for it."
    r "Next up..."
    
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t5

    "I seem to be in the clubroom."
    "Suddenly, I have a poem in my hand."
    "I think it's time to share poems."

    menu:
        "Who should I share my poem?"
        "Natsuki.":
            call natsuki_nightmare

    play music m1

    $ quick_menu = True
    mc "..."
    mc "No, not her as well."
    r "Yeah. I know."
    r "It was when Yuri became... insane."
    r "Totally obsessed with you."
    r "A {i}'yandere'{/i}, you might say."
    r "You were spending time with Natsuki the day before that."
    r "And you were about to spend time with her on that day as well but Yuri intervened."
    mc "..."
    "I have never felt this uneasy before."
    "Seeing Sayori ended herself and Natsuki... well..."
    "I wanted to cry."
    mc "I'm gonna guess..."
    mc "We still have Yuri, right?"
    r "Yes I still have to show you Yuri's as well."
    r "Well, off we go..."

    stop music fadeout 2.0
    scene bg club_day
    play music t10y
    
    "And... I'm back in the club."
    "Seeing no one is around, It seems everybody has left already."
    "...not all it seems."
    "I see Yuri looking at me with a creepy look."
    show yuri 2m zorder 2 at t11
    y "Finally."
    y 2y1 "Finally!"
    y 2s "This is really all I wanted."
    y 1y6 "[player], there's no need to spend the weekend with Monika."
    y "Don't listen to her."
    y 1y5 "Just come to my house instead."
    y 3y5 "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y 3y1 "Ahahaha!"
    y 3y4 "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    y 1y3 "I don't care anymore."
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    y 2y6 "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y 3y1 "I don't care anymore, [player]!"
    y "I have to tell you!"
    y 3y4 "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y 3y3 "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y 3w "Please, [player], just know how much I love you."
    y 3m "I love you so much that I even touch myself with the pen I stole from you."
    y 3y4 "I just want to pull your skin open and crawl inside of you."
    y 3y6 "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y 3s "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"

    menu:
        "Yes.":
            call yuri_death
        "No.":
            call yuri_death
    
    play music m1

    mc "..."
    mc "Why... Yuri... Why?"
    r "Yuri has this weird bizarre hobby of cutting herself."
    r "Also she likes knives and stuff."
    r "You can actually see her cuts in her arm."
    r "That's why she wears her long sleeves."
    mc "..."
    mc "I see."
    r "That's about everything."
    mc "Wait."
    r "Yes, my child?"
    mc "What about Monika?"
    r "As far as Monika..."
    r "...You were not around when stuff happened with her."
    r "It was the Modder who was around."
    r "And He did what he had to do."
    "I just sat there, distraught from what I saw."
    r "No worries [player]. That's why he asked my help to change things up a bit!"
    r "Actually, it was my twin sister, Aijou Renpirou."
    r "But seeing she has other things to do, she gave the task to me."
    r "And I have been doing a pretty good job here."
    mc "..."
    mc "Renpy-sama..."
    mc "I would like to thank you for enlightening me."
    mc "I'll never let you down!!!"
    r "Of course, [player]."
    r "Thank the Modder as well."
    r "I'd like you to meet him soon."

    return
