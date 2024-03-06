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
    n 5bz "Shhh. Raccoons don't talk!"
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
    s "Ooh! She is working on [player]'s room? And [player] is coming over occasionally on her?"
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
    m 5a "Okay, [player]!"
    m 3b "Okay, everyone!"
    m "Club Members, roll out!"
    show monika 3b at thide
    show sayori 1ba at thide
    hide monika
    hide sayori
    "And thus were the activities... we're all set."
    "Okay, It's time for me to help my girlfriends!"
    $ mc_help = 0
    $ n_help = False
    $ y_help = False
    $ sm_help = False
    
    if mc_help == 0:
        $ helptext = "Who should I help first?"
    else:
        $ helptext = "Who should I help next?"

    label help_loop:
        
        if mc_help < 3:
            menu:
                "[helptext]"
                "Help Natsuki." if n_help == False:
                    "I decided to help Natsuki."
                    "Baking seems to be a very tedious work."
                    call natsuki_help
                "Help Yuri." if y_help == False:
                    "I decided to help Yuri."
                    "She seems to be eager with me helping her."
                    call yuri_help
                "Help Sayori and Monika." if sm_help == False:
                    "I decided to help Sayori and Monika."
                    "Helping both of them seems to be fun."
                    call sayori_and_monika_help
        else:
            jump help_done
            
        $ mc_help += 1
        jump help_loop
        
    label natsuki_help:

        scene bg kitchen
        with wipeleft_scene

        $ n_help = True

        "I approached Natsuki in the kitchen."
        n "Instead of running away, you're coming closer to me?"
        show natsuki 4ba at t11
        mc "Yes."
        mc "I would like to help you in your work."
        mc "You also want to give me all the dirty work, you said."
        n 5bs "I only said that to look cool."
        n "Of course, I wanted to spend time with you."
        mc "So do I, Natsuki."
        show natsuki 5bs at thide
        hide natsuki
        "We continued our banter towards each other as we work."
        mc "Can you check if this batter is okay?"
        show natsuki 1ba at t11
        "She put her finger on it to taste test."
        show natsuki 1bk at f11 
        n "It's not properly mixed."
        n 1bd "Are you really that weak?"
        n 5bd "You have to beat the crap out of it!"
        "She took the bowl of batter from my hand and churned the batter hard."
        "She taste tested the batter again."
        n "Now it tastes good."
        show natsuki 5bd at t11
        "I tried to taste test the batter as well, but she swatted my hand like its a mosquito."
        n 1bf "Watch it, [player]!"
        n "Only I can taste test it!"
        mc "No fair!"
        mc "I wanted to at least taste it too."
        n "I don't want your gross fingers on my cupcake batter!"
        n 4by "But if you really want to..."
        "She mischievously smiled and took a big glob of batter on her finger."
        "And wiped it on my forehead."
        n 4bz "There! If you can reach it, you can taste it!"
        n "Problem solved!"
        mc "Why you little--"
        show natsuki 4bz at lhide
        hide natsuki
        n "Catch me if you can, sucker!"
        "She started to run around the kitchen table."
        mc "Get back here!"
        mc "You can't run forever!"
        mc "You're on my territory, so I'll catch you eventually."
        "I eventually cornered her in a wall."
        scene n_cg3_base
        show n_cg3_exp1
        show n_cg3_cake
        with dissolve_cg
        n "Ahahaha! Stop!"
        mc "Not until you wipe off the big glob you put on my head."
        n "Fine, fine!"
        n "Let me go though."
        n "How can I wipe it off if you're pinning me?"
        mc "Nah, I don't trust you with that."
        mc "You always tease me."
        n "...You do that to me all the time, you know!"
        n "You're the one whose teasing me!"
        n "Especially when I'm off guard!"
        n "You really shouldn't tease girls like that."
        mc "Is that so?"
        mc "In that case, I probably shouldn't do this, either..."
        show n_cg3_cake at cgfade
        hide n_cg3_cake
        "I take Natsuki's finger and put it in my mouth, licking off the icing."
        show n_cg3_exp1 at cgfade
        show n_cg3_exp2 at cgfade
        hide n_cg3_exp1
        n "W-W-What--?"
        n "D-Did you seriously just--"
        n "A-Ah--"
        "Natsuki is so surprised that she can't even figure out how to get mad at me."
        "Her face is entirely red."
        hide n_cg3_exp2
        mc "Now we're even."
        mc "Oh. It tasted pretty good."
        n "What are you doing?!"
        n "Eh--"
        "She can't form any words out of her mouth."
        show bg kitchen
        show natsuki 1bn at i11
        with dissolve_cg
        "I let go of her."
        show natsuki 1bv at f11
        n "Y-you... pervert!"
        "She punched me hard."
        mc "Yeowch!"
        
        show bg lr
        with wipeleft_scene

        "I landed facedown on the floor in front of Monika."
        m "[player]! Are you okay?"
        m "What happened?"
        show monika 1a at t11
        "I get up."
        "I looked at Monika."
        mc "Nothing."
        mc "Nothing happened."
        m "Are you sure?"
        mc "Yes, Monika."
        mc "It's Natsuki were talking about."
        show monika 3n at f11
        m "Yeah, you're right."
        show monika 5a at t11
        m "Sounds like you're having too much fun in there!"
        mc "Yes, Ma'am!"
        mc "No worries."
        mc "I'll finish helping her as soon as possible so I can assist you later."
        m 3k "Okay!"
        show monika 3k at thide
        hide monika
        "I went back to Natsuki."

        scene bg kitchen 
        with wipeleft_scene

        "As I went back, I can see her taking out the cupcakes from the oven already."
        mc "I'm back."
        show natsuki 1bn at t11
        n "Just d-dont do that again, [player]."
        n "You always... catch me off-guard."
        mc "You're okay, Natsuki."
        mc "That's why I love you."
        n 1bs "I love you too."
        show natsuki 1bs at thide
        hide natsuki
        "We went and continued completing the cupcake designs."
        "It turned out pretty great!"
        "There were cupcakes with cute designs, and stuff."
        n 1ba "Thanks for helping me out."
        n 5bd "You're no slouch yourself."
        n "You can be my apprentice in baking, [player]."
        show natsuki 1bn at face
        with dissolve_cg
        "She hugged me."
        n "Thanks for your help."
        n "Sorry for punching you."
        n "I love you."
        "I flustered."
        n 1bd "Now, look at your face!"
        n "That's me when you always catch me off guard."
        mc "Fine, fine."
        mc "I love you too."
        show natsuki 1bd at t11
        n "I'll clean up everything here, [player]."
        if mc_help == 0:
            n "I know they're probably gonna ask you for help as well."
            n "Go spend time with them."
            n 4bz "Help them!"
        else:
            n 4bz "Go, I'll be fine here."

        mc "Okay, Natsuki."
        show natsuki 4bz at thide
        hide natsuki
        "She went and cleaned the kitchen up."

        scene bg lr
        with wipeleft_scene

        return

    label yuri_help:

        $ y_help = True

        scene bg bedroom
        with wipeleft_scene

        "I went upstairs to my bedroom."
        mc "Hi, Yuri."
        y "Oh, [player]."
        y "Glad to see you here."
        show yuri 1ba at t11
        y "Offering a hand of assistance, perhaps?"
        mc "Yes, milady."
        mc "Let's make these banners beautiful!"
        y 1bf "Is your handwriting good?"
        mc "Ah..."
        mc "I could pass off to be a doctor for my handwriting."
        y 1bj "Ah I see..."
        y 1bd "Then I wouldn't mind if you can only assist me in getting what I need."
        mc "Okay, Yuri."
        show yuri 1bd at thide
        hide yuri
        "We laid out the big canvas on the floor."
        "She started to setup the paintbrushes and color of the paint."
        y "[player], would you pass off the red paint beside you?"
        mc "Oh yeah sure."
        "I passed her the red paint."
        if n_help == True:
            y "I heard you from the kitchen downstairs."
            y "It seems like Natsuki knocked you down again."
            mc "Ahahaha."
            mc "We're having too much fun, I say."
            y "I see."
            y "Hopefully, I'm not boring you out."
            mc "No, no you're fine, Yuri."
            mc "Sometimes, a bit of relaxation is all I need."
            y "Oh, okay then."
        else:
            pass
        "She continued her writing on the big canvas."
        y "Oh. I ran out of paint of this color."
        y "Buying it now would take a lot of time."
        y "[player], can you please help me make this paint color?"
        y "Mix this paint with that paint to produce this same color here."
        y "You have to mix it with hot water though."
        y "Else the paint just settles on the top."
        mc "Okay, Yuri."
        "I immediately took the two paint cans and went down the kitchen."

        scene bg kitchen
        with wipeleft_scene

        "I went and made hot water from my electric kettle."
        n "Oh, [player]."
        show natsuki 1ba at t11
        n "Helping Yuri, it seems."
        mc "Yes, Natsuki."
        n 4by "Hopefully you're not doing anything weird to her, you creep!"
        mc "No, no, no!"
        n 4bz "Just messing with you."
        show natsuki 4bz at thide
        hide natsuki
        "I finished making hot water and brought up the kettle."

        scene bg bedroom
        with wipeleft_scene

        "I went back up to the bedroom and laid down the paint cans and the kettle."
        mc "I'll be doing the mixing here, and brought the electric kettle with me."
        mc "And got enough water for the paint cans... {w}and maybe some tea later."
        mc "I have some tea packets I bought yesterday."
        show yuri 1bd at t11
        y "How sweet of you."
        y 1ba "You always never cease to amaze me."
        y "I love you, [player]."
        mc "I love you too."
        "I started to get a cup from what I bought yesterday to put the paint."
        "Meanwhile, Yuri is making tea while waiting for my mixture."
        mc "Let's see here..."
        "I poured a small amount of paint into the other."
        "Sure enough, the paint I poured settled at the top."
        mc "Time to pour the hot water."
        "As I was pouring the hot water, I accidentally poured the hot water on myself."
        mc "Yeowch! Hot!"
        "I accidentally splashed Yuri with the mixture on her face."
        y "Yeowch!"
        mc "Ahh! I'm so sorry!"
        "I immediately went to the bathroom."
        "I grabbed a towel, dipped it in hot water, made it lukewarm and wiped Yuri's face."
        scene y_cg3_base with dissolve_cg
        mc "I'm so, so sorry, Yuri."
        y "It's okay, [player]."
        y "We all share our mishaps sometimes."
        "The paint is hard to come off."
        "Looks like I'll be working on this for a while."
        y "Yeah, the paint is very sticky. It's hard to come off on soft surfaces, especially skin."
        mc "I really, apologize for this."
        y "No, no its okay."
        show y_cg3_exp1 with cgfade
        y "I do kind of enjoy this, to be honest."
        y "It feels like you're caressing me."
        y "Your gentle touch soothes me."
        "She seemed to be relaxed."
        "She really loves it."
        "She's like a cat that likes to be petted."
        "How adorable is this cute angel?"
        "I never would've thought that I will get to have a girlfriend this beautiful."
        mc "There. All gone now."
        "I successfully removed the paint in her face."
        "She held my wrist."
        hide y_cg3_exp1
        y "Please... do it a bit more."
        y "Wipe my face clean."
        mc "But there's no more--"
        "She took a paintbrush, dipped it in the paint, and painter her other face!"
        y "There. There is more!"
        "She aggressively said."
        mc "Oh. okay."
        "I moved the towel on my hand and caressed her, stroking my hand towards her face gently."
        y "It soothes me, [player]."
        y "I love you."
        mc "I love you too, Yuri."
        "I wiped her face clean."
        scene bg bedroom
        show yuri 1ba at i11
        with dissolve_cg
        mc "Feeling better now?"
        y 3bm "Yes. Thank you for that."
        y "Let's get back to our banner."
        show yuri 3bm at thide
        hide yuri
        "We continued to work on the banner."
















    # scrapped activity
    # call activity_minigame

    return
