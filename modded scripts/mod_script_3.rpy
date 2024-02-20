label mod_script_3:
    
    scene black

    play music m1
    
    r "Hi, [player]."
    mc "Renpy?"
    r "It's Renpy-sama to you."
    r "But anyways, long time no see... but you can't really see my physical form."
    r "I wish I had assets, but the person who is responsible in this mod doesn't know how to code me well so..."
    mc "Huh?"
    mc "What do you mean, responsible?"
    mc "Is there still someone above you?"
    r "Yes, there is. He is the 'Modder' the one who created this mod."
    mc "I'm... confused."
    r "The 'Modder' is the 'entity' that sits on his computer, types a bunch of dialogues and stuff, and voila!"
    r "A mod is created through his creative mind!"
    "Now there is another 'unknown entity' in the picture."
    mc "I'm... not going to process any more of those stuff. My head will explode."
    mc "Just tell me why are you here in my dream again."
    r "Ah yes. I am just here to tell you that you did okay yesterday."
    r "It was a bit of a mess, but hopefully it gets fixed on your next meeting with them ok?"
    mc "Yes, Renpy sir-- I mean Renpy-sama."
    r "Good. I trust you with them."
    r "Be like Aijou Rensho."
    r "Make them happy."
    mc "..."
    "Seeing my current situation with the girls and the happiness that we will share with each other fills me with determination."
    "I can feel it... crawling on my back."
    mc "I will, Renpy-sama."
    r "That's the spirit!"
    r "Make me and the Modder proud!"

    stop music

    scene bg bedroom

    "BZZT! BZZT! BZZT!"
    "The alarm goes off again."
    mc "Another weird dream."
    mc "I shouldn't play too much 'Enduretale'. It lessens my time to do other things."
    mc "Speaking of which, hopefully I will make them smile with these poems."
    "I picked up all 4 poems that I managed to write in a span of 10 minutes."
    mc "Time to prepare for school!"

    scene bg residential_day
    with wipeleft_scene
    play music t2

    "I stepped outside and waited for Sayori."
    "I promised her that we will walk together to school today."
    "But for some reason, she is not here yet."
    "It makes me worry about her because she'll be late."
    "She's always like this before. Oversleeping."
    "I can't believe she carried this behavior of hers till high school."
    "Guess I'll be waking her up."
    
    scene bg house 
    with wipeleft_scene

    "I approached her house and opened her front gate."
    "Rather than asking, I simply tell her \"I'm coming over\", much like we've done in the past."
    "Once I reach Sayori's house, I knock on the door before entering it myself."
    "Again, we used to play so often that we've made it a habit of simply entering each other's houses like we were family."
    
    stop music fadeout 2.0
    scene black with wipeleft

    "The house is quiet."
    "Sayori isn't anywhere on the first floor, so I assume she's up in her room."
    "It's already strange of her not to run down and greet me."
    "I knocked on her door."
    "No response."
    "Hearing no response from her worries me even more."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "......Sayo--"

    scene bg sayori_bedroom

    mc "--ri?..."
    "Huh."
    "She's not here."
    "Where she could've gone?"
    mc "Come on out now, we're gonna be l--"

    show sayori 4x at l11
    s "{b}BOO!{/b}"
    "Silence."
    s 1a "Did I scare you?"
    "..."
    menu:
        "Uh... yeah.":
            show sayori 4r at h11
            s "Hahaha, got you again!~"
        "...":
            show sayori 5c at f11
            s "You meanie!"

    play music t2

    show sayori 1a at t11

    s "Anyways, thank you for checking in on me [player]."
    mc "Yes, because we're going to be late."
    show sayori 4m at h11
    s "Oh right, right!"
    s "We have to hurry, [player]. Let me just get my breakfast first."
    s "I can't run with an empty stomach."
    "And with that, she ate her breakfast quickly and we went outside to start our walk to school."

    scene bg residential_day
    with wipeleft_scene

    "We have begun our walk to school."
    "As we walk down the road, I see a familiar figure walking by herself."
    "We decided to walk closer to her."
    "I decided to cover her eyes."
    n "Eyaaaaugh!"
    "She screeched."
    show natsuki 1v at t11
    n 4o "Khhh..."
    show natsuki 4p at f11
    n "{b}TAKE THIS YOU PERVERT!!!{/b}"
    "She punched me. HARD."
    mc "YEEEEEEOOOOWWWW--"

    scene bg residential_day
    with wipeleft_scene
    
    mc "WWWWWWWWWW--""

    scene bg house
    with wipeleft_scene
    
    mc "WWWWWWWWW--""

    scene bg club_day
    with wipeleft_scene

    mc "WWWWWWWCH!"
    
    return
