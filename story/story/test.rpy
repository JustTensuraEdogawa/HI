label test:

    stop music fadeout 2.0
    scene black 
    with dissolve_scene_full

    scene bg club_day
    with dissolve_scene_full

    show natsuki 1a at t11
    $ n_name = "Natsuki"
    n "Hello!"
    n "This is for testing purposes only."
    n "Let's see if I can do this right..."
    hide natsuki 
    play sound "mod_assets/sfx/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show ssnatsuki 1e zorder 4 at h11
    pause (1.0)
    ssn 1c "Did I do it right?"
    ssn "I did?"
    ssn 4d "Oh yeah!"
    show natsuki 4d zorder 1 at i11
    hide ssnatsuki 
    with dissolve_cg
    pause (1.0)
    n 4z "I thought I wouldn't pull it off!"
    n 1d "Anyways, that's all I wanted to show you."
    n "See you when this mod is released!"
    n "Bye!"
    show natsuki at thide
    hide natsuki

    return