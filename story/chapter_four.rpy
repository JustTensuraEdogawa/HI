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
    "This is very nerve-racking, but I have to set my girlfriends free."
    "I gently open the clubroom door."
    
    scene bg club_night
    with wipeleft_scene

    "To my surprise, there is a figure sitting on Monika's desk, performing some sort of voodoo ritual type of thing."
    "I approached the figure."
    mc "Hey! what are you doing?!"
    $ style.say_dialogue = style.edited
    a "So you've come."
    show amy robe at t32
    a "Hehehe, you're pretty resilient. You will be part of my army soon..."
    a "Name's Amethyst. Amethyst-sama."
    $ a_name = 'Amethyst'
    a "Better address me that way from now."
    $ style.say_dialogue = style.normal
    mc "You're hurting my girlfriends!"
    $ style.say_dialogue = style.edited
    a "Ara-ara, so they are {i}your{/i} girlfriends?"
    a "What a pleasant surprise."
    a "I despise you..."
    a "You, being popular with girls..."
    a "You have lots of friends!"
    a "Girlfriends at that!"
    a "While here I am, stuck at being alone..."
    a "Well who am I kidding?"
    $ style.say_dialogue = style.normal
    "She starts to cry."
    $ style.say_dialogue = style.edited
    a "I am always alone, because of my weird fetish."
    a "So what if I like spiders?"
    a "I can be caring!"
    a "All I wanted is to never be alone..."
    a "Is that too much to ask?"
    a "But now... with the power of the Dark Arts I read here in the library for hours..."
    a "I can now form an army of my own..."
    a "Mindless feeble humans obeying my will..."
    a "I WILL NEVER, EVER, BE ALONE ANYMORE!!!"
    a "AHA A HA HA HA HA HA HA HA HA HAHAHA HA AHA  HA HA!"
    $ style.say_dialogue = style.normal
    mc "I... feel you..."
    mc "I was... alone... too."
    mc "I am a NEET."
    mc "Or so I was."
    mc "Stop this nonsense."
    mc "You're just scaring away the people around you."
    "She shouted angrily."
    $ style.say_dialogue = style.edited
    a "AND YOU'RE RUBBING IT IN!"
    a "YOU'RE MAKING IT ONLY WORSE!"
    a "I'VE HAD ENOUGH!"
    a "I can see that you disabled my soul control."
    a "I can reactivate it again HAHAHAH!"
    $ style.say_dialogue = style.normal
    "She presses a button in the relic she's holding."
    mc "No! You can't do this to my girlfriends!"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    mc "Holy Aura!"
    "I managed to release a holy aura."
    "Most of my girlfriends were protected and not affected."
    "Except... {w}two..."
    "Oh no."
    show sayori turned e0a rup casual lup at t31
    show yuri turned e0a rup casual lup at t33 
    "She still got Sayori and Yuri."
    m "Sayori! Yuri!"
    c "You're not getting away with this!"
    mc "Stop!"
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    n "It's clear she aint listening."
    n "So I'm about to talk some sense into her with my fists!"
    $ style.say_dialogue = style.edited
    a "I wouldn't do that if I were you."
    a "I could make these 2 here kill each other if I want."
    s "Amethyst-sama... It hurts..."
    y "Amethyst-sama... I..."
    a "Go ahead."
    a "Tackle me."
    $ style.say_dialogue = style.normal
    m "I ain't doing that to you."
    "Monika ain't playing."
    $ style.say_dialogue = style.edited
    a "Oh, you're right."
    a "It was interesting when I took over your soul."
    a "It just sucks that I flunked programming class."
    a "If I had learned more about it, I could've ruled the world."
    a "But... I have something that you don't..."
    $ style.say_dialogue = style.normal
    "She chanted some sort of spell."
    "Monika fell on the floor."
    m "My arms! They're so heavy!"
    $ style.say_dialogue = style.edited
    a "I made your arms as heavy as a wrecking ball."
    a "If you can't code, you can't use your power."
    $ style.say_dialogue = style.normal
    k "Monika!"
    "Ken attended to Monika."
    "Cara and Natsuki just stood there, not knowing what to do."
    $ style.say_dialogue = style.edited
    a "If you all agree to be my slave, this will all be over."
    $ style.say_dialogue = style.normal
    "I need some sort of water to atleast free one of them..."
    "Water... water..."
    "I looked around."
    "I looked at Cara."
    "I looked at Natsuki."
    "And an idea popped on my head."
    mc "Natsuki?"
    n "Not now, [player]."
    "I hugged Natsuki tight."
    n "Wait--"
    n "W-ww-w-w-w-what are you d-d-d-oing?"
    n "Get off me!"
    mc "I just wanna hug my girlfriend, that's what."
    n "Why now, dummy?!"
    c "Yeah, [player]. Why now?"
    c "We're in a dire situation!"
    $ style.say_dialogue = style.edited
    a "It seems that your boyfriend lost his mind now."
    $ style.say_dialogue = style.normal
    mc "Thank you Natsuki. I love you."
    mc "Holy aura!"
    "I splashed my holy-infused water to Sayori."
    "Sayori fell down."
    show sayori at thide
    hide sayori 
    s "Owww. my head."
    mc "Sayori!"
    "I managed to get her and protect her from being controlled."
    $ style.say_dialogue = style.edited
    a "WHAT. {w}DID. {w}YOU. {w}DO?"
    $ style.say_dialogue = style.normal
    mc "I infused Natsuki's sweat with my aura and splashed it to Sayori."
    mc "It's really hard to make her nervous."
    mc "But I'm glad it worked!"
    play sound "sfx/slap.ogg"
    mc "Ow!"
    n "You dummy!"
    n "If I would've known, I wouldn't be flustered like this!"
    mc "Natsuki, If you knew, then you wouldn't be nervous."
    n "Uuuuu."
    n "Thanks."
    n "It's not I liked that or anything..."
    "Cara just laughs."
    c "You're cute, Natsuki."
    n "Stop that!"
    $ style.say_dialogue = style.edited
    a "It seems I underestimated you..."
    a "I should've gone for you first!"
    a "Say goodbye!"
    show amy at thide
    hide amy
    show yuri b1b e0b mo at t11
    $ style.say_dialogue = style.normal
    "Yuri armed herselves with the 3 knives she had."
    $ style.say_dialogue = style.edited
    y "Three-knives style..."
    show yuri at face
    $ style.say_dialogue = style.normal
    "She's fast."
    "She's in front of me."
    s "YURI STOPPP!"
    play sound "sfx/stab.ogg"
    "Sayori moved herself in front of me."
    "Sayori was stabbed."
    mc "Sayoriiiiiiiiiiiiiiiiiiiiiiiiiii!"
    $ style.say_dialogue = style.edited
    y "HEHEHEHEHEHE..."
    show yuri at t11
    $ style.say_dialogue = style.normal
    "I pushed Yuri away."
    mc "{b}That. {w}Is...{/b}"
    mc "{b}ENOUGHHHHHHHHHHHHHH!{/b}"
    play sound "mod_assets/powerup.mp3"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    scene bg club_day
    "I released a very powerful aura..."
    "So strong that the light I emit makes it look like it's afternoon."
    "Amethyst saw me flashing."
    $ style.say_dialogue = style.edited
    a "What is happening?"
    $ style.say_dialogue = style.normal
    "Tables, chairs, were shaking."
    $ style.say_dialogue = style.edited
    a "Argh!"
    $ style.say_dialogue = style.normal
    "She got pushed to the front of the clubroom."

    scene bg class_day
    with wipeleft_scene

    "I teleported in front of her."
    mc "Checkmate."
    "The hoodie on her robe fell."
    "And we both looked each other in the eye."
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    "ZING!!!"
    stop music fadeout 2.0
    scene bg class_night
    with dissolve_cg
    "Oh hell nah."
    "Renpy-sama... WHYYYY?"
    "Well, she is supposed to be one of my girlfriends."
    "I'm supposed to know the drill..."
    "Here goes nothing."
    mc "Amethyst?"
    mc "Wait..."
    mc "Amy?"
    show amy 4er at t32
    "This is my classmate, Amy."
    "She sits way back in our classroom."
    "I only heard her name every school attendance."
    "She always disappears during lunch breaks."
    "I never actually got to talk with her."
    "This is the {i}first{/i} time."
    $ a_name = 'Amy'
    a "..."
    a "Oh, it's you, [player]."
    a "I'm sorry."
    show natsuki 5bh at t33 
    n "You know this girl?"
    mc "Yeah, she's my classmate."
    show natsuki 5bw at f33
    n "Your class sure have a lot of weird people in it."
    n 5bl "Starting with you."
    show natsuki at t33
    show cara 3ac at t31
    c "[player]! We're losing Sayori!"
    c "She's not breathing!"
    mc "What?"
    show cara at thide
    show amy at thide
    show natsuki at thide
    hide cara
    hide amy
    hide natsuki
    show bg club_night
    with wipeleft_scene

    "I went back to Sayori."
    "Her body looks paler than before."
    play music t9
    show yuri turned rup cry casual mk lup at t33 
    y "I'm sorry, I'm sorry!"
    mc "It's not your fault, Yuri."
    show yuri ml at f33
    y "But I stabbed her!"
    mc "I'm not blaming you for this."
    mc "Let's focus on Sayori at the moment."
    show yuri at t33
    "I panicked."
    mc "Meiji? Are you there?"
    mj "Hello, Master! How may I of service today?"
    mc "Please analyze Sayori."
    mc "Is there anything we can do for her?"
    mj "Analyzing.{w=1.5}.{w=1.5}."
    mj "Analysis complete."
    mj "I'm sorry, [player]."
    mj "She's gone."
    mc "What?!"
    mc "I have tons of powers! Can we bring her back?"
    mj "Unfortunately, It is beyond your power."
    show monika forward ce cry casual me at t31
    m "It's true, [player]."
    m lpoint e1h "Even I, can't bring back people from the dead."
    show monika mh at f31
    m "True, I can create, destroy, delete, copy, paste."
    m "But that's that."
    m "If a character file is dead, then I can only copy that file, delete, recreate. But it's still going to be lifeless."
    m "I'm not as powerful as Renpy-sama."
    m "If a soul has left one's body, that's it."
    mc "..."
    mc "I can't accept this..."
    "The tables and chairs begin to violently shake again."
    show bg club_day
    with dissolve_cg
    "I'm going to {b}end{/b} everything."
    "My best friend died."
    "My girlfriend died."
    "{b}I'm going all out.{/b}"
    m "... Stop!"
    $ run_input("os.GodMode/mc.chr = False", "Successfully deactivated.")
    m "One more..."
    $ run_input("os.setpowerlevel/mc.chr = 5", "Successfully set.")
    m "There..."
    hide screen console_screen
    show bg club_night
    with dissolve_cg
    "I lost my God powers."
    "Monika took it away from me."
    "I managed to calm down."
    mc "Sorry, Monika."
    mc "I got a little carried away."
    mc "But Sayori..."
    a "Hey, [player]."
    mc "Amy?"
    show amy 4er at t32
    "Amy stepped forward."
    show yuri turned vang casual om at f33
    y "You..."
    y "You did this to us!"
    y "Now we lost Sayori!"
    show yuri at t33
    show amy 4eu at f32
    a "I'm sorry, okay?!"
    show amy at t32
    show monika forward rhip vang casual om at f31
    m "Your apology won't bring her back!"
    m lpoint "I'll just delete you right here, right now!"
    show amy at f32
    show monika at t31
    a "Wait!"
    a "I understand you're angry at me..."
    a 4ji "But..."
    a 4eu "I can bring her back to life."
    a "I have taught myself revival spells."
    a "Courtesy of the Dark Arts book I found in the library."
    mc "What?"
    mc "You can {i}revive{/i} dead people?"
    a 7k "Yeah."
    a "I just need the right tools."
    mc "Tell me what it is, and Monika will spawn it for you."
    a "Okay..."
    a "I need..."
    stop music fadeout 2.0
    hide monika
    hide amy
    hide yuri 
    with wipeleft
    "Amy and Monika prepared the things needed for the revival spell."
    show amy 61u at t11
    a "Here goes nothing..."
    $ style.say_dialogue = style.edited
    a "Efil ot kcab emoc, Iyoras, eeht dnammoc I, ssenkrad fo rewop eht yb!"
    a "Secret Dark Arts spell: RESURRECTION!"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    $ style.say_dialogue = style.normal
    "A brief flash of light envelops the room."
    s "..."
    s "*cough* *cough*"
    s "Ow... My head..."
    show amy at t42
    show sayori 1bm zorder 3 at t43
    s "I haven't said goodbye to St. Cow!"
    show yuri turned cry casual mb lup rup at t44 
    y "Sayori!"
    play music t9
    show yuri at t43
    y "We thought we lost you..."
    y mi "I'm sorry!"
    show monika forward cry casual mb at t41 
    m "Sayori!"
    m "The spell worked!"
    show sayori at thide
    show yuri at thide
    show monika at thide
    hide monika 
    hide yuri 
    hide sayori 
    show amy at t11
    "We all hugged Sayori."
    m "Hey, Amy, you're not that bad at all."
    show monika casual b1b mb lpoint at t21
    show amy 1a at t22
    m "You're just isolated."
    m "Alone."
    m "I'm willing to forgive you."
    show amy 1ji at f22
    a "Again, I'm sorry."
    a "I'm just... so lonely..."
    mc "Hey, I do get the feeling..."
    mc "Hey, why don't you join the Literature Club?"
    mc "I'm inviting you over!"
    e "What?"
    n "What the heck?"
    m ldown b1e mg "I know I forgived her, [player]."
    m lpoint "But it doesn't mean she's invited."
    a "I understand."
    mc "I'll take the blame for this..."
    mc "In fact..."
    show amy at face
    show monika ldown at t31
    mc "Amy, I'm willing to accompany you so that you'll never be alone."
    mc "I'll accept you to be one of my girlfriends..."
    e "What?!"
    n "Aw, come on man!"
    a 2ex "T-that's too much, [player]."
    a "I can't be with you after all I've done..."
    mc "No, It's alright."
    show natsuki 5be at t33 
    n "What do you {i}mean{/i} it's alright?"
    n "She made Yuri kill Sayori!"
    mc "Girls, I understand."
    mc "But please think of this differently."
    mc "She's just lonely."
    mc "Yeah it is inexcusable to kill somebody for it but..."
    mc "If it wouldn't for her, Sayori is permanently gone."
    mc "She can be caring she said if she has friends."
    mc "We can help her."
    mc "I'll take all the blame for what she caused."
    mc "Monika, delete me if you like to delete her."
    mc "Natsuki, beat me to a pulp if that's what you want to do to her."
    mc "I'll take the blame since she's my classmate."
    mc "I should've gotten to know her since the first day of class."
    mc "None of this would've happened if I became friends with her then."
    mc "This is all my fault."



    return
