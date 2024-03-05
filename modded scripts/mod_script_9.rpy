label mod_script_9:

    play music m1

    mc "Hello?"
    "No response."
    mc "Renpy-sama?"
    "No response still."
    mc "What's going on?"
    mc "Monika?"
    "It sounds like I am all alone here."
    "I saw a piece of paper floating."
    mc "What is this?..."
    mc "I took the paper and read it."
    call showpoem (r_note, music=False, track=None, revert_music=False, where=i11, paper=None)
    mc "Oh..."
    mc "No one's here."
    mc "I'm alone at this void."
    "I wanted to wake up, now."
    "I looked at the back of the paper."
    "And sure enough there is a button."

    $ wait_meter = 0
    $ skip_transition = False

    label waiting_loop:
        
        menu:
            "Ah... There's nothing here. What should I do?"
            "Press the button.":
                jump wake_up
            "Wait.":
                $ wait_meter += 1
                "I decided to wait."
                "..."
                jump waiting_loop
            "Catch ligma." if wait_meter == 69:
                $ wait_meter += 21
                $ style.say_dialogue = style.edited
                "You waited for this long to get this easter egg, did you?"
                "Now you have ligma."
                "LIGMA BALLSSSSSSSSSSSSSSSSSSS!"
                "Now go back to the main options."
                $ style.say_dialogue = style.normal
                jump waiting_loop
            "..." if wait_meter == 100:
                $ wait_meter += 1
                stop music fadeout 2.0
                $ pause (3.0)
                play music "mod_assets/easter_egg.mp3"
                "AUGHHHHHHH!"
                "Hahahah, just messing with you."
                "You got an easter egg, and a rickroll!"
                "Let's go back to the main options."
                stop music fadeout 2.0
                play music m1
                jump waiting_loop
                
label wake_up:
    
    $ wait_meter = 0

    stop music
    scene bg bedroom

    "BZZT. BZZT. BZZT."
    "And I indeed woke up."
    "Time to spend my Sunday with my girlfriends!"

    scene bg house
    with wipeleft_scene
    play music "<loop 0>mod_assets/yr_extended.ogg"

    "I couldn't wait much longer for this day!"
    "I waited outside for my girlfriends."
    "And sure enough, Sayori arrives first."
    show sayori 1ba at t11
    s "Good morning, [player]!"
    show sayori 4ba at face
    "She went in for a hug immediately."
    mc "Good morning, Sayori."
    mc "How was your rest, yesterday?"
    show sayori 4br at t11
    s "I've been doing great, [player]!"
    mc "Good."
    "I noticed her holding another rope."
    mc "Sayori..."
    mc "What's with the rope this time?"
    s 4bl "Ahh..."
    s 4br "You might want to tie me up later when we sleep~"
    mc "Sayori..."
    show sayori 1ba at f11
    s "Yes, [player]?"
    mc "You shouldn't watch any more weird stuff you find on the Internet."
    show sayori 1bf at s11
    s "You meanie!"
    show sayori 4br at h11
    s "I'm messing with you, [player]."
    s "It's for something we might enjoy playing later."
    "She revealed me the rope."
    "It is a very long jumprope."
    "The jumprope that young girls use to play."
    mc "Oh, okay. We can play that as an outdoor activity if we finish our task."
    mc "Or maybe... if we take a break."
    mc "I learned something from Yuri yesterday..."
    show sayori 1bx at f11
    s "Really? What did Yuri teach you?"
    mc "She taught me that pushing yourself too hard on a task stresses you out."
    mc "It's good to take breaks and have fun!"
    show sayori 1ba at t11
    s "I'm really glad that you are taking her advice at heart, [player]."
    s "Yuri is a smart girl, isn't she?"
    mc "She is."
    mc "That's why I love her."
    s 1by "And what do you love about me, [player]?"
    mc "Sayori..."
    mc "I love your cheerfulness, your face, your smile, your hair!"
    mc "And I love you as a whole, Sayori."
    s 4bs "You're so sweet, [player]~"
    s "I love you!"
    mc "I love you too."
    s "[player]... tying me up in the bed later tonight is still on the table~"
    mc "Sayori!"
    n "Who's getting tied up?"
    "Natsuki arrived next."
    show sayori 1ba zorder 1 at t22
    show natsuki 5bd zorder 2 at t21
    n "The only one getting tied up here is [player]!"
    show natsuki 5bz zorder 2 at f21
    n "Of course, by yours truly!"
    mc "No one's getting tied up, Natsuki."
    show natsuki 5bd at t21
    n "Not if I can fix it!"
    n "Sayori, may I borrow that rope?"
    show sayori 1bx zorder 2 at f22
    s "Sure thing, Natsuki."
    show sayori 1ba at t22
    "She handed Natsuki the rope."
    mc "Now, now, no need to resort to that, Natsuki."
    mc "The only thing that will be tied is you and me tying the knot."
    "Natsuki starts to get flustered."
    n 4br "Hey, that's n-not..."
    mc "Remember your letter? You said {i}you{/i} wouldn't mind."
    mc "Do you want me to read the paper out loud?"
    n 4bp "N-no!"
    n 1bv "Give that back!"
    n "O-okay, fine, you win!"
    "Natsuki gave the rope back to Sayori."
    n 12c "Sheesh."
    y "Seems like [player] is getting a handful with you two."
    "Yuri arrived."
    mc "Hi, Yuri."
    show yuri 1ba at t31
    show natsuki 5br at t32
    show sayori 1ba at t33
    y "Hello, [player]."
    y "I'm excited about today."
    mc "Me too, Yuri."
    y "I will do my best in creating the banner!"
    $ style.say_dialogue = style.edited
    y "Can't wait to... {w}have a sniff of another pen..."
    $ style.say_dialogue = style.normal
    mc "...Uh... right."
    s "Natsuki... Yuri's acting like a raccoon again."
    y 3br "Sayori!"
    y "For the last time, I am not a racoo--"
    n 5bd "Shhh. Raccoons don't talk!"
    y "That's offensive!"
    mc "That's enough, you two."
    "We all laugh."
    "If this is the start of our morning together I don't know how fun it will be later!"
    m "Wait! don't start te fun without me!"
    "And surely enough, Monika arrived."
    show monika 3j at t41
    show yuri 1ba at t42
    show natsuki 5ba at t43
    show sayori 1ba at t44
    m "Good to see you all, sorry I'm late!"
    m "Practicing my piano skills!"
    m "My tutor asked me to play at least 1 hour a day."
    m "And I didn't even checked the time!"
    m "I even just wore my school uniform because of rush adrenaline."
    mc "No worries, Monika."
    mc "It's a good thing that you arrived."
    mc "Come here, Monika~"
    "I gave her a hug."
    show monika 1a at face
    m "Oh, I love you so much, [player]."
    mc "I love you too, Monika."
    show monika 1a at t41
    mc "Okay, now we are here all of us, let's go inside and start on our preparations!"
    mc "If you need to take a break, just let me know!"
    mc "I'll be assisting all of you!"
    "And with that, we went inside my house."

    scene bg lr
    with wipeleft_scene
    
    "We all gathered together in my living room."
    mc "Well, Monika... about the things that we need to do..."
    show monika 1a at t32
    m "Yeah, about that!"
    m "Natsuki will be baking cupcakes..."
    mc "You can use my kitchen. I'll be assisting you whenever you need me."
    show natsuki 1bd at t31
    n "Don't be slacking off on me now, mister."
    n 4bd "I'll let you handle all the dirty work."
    show sayori 1ba at t33
    s "Ooh! Dirty work~"
    mc "Not {i}that{/i} kind of dirty work, Sayori."
    show sayori 4br at h33
    s " I know. I'm just messing with you~"
    mc "Sheesh."
    show sayori 4br at thide
    show natsuki 4bd at lhide
    hide natsuki
    hide sayori
    m 3a "Now, Yuri is going to be working on the banners."
    m "Do you have any sort of space that she can work on it, [player]?"
    mc "She can work on my room, Monika."
    mc "There's a lot of office supplies there on my desk as well to help on her work."
    mc "I'll be your helping hand when you need me, Yuri."
    show yuri 1ba at t31
    y "I'd love it that you will assist me."
    y 3bd "Thanks for your assistance."
    show sayori 1ba at t33
    s "Ooh! She is working on [player]'s room? And [player] is coming over occasionally on her?
    s "I bet something {i}colorful{/i} is going to be beautifully made in his room~"
    mc "Sayori... {w}not again."
    show sayori 4br at h33
    s "It's fun teasing you like that, [player]~"
    show yuri 1ba at lhide
    hide yuri
    show monika 3a at t21
    show sayori 1ba at t22
    m "And now... me and Sayori will be doing our crafts here in the living room!"
    mc "Okay then."
    mc "There is a printer at the corner, over there. You can print using that stuff."
    


    


    return