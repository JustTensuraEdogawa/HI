label teaser:

    scene black
    with dissolve_scene_full
    stop music fadeout 2.0

    pause(1.0)
    "Previously on '100 Club Members who Really, Really, Really, Really Love You'..."

    scene bg corridor
    with dissolve_scene_full
    pause(2.0)

    $ c_name = 'Cara'
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

    play music t100

    scene bg club_day
    with wipeleft

    $ n_name = 'Natsuki'

    show natsuki 4e at t11
    n "Who the heck are you missy?"
    show natsuki at t21
    show cara 1a at t22 
    c "My name's Cara. I'm from the karate club."
    
    scene bg closet
    with wipeleft

    show cara 1h at t22
    c "I won't let you hurt and bully [player] like that, Natsuki."
    show natsuki 4d at t21
    n "Ho, are you sure about that, Cara?"
    n 4y "Just so you know that nobody beats me when it comes to punching."
    show cara 1h at f22
    c "Well then you're on!"
    "Oh no. I need to save them from this situation..."

    scene bg residential_day
    with wipeleft

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

    scene bg club_day
    with wipeleft

    $ s_name = 'Sayori'
    $ y_name = 'Yuri'

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
    "Out of nowhere, we heard a shout."
    k "I finally found you, [player]."
    show sayori 4m at h31
    show cara 3af at h32
    show yuri 3p at h33
    "We were startled by that voice."
    
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full

    scene bg end_teaser
    with dissolve_scene_full
    pause(5.0)

    t "That is all for now."
    t "If you want, I could use some assistance with other assets for this mod."
    t "Shoot me a DM in my Discord if you'd like to help!"
    t "Name's 'tensuraedogawa'"
    t "Thank you!"

    $ renpy.quit()

    return


