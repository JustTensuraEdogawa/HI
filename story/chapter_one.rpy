label chapter_one:
    
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0

    pause(1.0)
    "Previously on '100 Club Members who Really, Really, Really, Really Love You'..."

    scene bg corridor
    with dissolve_scene_full
    pause(2.0)

    $ c_name = '???'
    c "..."
    "I ran as fast as possible."
    "I didn't know that my karate chop could send a brick flying towards a beehive."
    "Come on."
    "I need to apologize to whoever's inside that room."
    "Those bees must've made them run panic."
    c "I think it's this room."
    c "Literature Club..."
    c "Oh gosh, they're holding an event here."
    c "I could've single-handedly ruined their event."
    c "Oh my."
    c "Calm down, Cara."
    "I gently opened the clubroom door."

    scene black
    with dissolve_scene_full

    pause(3.0)

    scene bg club_day
    with wipeleft_scene
    play music t9

    "Monika's still sulking after the bee incident."
    "Well, I couldn't blame her since she worked hard for the festival."
    "Sayori and the others are cleaning the aftermath while I went to Monika to comfort her."
    show monika forward ce cry mk at t11
    $ m_name = 'Monika'
    m "All our hard work..."
    m "All of it..."
    mc "Hey, Monika..."
    show monika at face
    "I hugged her tightly."
    mc "Again, It's not your fault that those bees ruined our event."
    mc "We're all here for you."
    mc "I'm... {w}...here for you."
    play music t8
    m 1m "Thanks... I really appreciate you my love~"
    mc "Anything for my girlfriend."
    show monika at t11
    "Monika smiled."
    m 1k "Ah, I feel much better now~"
    m 3a "Let's just clean the mess up and we'll call it a day!"
    mc "Yes ma'am!"
    show monika at thide
    hide monika
    "We helped the others clean and pack up."
    "Sayori, Yuri and Monika have done all the cleaning and left."
    "Natsuki is still in her closet, arranging her manga collection."
    "As I'm packing my stuff and ready to go, I heard the door slide open."
    c "Hello?"
    show cara 3p at t11
    mc "Um, excuse me miss how can I help--"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show cara 3q at h11
    "{b}ZING!!!{/b}"
    "A zing..."
    "Wait, a zing?"
    "She is one of my girlfriends too?"
    c 3t "Ah, erm..."
    c 3v "I'm sorry! It's all my fault!"
    "I'm confused at this point." 
    mc "Can you please explain further?"
    show cara 3v at f11
    c "While I was practicing my karate outside..."
    c "The brick managed to fly towards the tree near your room, disturbing a beehive!"
    mc "EHH?"
    show cara at thide
    hide cara 
    "Wow. She's strong."
    "I actually don't know how to respond to her."
    mc "Ahh, It's okay!"
    mc "We have already cleaned up here."
    mc "It's not your fault, okay?"
    "I stretched forth my hand, introducing myself."
    mc "My name's [player]. And you are??"
    $ n_name = 'Natsuki'
    n "[player]! let's go!"
    n "Huh?"
    "Natsuki looks at me then at the girl I'm talking to."
    show natsuki 4e at t11
    n "Who the heck are you missy?"
    show natsuki at t21
    show cara 1a at t22 
    c "My name's Cara. I'm from the karate club."
    $ c_name = 'Cara'
    c 3p "Again, I'm sorry for causing all of this."
    c "I was the one who managed to disturb the beehive that messed up your event."
    show natsuki 4e at f21
    n "Wait, you what?"
    mc "Now, now, Natsuki. It's not her fault."
    n "And you're defending her, [player]?"
    mc "It's not her fault. She didn't throw the brick there, she's just practicing her karate."
    "Natsuki felt irritated, but calmed down nonetheless."
    show natsuki 4d at t21 
    n "Alright, fine! Let's just go, ok?"
    "She grabbed me on my ear and tried to drag me out of the clubroom."
    mc "Ow, ow, ow! Natsuki, why?"
    n "I just want to hehehe~"
    "She smirked."
    show cara at lhide
    show natsuki at lhide
    hide cara 
    hide natsuki 
    "To my surprise, Cara grabbed Natsuki's arm and dragged her to the closet."
    "I followed both of them."
    n "H-hey!"

    scene bg closet
    with wipeleft

    show cara 1h at t22
    play music t7
    c "I won't let you hurt and bully [player] like that, Natsuki."
    show natsuki 4d at t21
    n "Ho, are you sure about that, Cara?"
    n 4y "Just so you know that nobody beats me when it comes to punching."
    show cara 1h at f22
    c "Well then you're on!"
    "Oh no. I need to save them from this situation..."
    "Why did it end like this?"
    "Natsuki tried to punch Cara, but she blocked it."
    "Cara released a 3-hit combo at Natsuki."
    show natsuki at lhide
    hide natsuki
    n "Eyaaah!"
    "Natsuki fell down at the ground."
    "Cara is good at karate."
    show natsuki 4p at t21
    n "This isn't over yet!"
    "She lunges forward again at Cara, only to get hit by another 3-hit combo."
    show natsuki at lhide
    hide natsuki 
    n "Eyaaah!"
    show natsuki 4v at t21
    n "I've had it!"
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show cara 1q at h22
    c "!"
    "Woah."
    "Natsuki?"
    "I have to step in before anyone gets hurt."
    "Natsuki charges forward towards Cara."
    show cara 1q at h22
    c "She's fast!"
    c "I can't block it!"
    "I managed to step between them, causing me to get hit instead."
    mc "Aaaahh!"

    scene bg corridor
    with wipeleft

    stop music
    "I flew outside the clubroom into the corridor."
    c "[player]!"
    show natsuki turned s_scream at t21
    show cara 3q at t22
    "Both of them rushed to check on me."
    show cara 3af at f22
    c "Are you okay?"
    mc "I'm... okay."
    "I stood up."
    mc "I'm glad I was able to step in."
    show natsuki 4e at f21
    show cara at t22
    play music t8
    n "Why would you do that, [player]?"
    n "You could've gotten yourself badly injured there!"
    mc "And you could've gotten her badly injured, if that's what your telling me."
    n 4w "She should be fine taking that hit since she is a martial artist."
    show natsuki at t21
    n "By the way, [player], I have to go home by myself. I'll have to clean my house since it's a mess."
    n 1l "Bye!"
    show natsuki at lhide
    hide natsuki
    "Natsuki gets her belongings and storms off."
    c 3k "This is all my fault."
    mc "No, it's not."
    "I shoved my backpack into my shoulders."
    "Hmmm... she is also one of my girlfriends..."
    "I'll try to spend time with her."
    mc "Anyways... Would you like to walk home with me?"
    show cara 3q at f11
    c "E-eh?"
    c 3u "S-sure."
    c "I guess it's probably how I can make it up to you..."
    c 1f "Wait for me outside, ok?"
    show cara at thide
    hide cara 
    "She went to get her belongings."
    "Well, I guess I have to wait for her now..."

    scene bg residential_day
    with wipeleft_scene

    "I waited outside the school grounds."
    "I see Cara walking towards me, with her belongings."
    "We walked for a little bit around the residential area."
    c "[player]..."
    show cara 3p at t11
    c "Sorry about the commotion earlier with your friend over there."
    mc "Ahh, it's okay!"
    mc "You didn't mean any harm to me."
    mc "My girlfriend is just like that sometimes..."
    mc "... uh no, most of the time."
    show cara 3q at f11
    c "Girlfriend?"
    c 3p "Oh... so she is your girlfriend."
    mc "Why? You seemed to be surprised."
    c 3u "I'm just curious."
    show cara 3p at s11
    c "I'm sorry because I picked a fight with your girlfriend."
    mc "As I said... It's okay."
    mc "You didn't mean any harm."
    mc "You just stood up for what you think Natsuki is doing."
    c 3u "Also... thank you for protecting me."
    c "I could've been knocked out cold with that punch."
    c "Yes, I may be strong..."
    c "But I also need someone to be my knight and shining armor."
    c "Which you have fulfilled."
    show cara at face
    c "I... think you might be the perfect guy for me."
    c 3q "But this isn't right."
    c "You already have a girlfriend."
    c 3ae "I... just couldn't ruin your relationship."
    "Oh. okay it's this again."
    "We'll let's see how it plays out."
    c 3q "I... l-love you."
    c 3ac "But I can't stand in the way."
    show cara at t11
    c "But at least I can relieve myself of the weights in my chest."
    c 3u "It's kinda hard to move with weights, like when I'm usually training."
    c "So there."
    c 3ae "It's time for me to go..."
    "She confessed."
    show black zorder 4 with dissolve_cg
    menu:
        "And of course, my response to her would be--"
        "Cara... I love a strong woman like you.":
            pass
        "Cara, you're strong enough to handle getting friendzoned, right?":
            "Bruh."
            "It's season 2 already."
            "You're still doing this?"
            "You should've known that this is not an acceptable option."
            "As Frieza always say..."
            "You filthy monkey."
            menu:
                "So please, pick the most sensible option."
                "Cara... I love a strong woman like you.":
                    pass
    
    hide black with dissolve_cg

    "I held her, preventing her from running away."
    mc "Cara..."
    mc "I love you too."
    show cara 3af at f11
    c "E-eh?"
    mc "And I'm willing to be your knight and shining armor."
    mc "I accept your confession."
    show cara 3q at s11
    c "But, you have a girlfriend..."
    c "I can't..."
    mc "It's okay."
    mc "I'm fair to {i}all{/i} of my girlfriends."
    show cara 3af at h11
    c "What?"
    c "{b}Girlfriends?{/b}"
    mc "Yes."
    mc "I currently have 4 girlfriends."
    mc "Which makes you the fifth."
    mc "I have loved all my girlfriends equally."
    mc "If I didn't, It would make me a liar."
    mc "And I will love you as much as I love Natsuki, and the others."
    c "[player]..."
    c 3ab "It would be an honor to be a part of your girlfriend train."
    c "I love you."
    c "Thank you for accepting me."
    show cara at thide
    hide cara 
    "She gave me a smile as she leaves."
    "Welp, time to go home."
    
    scene bg bedroom
    with wipeleft_scene

    "Ok..."
    "5th girlfriend acquired!"
    "I can't believe this!"
    "I'm 5 percent done as far as collecting all of the girlfriends Renpy-sama has promised me."
    "Still 5 percent!"
    "I still have a long way to go."
    "Anyways... I have to do what I have to do..."
    "I don't know what lies ahead."
    "I'll have to find out when it comes."
    "I dozed off to sleep."
    scene black
    with dissolve_scene_full

    return