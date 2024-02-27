label mod_script_7:

    scene bg kitchen
    with wipeleft_scene
    play music t2

    "I went downstairs to the kitchen."
    "And I saw Monika there, preparing a meal for me."
    show monika 3a at t11
    m "Hi, [player]."
    m "How was your sleep?"
    m 5a "Bet you saw me in your dream, are you?"
    m "Ehehe~"
    mc "Yes, Monika. I saw you in my 'dream'."
    m 1k "Ahaha, I'm just teasing you."
    m "I love you, my dearest [player]."
    mc "I love you too, my dearest Monika."
    show monika 1a at face
    "She hugged me tightly."
    "I feel comfortable in her arms. Really."
    "I will love you forever, Monika."
    "I'm sorry if I didn't spend time with you for the past 3 days."
    "We continued being like this for a while."
    "Until I smell something burning."
    mc "Monika... I think I smell something burning."
    "She turned around."
    show monika 1p at t11
    m "Yikes!"
    show monika 1p at lhide 
    hide monika
    m "My cooking!!"
    show monika 1o at t11
    m "It's ruined now..."
    m "I'm sorry, [player]."
    "She burnt the eggs to a crisp!"
    "She also made it as pitch-black as can be."
    mc "It's okay, Monika."
    mc "We were in the heat of the moment."
    mc "I'll just make one for--"
    m 3a "No, no, no. Let me just do this then."
    $ run_input ("os.give Monika cooked eggs 4", "Gave Monika 4 cooked eggs successfully.")
    "Suddenly, a plate with 4 fried eggs spawned on the table."
    m "Okay, now let's do the next item on the menu..."
    $ run_input ("os.give Monika cooked bacon strips 4", "Gave Monika 4 bacon strips successfully")
    "Suddenly, 4 strips of bacon spawned also on the same plate."
    hide screen console_screen
    "There! Problem solved!"
    mc "Monika, you're so cool."
    mc "I love you."
    m 1a "I love you too, [player]."
    "We ate our breakfast and went outside of my house."

    scene bg residential_day
    with wipeleft_scene

    "We prepared to walk to school."
    "And as usual, we are greeted by my other lovely girlfriends."
    s "Hi, Monika! Hi, [player]~"
    show sayori 1a at l33
    mc "Hi, Sayori."
    show sayori at face
    "She gave me a hug."
    s 4a "Here's my hug energy~"
    s "I missed you~"
    mc "I missed you too~"
    show sayori 4a at t33
    n "Hey, what about me?"
    show natsuki 1l at l32
    n "Hi, [player]."
    mc "Hi, Natsuki. You want a hug as well?"
    show natsuki 1n at f32
    n "Uuuuu..."
    n 42c "Fine. Just this once."
    n "It's not that I like your hugs or anything..."
    "I went in for a hug."
    show natsuki 1n at face
    n "You look gross."
    mc "I am?"
    n 1z "Yeah!"
    mc "You look cute!"
    show natsuki 4o at t32
    "She broke off the hug."
    n 4p "So you have chosen... {w} death."
    "Me and Monika laughed."
    show natsuki 1a at t32
    y "[player], wait for me!"
    show yuri 1a at l31
    y "Hi, Monika, Hi [player]."
    y "I'm ready to face my day with you by my side."
    mc "Glad to hear that, Yuri."
    show yuri 3s at face
    y "Come here, my cute boyfriend~"
    "She gave me a hug."
    y 3m "You smell nice..."
    y 3y1 "You... smell like... your pen~"
    y "Your pen that spilled its ink."
    mc "Hahaha."
    $ style.say_dialogue = style.edited
    y "I can't get enoughhhhhhhhhhhhh."
    show yuri 3a at t31
    $ style.say_dialogue = style.normal
    mc "Yuri..."
    mc "Are you ok?"
    show yuri 3n at s31
    "She got flustered."
    y 4c "I'm... I'm sorry."
    mc "Nah. It's okay, Yuri."
    mc "As long as you are okay..."
    "Sheesh. Yuri seems to have something bizarre going on her."
    m "Hey, [player]..."
    show sayori 4a at t44
    show natsuki 1a at t43
    show yuri 1a at t42
    show monika 1a at t41
    m "What about me?"
    m "Where's my hug?~"
    mc "Of course, Monika."
    mc "Why would I leave out my beautiful girlfriend?"
    mc "Come here~"
    show monika 1a at face
    "I hugged her tight."
    m "I'm so happy~"
    "She let go of me."
    show monika 1a at t41
    mc "Well then... Let's all walk to school now!"
    hide monika
    hide yuri
    hide natsuki
    hide sayori
    with wipeleft
    "We decided to walk to school."
    "Well, it's gonna be a long walk..."

    menu:
        "So It's time to have fun!"
        "Give Sayori a cookie.":
            "I approached Sayori and gave her a cookie."
            show sayori 4m at t11
            s "Is this for me?"
            show sayori 4r at h11
            s "Yay! I'm so happy!"
            s "Thank you, [player]!"
            s "You're such a sweetheart."
            s "You always satisfy my sweet tooth."
            s "I love you, [player]."
            "She smiled at me."
            "She took my hand as we walked down the road."
            s "I really wish we could go on like this forever, [player]."
            s "No amount of cookies or snacks can really replace the happiness I get if I'm with you."
            "I gave her a wide smile."
            mc "Of course!"
            mc "I'm happy that you're happy with me."
            mc "Rest assured that I will be your happiness."
            mc "And I love you too, Sayori."
            show sayori 4r at thide
            hide sayori
        "Give Natsuki a 'Parfait Girls' shirt.":
            "I approached Natsuki."
            mc "Yo, Natsuki."
            show natsuki 1a at t11
            n "Yo, [player]."
            "I gave her the shirt."
            n 1m "Is this.. for me?"
            mc "Yes."
            n 4r "I was planning on buying this with the money I saved up..."
            n 4p "And you went and ruined the experience for me!"
            n 4v "You, dummy, dummy, dummy!"
            mc "... Sorry, Natsuki."
            mc "I thought because I saw you eye on that shirt each time we pass by the shop.."
            show natsuki 1s at s11
            "Natsuki felt bad about what she said."
            n 1t "Hey, it's not I hate you about that or anything."
            n 1l "I appreciate the effort!"
            n "Thank you!"
            n "I guess, now I can use the money for something else!"
            n "I love you!"
            mc "I love you too, Natsuki."
            show natsuki 1l at thide
            hide natsuki
        "Give Yuri a new pen.":
            "I approached Yuri."
            mc "Hi, Yuri..."
            show yuri 1a at t11
            y "Hello, [player]."
            "I gave her the pen."
            y "[player]..."
            y 3y1 "I love it."
            y "I love ittttt."
            $ style.say_dialogue = style.edited
            y "I LOVE ITTTTTTTTTTTTTTTTTTTTTTTTTTTT."
            y "AHAHAHAHAHAHAHAHAHAHAHAHAHA."
            $ style.say_dialogue = style.normal
            "I felt a little bit weird."
            mc "Yuri..."
            mc "If you don't feel ok, let me know, ok?"
            "Yuri came back to her senses."
            show yuri 3p at h11
            y "Ah!"
            y 4a "Sorry, Sorry!"
            y 4c "Please don't hate me!"
            mc "No, no!"
            mc "It's okay!"
            mc "I'm here for you."
            mc "And I love you nonetheless."
            y 3s "I love you too, [player]."
        "Give Monika a... I don't know. She has everything already.":
            "I approached Monika."
            mc "Monika?"
            show monika 1a at t11
            m "Yes, [player]?"
            m 5a "Wanted to walk beside me, I suppose?"
            mc "Um... yeah, but actually..."
            mc "I wanted to give some sort of a gift for you."
            mc "But since you can spawn anything out of thin air..."
            mc "I really don't know what to give you!"
            mc "Ahahaha..."
            m 4l "Ahahaha~"
            "She laughed at me."
            m 4a "Well... if there was something that I could have that I couldn't get for myself..."
            show monika 5a at h11
            m "Is that your time, love, and affection."
            m "I'm happy whenever you just spend time with me."
            m "I love you, [player]."
            mc "I love you too, Monika."
            show monika 5a at thide
            hide monika
    "And with that, we arrived at our destination."

    scene bg class_day
    with wipeleft_scene

    "Classes are boring as usual."
    "If you're really not interested in it and you're mind is on something else."
    "You couldn't concentrate."
    "But anyways..."
    "I'll make it up to Monika today."
    "I should spend time with her."
    "I would really love if things speed up."
    "This teacher talks forever."
    "..."
    ".."
    "."
    $ style.say_dialogue = style.edited
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    mc "[gtext]!"
    $ style.say_dialogue = style.normal
    "Class is over before i know it."
    mc "Yes! Time for club!"

    stop music fadeout 2.0
    scene club_day
    with wipeleft_scene

    play music t3

    show monika 1g at l31
    m "Aw, man..."
    m "I'm the last one here again!"
    mc "Don't worry, I just walked in too."
    show yuri 1f zorder 3 at f32
    y "Were you practicing piano again?"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1l "Yeah..."
    m "Ahaha..."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1m "You must have a lot of determination."
    y "Starting this club, and now picking up piano..."
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Well, maybe not determination..."
    m "But I guess passion."
    m "Remember that the club wouldn't be here if it wasn't for all of you."
    m 1b "And I'm super happy that you're all willing to help out for the festival, too!"
    show natsuki 1z zorder 3 at f33
    show monika zorder 2 at t31
    n "Aaah, I can't wait for the festival!"
    n "It's gonna be great!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f31
    m 1d "Eh?"
    m "Weren't you complaining about it just yesterday, Natsuki?"
    show monika zorder 2 at t31
    show natsuki 2a zorder 3 at f33
    n "Well, yeah."
    n "I'm not talking about {i}our{/i} part of the festival."
    n 4l "But it's a whole day of school where we get to play and eat all kinds of delicious food!"
    show natsuki zorder 2 at t33
    mc "You sound a bit like Sayori all of a sudden..."
    show natsuki zorder 3 at f33
    n 4a "Monika! Do they usually have fried squid?"
    show natsuki zorder 2 at t33
    show monika 2a zorder 3 at f31
    m "Squid...?"
    m "That's a pretty specific thing to look forward to..."
    show monika zorder 2 at t31
    show natsuki 2k zorder 3 at f33
    n "Oh, come on."
    n "Are you saying you don't like squid?"
    n "You, of all people?"
    show natsuki zorder 2 at t33
    show monika 1d zorder 3 at f31
    m "Eh? I didn't say I don't like it."
    m "Besides, what do you mean by 'you of all people'?"
    show monika zorder 2 at t31
    show natsuki 1d zorder 3 at f33
    n "Because!"
    n "It's right in your name!"
    n 4z "Mon-ika!"
    show natsuki zorder 2 at t33
    show monika 5b zorder 3 at f31
    m "Eh?!"
    m "That's not how you say my name at all!"
    m "Also, that joke makes no sense in translation!"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f33
    n 4m "...?"
    show natsuki zorder 2 at t33
    show monika 4l zorder 3 at f31
    m "Ah...never mind!"
    m "Let's just focus on our own event for now, okay?"
    show monika zorder 2 at t31
    show natsuki 2a zorder 3 at f33
    n "Ehehe."
    n "Fine, fine."
    n "Your reactions aren't as fun as Yuri's or Sayori's, anyway."
    show natsuki zorder 2 at t33
    show yuri 2h zorder 3 at f32
    y "Excuse me..."
    show yuri zorder 2 at t32
    mc "Where is Sayori anyway?"
    mc "Oh, there you are."
    hide monika
    hide yuri
    hide natsuki
    with wipeleft
    "I approached Sayori who is sitting down, writing stuff."
    s "Yuri is a raccoon..."
    s "Oh hi, [player]."
    show sayori 1a at t11
    s "I'm just writing my poem for the festival!"
    s 4r "I'm really excited!"
    mc "Sayori..."
    mc "Did you seriously write 'Yuri is a raccoon'?"
    s 1l "Oh hehhehe, sorry."
    s "I'm just out of words at the moment..."
    s "But anyways..."
    s 1a "Hopefully you are ready for the poetry performance for the festival!"
    mc "Of course!"
    mc "I will try my best!"
    show sayori 4r at h11
    s "That's the spirit!"
    show sayori 4a at face
    "She gave me a hug."
    mc "I love you, Sayori."
    s "I love you too, [player]."
    show sayori 4a at t11
    s "I'll be continuing to write my poem."
    s "Go spend time with the others."
    mc "Okay, Sayori."
    show sayori 4a at thide
    hide sayori
    "And with that, Sayori continues to write her poem."
    "Hopefully Yuri doesn't see what she wrote."
    y "Sayori! How childish of you!"
    "And she saw it."
    "Well, Everyone seems to be doing something."
    "Sayori and Yuri are talking."
    y "I AM NOT A RACCOON!"
    "More like... a heart-to-heart conversation."
    "Natsuki is reading beside the closet, sitting on the floor."
    "And Monika seems to be doing some stuff as well."
    "I have decided to spend time with Monika today."
    "My goddess."
    "For real. She can do anything."
    "I approached her in her desk."

    return
    