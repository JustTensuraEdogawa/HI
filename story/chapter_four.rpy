label chapter_four:

    play music m1

    "..."
    mc "Hello?"
    mc "Renpy-sama?"
    "Huh."
    "He's not here again."
    "I hear heavy footsteps."
    m "[player], Help!"
    mc "Monika?"
    show monika forward b1b e1g casual mk at t11
    "She looks tired, in panic and crying."
    "What happened?"
    show monika forward b1b e1g casual ml at f11
    m "You've got... to... help us..."
    m "Sayori... Yuri... Natsuki..."
    m "{b}They became mindless zombies!{/b}"
    mc "Wait, WHAT?"
    m "You're... our... only... hope..."
    m "I'll become one as well..."
    m lpoint "Let me... give... you... this..."
    $ run_input("os.GodMode/mc.chr = True", "Set MC to God Mode.")
    m "Just... one... more..."
    $ run_input("os.setpowerlevel/mc.chr = over 9000", "Successfully set.")
    m "There... I did it..."
    hide screen console_screen
    "I became overflowing with power again." 
    m "Call Cara... and Ken..."
    m "You'll need... their assistance..."
    mc "Why?"
    mc "Is there another threat like Sukini?"
    show monika forward b1a e4a casual cm at t11 
    "There is no response."
    $ style.say_dialogue = style.edited
    m e0a mh "ALL HAIL THE GREAT AMETHYST-SAMA..."
    show monika at thide
    hide monika
    $ style.say_dialogue = style.normal
    mc "Wait... what?"
    "I need to wake up..."
    "But no one is here!"
    "How?"
    "I stepped on a paper."
    "Wait..."
    "This is the paper I used to wake up."
    "C'mon where's the button?"
    "I pushed the button."

    scene bg bedroom_night
    stop music
    play sound fall

    "I woke up."
    "It's... 3am."
    "Fitting for what happened."
    play music ct
    "I need to inform Cara and Ken about the situation."
    "I don't have their numbers though."
    "C'mon think..."
    "I suddenly hear them in my mind..."
    c "[player]..."
    c "Protect me~"
    k "[player]..."
    k "Protect Monika~"
    "Is this {i}telepathy{/i}?"
    "I can telephatically communicate to them!"
    "So this power that I had..."
    "Has more to offer for me!"
    "I tried to talk to them using my mind."
    mc "Cara? Ken?"
    mc "Please come here, I need your help."
    mc "I hope you can hear me..."
    "Agh they're not responding..."
    "I guess I have no choice..."
    "I went outside the house."

    scene bg house_night
    with wipeleft_scene

    "It's pretty quiet in here."
    "Well, who am I kidding, It's 3 am..."
    $ style.say_dialogue = style.edited
    s "..."
    s "Must... bring sacrifices for... Amethyst-sama."
    show sayori turned b2a e0a casual mh at t11
    $ style.say_dialogue = style.normal
    "She looks pale."
    mc "Sayori?"
    "She doesn't respond."
    show sayori lup rup at face
    "I tried to hold her."
    mc "Sayori! Snap out of it!"
    $ style.say_dialogue = style.edited
    s turned b1e e3a casual mp "GET OFF ME MEANIE! KHHHHHH!"
    show sayori ldown rdown at t11
    $ style.say_dialogue = style.normal
    "She really is a mindless zombie..."
    $ style.say_dialogue = style.edited
    y "WHO DARES TOUCH SAYORI??"
    show yuri turned e3a casual mh at t22
    show sayori at t21
    y "YOU DARE TOUCH HER, I'LL KILL YOU..."
    y turned b2c e3a rup casual mo "ILL SACRIFICE YOU TO AMETHYST-SAMA!"
    $ style.say_dialogue = style.normal
    "She pulled out a knife."
    "Yuri?"
    mc "Please don't Yuri!"
    show yuri at face
    "She managed to hold me."
    show yuri ml at t22
    play sound "sfx/slap.ogg"
    "I managed to slap away the knife."
    $ style.say_dialogue = style.edited
    y mo "Don't worry..."
    y mr "I have a lot of those!"
    $ style.say_dialogue = style.normal
    "She pulled up 3 more of them."
    "She held one at her left, one at her right, and one at her mouth."
    mc "Did Zoro's soul got lost and possessed you Yuri?"
    $ style.say_dialogue = style.edited
    y "Three-knives style..."
    $ style.say_dialogue = style.normal
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori at lhide
    show yuri at lhide
    hide sayori 
    hide yuri 
    "I managed to release a small fraction of my aura, which blew them a few meters away."
    mc "Sorry, girls."
    "I need to snap them out of whatever voodoo stuff they are in."
    play sound "mod_assets/it.mp3"
    show natsuki turned b1e rhip e3a casual mo lhip at i11
    $ style.say_dialogue = style.edited
    n "YOU LOOK PRETTY STRONG... LET'S FIGHT!"
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    n mr "FOR AMETHYST-SAMA!!!!!"
    $ style.say_dialogue = style.normal
    "She charged instantly."
    "She's gotten stronger."
    "I guess I'll have to use more power..."
    c "[player]!"
    show cara 1a at t22
    show natsuki at t21
    "She blocked Natsuki's attack."
    c 1e "I'll handle this..."
    c 1h "Take care of the others!"
    "Cara's here."
    mc "Right, right."
    show cara at thide
    show natsuki at thide
    hide natsuki
    hide cara 
    "I left both of them alone."
    "I tried to approach Sayori and Yuri once again."
    $ run_input("os.restrict/mc.chr", "mc.chr successfully restricted.")
    "I suddenly stopped moving."
    "{b}I can't move!{/b}"
    show monika forward b1a e0a casual mh lpoint at t11
    $ style.say_dialogue = style.edited
    hide screen console_screen
    m "NO ESCAPE..."
    m "ALL HAIL AMETHYST-SAMA!"
    m e3a mb b1e "A H A H A H A H A H A H A H A!"
    $ style.say_dialogue = style.normal
    k "[player]!"
    show ken 1a at t44
    pause(0.5)
    show ken at lhide
    hide ken 
    show monika at lhide
    hide monika 
    "Somebody tackled Monika."
    mc "Ken!"
    k "I'll deal with Monika."
    k "I don't want you hurting her!"
    mc "Okay, okay."
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "I released more aura to free myself."
    "I approached Sayori and Yuri."
    "They're still out cold."
    "I don't know what to do."
    "If I had something like 'Great Wisdom King Gabriel'..."
    "You know, the skill Reimu Torrents had as a Demon Lord slime."
    mj "Hello, Master!"
    mj "It seems your subconsious mind called me. How can I help?"
    "I hear a voice in my head."
    mc "Who are you?"
    mj "It's me, your ultimate skill, 'Wisdom Lord, Meiji Chizu'!"
    mj "At your service!"
    "Sweet."
    "I never knew I had this."
    "Monika is sure powerful to have given me this, and everything else."
    mc "Okay... I need you to analyze and assess my girlfriends."
    mj "Sure thing, Master!"
    mj "Just put your hand on them and I'd be able to give my findings."
    mc "Okay!"
    "I put my hand upon them."
    mj "Analyzing.{w=1.5}.{w=1.5}."
    mj "Analysis complete."
    mj "Their souls have been controlled."
    mj "They touched a relic that seized control over their souls."
    mc "I see, I see."
    mc "How do I get them back to normal?"
    mj "You need to break the relic."
    mj "But the relic is currently under possession of someone..."
    mj "She's located in the clubroom."
    mc "But I need to break them free now!"
    mj "You can try to also infuse your holy aura with something {i}wet{/i}..."
    mj "Splash it on their face."
    mj "But if the wielder of the relic reactivates it, They will be in control again."
    mc "Id take that chance."
    mc "Thank you, Meiji."
    mj "Happy to assist, Master."
    "I tried to manipulate the water in our backyard."
    "To my surprise, it moved at my will."
    "Okay... I can waterbend too. Sweet!"
    "I gathered enough water and infused it with my holy aura."
    "I splashed it onto Sayori and Yuri."
    "They woke up."
    s "W-where am I?"
    s "Y-yuri?"
    y "My head..."
    y "All I remembered is that we passed out after you touched that weird thing..."
    mc "Sayori! Yuri!"
    play sound fall
    "I hugged both of them."
    mc "You're safe now."
    y "[player]..."
    s "What's going on?"
    mc "No time to explain."
    mc "Just look around."
    "We all looked around."
    show monika forward casual e3a mo b1e at t41
    show ken 1g at t42
    show cara 1g at t43
    show natsuki cross e3a casual mo at t44
    "They're trying to hold off both of them."
    s "What's wrong with them?"
    mc "The relic made all of you do that."
    mc "You picked up some strange item at the ground, did you?"
    s "Ah yeah..."
    s "Sorry."
    mc "It's okay, Sayori."
    mc "As long as you're not hurt."
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "I released a slightly powerful aura."
    show monika at lhide
    hide monika
    show ken at lhide
    hide ken 
    show cara at lhide 
    hide cara 
    show natsuki at lhide 
    hide natsuki 
    "They all got knocked out."
    c "Owww..."
    k "H-hey! Watch it!"
    mc "Sorry."
    "Both Natsuki and Monika got knocked out cold."
    mc "Sorry, girls."
    "I gathered more water, infused it, then splashed it to both of them."
    "They immediately woke up, feeling woozy."
    m "Oww...."
    n "My head..."
    n "What the heck am I doing here?"
    m "Ugh..."
    m "I had a strange dream..."
    mc "It's not a dream."
    "I explained to all of them what happened."
    m "So I did give you your powers back and I became a mindless zombie..."
    mc "Yeah, you did."
    show sayori 2bi at t41
    show yuri 1bu at t42
    show natsuki 5bn at t43
    show monika casual forward e4a at t44
    mc "It's not your fault, girls."
    mc "We just have to find the wielder of this stupid relic."
    show yuri 2br at f42
    y "Yeah. Whoever this person is must pay for what he did."
    mc "According to my intuition..."
    mc "That person right now is in the clubroom."
    mc "Let's go there, now."
    show sayori 2bj at f41
    show natsuki 4be at f43
    show monika forward b1e e2a casual mi at f44
    e "Roger!"
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "We headed towards the school grounds..."
    "Hopefully no one sees us breaking in."

    scene bg corridor_n
    with wipeleft_scene

    "We made it inside the school building."
    "We ran across the corridor."
    "It feels a bit... ominous."
    "Until all 7 of us arrived at the clubroom..."
    "I can hear someone whispering..."
    $ style.say_dialogue = style.edited
    a "Hehehe~"
    a "They're approaching me now."
    a "I can't be a good person if I don't welcome them properly..."
    a "H E H E H E HE EHE E EHE E HE EH EH EHE ..."
    $ style.say_dialogue = style.normal
    "..."
    "How does she know were coming?"
        




    return