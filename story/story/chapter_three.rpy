image n_kill:
    subpixel True
    "mod_assets/nutsucky.png"
    
label chapter_three:

    play music m1

    r "..."
    r "Well, nothing's interesting in this weekend..."
    r "I'm just gonna say they did a fantastic job in preparing for the school event."
    r "So..."
    r "Let's fast forward to Monday!"

    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the school event."
    "I am excited to go to school today."
    play music sn
    "This feels like the festival."
    "Since everyone else have prepared for the school event, they all went to school early."
    scene bg class_day
    with wipeleft_scene
    "Class is just as usual..."
    sz "Alright, class..."
    show sayozuki 3bb at t11
    sz "Don't forget to support the school by attending our school event later after class!"
    sz 1be "We have prepared for it night and day for all of you!"
    sz 1bb "Alright, class dismissed."
    show sayozuki at thide
    hide sayozuki
    "Everyone seems to be stoked as well."
    "Well, I really can't wait for it."
    "I wonder what my girlfriends prepared for me..."
    "I head straight to the event hall."
    scene bg stage
    with wipeleft_scene
    "The event hall is filled with students and teachers alike."
    pr "Thanks for coming to our school event featuring 100th year anniversary of our school!"
    pr "And now from the word of our beloved owner of the school..."
    "The owner stepped up the stage and said encouraging words."
    pr "Well, thank you for those encouraging words..."
    pr "Let's enjoy the food set by the dedicated team of our debate club leader, Miss Kotonoha!"
    "Oh... so it was the secret that they're keeping from me."
    "They are the chefs of the event!"
    "Kotonoha steps up the stage."
    show kotonoha toward happ lup om at t11
    kt "I thank you all for being here on this event."
    kt lchest "Me, Sayochi, Sayori, Sayozuki, and Mizumi helped in making all of this food that we will enjoy a bit later."
    kt ce ldown "Hope that you consider joining the debate club!"
    m "What?!"
    show kotonoha oe cm at t11 
    "Monika is about to step up, but Kotonoha looked at her with a smug on her face."
    kt om "... but I couldn't have done all of these work without Monika's club members too..."
    kt ce "Hope you consider joining the Literature Club as well!"
    kt curi mc "Of course I won't stop you if you'd join the debate club..."
    kt happ om ce lchest "I'm the better club president after all!"
    m "Why you little--"
    s "Calm down, Monika..."
    kt oe ldown "That's all, enjoy the food we prepared!"
    show kotonoha at thide 
    hide kotonoha 
    "I laughed at both of them."
    "I enjoyed the food that is being served at the event hall."
    "I hope I do get to see the performance."
    pr "And as we enjoy our meal... please enjoy a wonderful performance directed by the president of our Literature Club, Monika."
    m "Thank you so much."
    "Monika stepped up the podium."
    show monika 3b at t11
    m "Hi, this is Monika, the president of the Literature Club."
    m "Please consider joining our club..."
    m forward happ om ce "Because members of other clubs came to join us too!"
    m lpoint rhip "Like Cara, from the karate club..."
    m ce rdown ldown "And even Kotonoha herself, the debate club president!"
    m lean happ om "If she joined our club, she's probably bored out of her mind on her club..."
    m ce "But if you still want to join her club, it's up to you!"
    m forward happ om oe "Now without further ado..."
    m lpoint "Put your hands together for the Literature Club members' play performance..."
    m "Titled... {i}'Melodious Farewell'{/i}."
    m ldown "Based on a certain manga, which some of my members considered 'literature'."
    m cm "Enjoy."
    show monika at thide 
    hide monika 
    "The play is about to start..."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    scene bg play_residential 
    with dissolve_scene_full

    $ c_name = "Meizu"
    c "..."
    c "It's the day of the festival."
    show cara turned mb at t11
    c "I need to see Satori."
    c "She's been really, really, looking forward to spend time with me!"
    c "I need to call her and get her attention."
    show cara turned ma at t11 
    "She tried to call Satori."
    "But no response from her."
    c me "Huh? That's odd."
    c "I need to go check on her."
    "She went to her house to check her."
    scene bg play_house
    with wipeleft_scene
    c "Satori?"
    "Still no response."
    c "Ahhh, I think it's best for me to check on her."
    scene black
    with wipeleft_scene
    "In times like this Satori should be up and ready."
    "She's the Vice President of the anime club after all."
    "She's still not responding tho..."
    "It leaves Meizu no choice..."
    "She punches the door open."
    c "...Sato--{nw}"
    play sound punch
    scene bg play_sayori_bedroom 
    $ s_name = "Satori"
    show sayori turned casual lup rup cry e4e me at i11
    s "I'm about to end this depressed girl's own career..."
    c "--ri?"
    c "Satori!"
    show cara turned bb me at t21
    show sayori oe at t22
    s "Eh?"
    s om "Meizu!"
    show cara at rhide 
    show sayori at rhide 
    hide cara 
    hide sayori 
    "She tackled Satori to prevent her from turning herself off."
    play music t1p 
    c "Stay with me, Satori..."
    c "Stay with me!"
    s "Meizu..."
    s "I'm as useless as that water goddess, Oceania..."
    s "You go to the festival without me..."
    c "I am not letting that happen, Satori."
    s "Jokes on you, I know that hanging myself will fail..."
    s "So for plan B..."
    "Satori took a pill from her pocket and immediately swallowed it."
    c "What the heck, Satori!"
    c "Spit it out!"
    "Satori passed out..."
    c "911... wait, no..."
    c "I need to call an ambulance... but not for me..."
    "Meizu called for an ambulance for Satori."
    "She took her to the hospital."
    scene bg play_hospital
    with wipeleft_scene
    "The doctor told Meizu that she'll be alright and the poison was successfully removed."
    show cara turned lbehind rhold me ea be at t11
    c "..."
    c "Satori, I hope you'll be okay soon."
    "Soon enough, Satozuki, Satori's mom arrived."
    show cara at t21
    show sayozuki 1cg at t22
    $ sz_name = "Satozuki"
    sz "I'm sorry that you saw Satori like that."
    sz 3cb "No worries, I'll go ahead and take care of her."
    c mb "Thanks, Ms. Satozuki."
    sz 1cb "You're very sweet to my daughter, Meizu."
    sz 1ce "I wonder if you'll get to be with her..."
    c me "Ms. Satozuki..."
    "Meizu just sighed and left."
    stop music fadeout 2.0
    scene bg play_residential
    with wipeleft_scene 
    "Meizu is distraught after seeing her best friend try to turn herself off."
    "But that actually is the beginning of her troubles..."
    "Soon after she saw a familiar figure limping..."
    $ n_name = "Natsuchi"
    show natsuki turned cry fs at t22
    show cara turned be me at t21 
    c "Natsuchi... why are you crying?"
    play music t10 
    n om "I..."
    show natsuki at rhide 
    hide natsuki 
    show cara at t11
    c "Natsuchi!"
    show cara at rhide 
    hide cara 
    "Meizu tried to follow Natsuchi."
    "Suddenly, Meizu's phone rang."
    c "Oh, Monique's calling."
    $ m_name = "Monique"
    m "Where the heck are you guys?!"
    m "Me and Yui are having a hard time to handle the crowd here, they're looking for Natsuchi's muffins!"
    c "Sorry, Monique."
    c "There seems to be a bit of a problem..."
    c "Satori is in the hospital..."
    c "And I saw Natsuchi just this instant, she ran away for some reason..."
    c "We might as well gonna be cancelling our part for the festival..."
    m "What?"
    m "We can't do that!"
    c "Well, I'm gonna go try to find Natsuchi..."
    c "Bye."
    m "Meizu!"
    "Sorry, Monique..."
    "Things aren't going to your plan..."
    scene bg play_house 
    with wipeleft_scene
    pause (0.5)
    scene bg play_corridor
    with wipeleft_scene
    pause (0.5)
    stop music fadeout 2.0
    "Well, Meizu couldn't find her anywhere, maybe she went to the club after all?"
    c "I guess I'll have to check there... she may have went here."
    "As Meizu went towards the clubroom, a lot of students passed by her..."
    "She overheard them say that the anime club is just a waste of time..."
    "Hearing that, she rushed towards the clubroom."
    scene bg play_club
    with wipeleft_scene
    play music t3p
    c "Monique..."
    m "Meizu!"
    c "I'm sorry..."
    $ y_name = "Yui"
    y "We understood."
    show cara 1ac at tf31
    show monika 1p at t32 
    show yuri 3w at t33 
    c "We need to find Natsuchi..."
    c "I don't know where she might've been..."
    c "I need your help finding her..."
    m 3i "Right..."
    show cara at lhide 
    show monika at thide 
    show yuri at thide 
    hide cara 
    hide yuri 
    hide monika 
    "All 3 of them tried to look for Natsuchi."
    scene bg play_school_grounds
    with wipeleft_scene
    show cara 1k at t31 
    show monika 1g at t32
    show yuri turned neut at t33 
    m "It's getting late, Meizu and we can't seem to find Natsuchi."
    y om "Maybe she went home already..."
    show yuri cm at t33 
    m "As much as we love to help you, we need to go."
    y om "We'll resume finding her tomorrow if there is still no sign of her."
    show yuri cm at t33 
    m "Call me if you found her, okay?"
    c turned lbehind rhold me ea be "O-okay..."
    show cara at t11 
    show monika at thide 
    hide monika 
    show yuri at thide 
    hide yuri 
    c "Natsuchi..."
    scene bg play_house2
    with wipeleft_scene
    stop music fadeout 2.0
    "Meizu kept looking..."
    "Until she arrived in a house..."
    c "Wait... this is..."
    "Natsuchi's residence."
    "Meizu considered asking her parents to know what's going on."
    "She knocked on the door only to find that it's not locked and opened as soon as she knocked."
    c "Oh?"
    "A lot of knives, pills and syringes are scattered across the floor."
    show cara 3n at t11
    c "Sheesh, this feels ominous..."
    c "Feels like this is an abandoned house..."
    show cara turned lbehind rhold me be at s11 
    c "I really hope Natsuchi's okay..."
    "Meizu went upstairs."
    scene black 
    with wipeleft_scene
    "Meizu don't really have any idea where she is..."
    "But this is worth a shot for her..."
    "She punches the door open."
    play sound punch
    scene bg play_natsuki_bedroom
    "Meizu finds Natsuchi taking some sort of syringe."
    c "Natsuchi!"
    show cara 1ah at t22
    show natsuki turned casual cry at tf21
    "Natsuchi looks at Meizu..."
    play music t1p fadein 2.0
    n om "W-why are you here?!"
    n "G-get out... of my... room."
    show natsuki cm at t21
    play sound "sfx/slap.ogg"
    c 1h "Not until I see you put that away!"
    c "If I have a nickel for everytime I saw someone try to off themselves, I have two nickels."
    c 1e "Which may not be enough, but it's bizarre it happened twice."
    c 1h "So... no."
    n om "Meizu..."
    show cara 1b at t22 
    show natsuki ce at tf11
    n oe om "I'm... sorry! I'm sorry!"
    n sad "I've been living in a nightmare here with my mom {i}every single day{/i}."
    n "She never really treated me properly like a daughter."
    c "..."
    c 1c "You know what, Natsuchi...?"
    c "Wanna come with me?"
    n pout om "Where are we going?"
    c turned lbehind rhold me be "I don't know..."
    c "But... at least I need to get you out of here..."
    c "You can stay at my house at the moment."
    n "I'm scared..."
    n "But I trust you, Meizu."
    n neut om "Let's go, my mom wouldn't even notice that I'm gone until she's gonna need me for something..."
    n "That's how she doesn't care about me."
    show natsuki cm at tf21 
    c "Let's get out of here..."
    show cara at rhide
    show natsuki at rhide 
    hide natsuki 
    hide cara 
    "Meizu and Natsuchi left the house."
    scene bg play_kitchen 
    with wipeleft_scene
    "They arrived at Meizu's house."
    show cara 1c at t22
    c "You're probably hungry at the moment, you go ahead and help yourself in the fridge."
    c "I'm just gonna go change clothes at my room."
    show natsuki turned casual neut om at t21 
    n "... Alright."
    show natsuki at thide
    hide natsuki 
    show cara at rhide 
    hide cara 
    "As Meizu changed her clothes, Natsuchi grabbed something to eat..."
    "After she had her fill, she fell asleep on the table."
    show cara 1bf at r11 
    c "Alright, Natsuchi, time to--"
    c 1bb "Eh?"
    c 1bj "..."
    "Meizu picked up Natsuchi and took her to her bedroom."
    scene bg play_bedroom
    with wipeleft_scene
    stop music fadeout 2.0
    "Meizu put Natsuchi in her bed."
    c "Sweet dreams, Natsuchi."
    c "I will help you in whatever you're facing."
    "Meizu went downstairs and slept on the couch."
    scene black 
    with dissolve_scene_full
    pause (1.5)
    scene bg play_lroom 
    with dissolve_scene_full
    c "..."
    c "!"
    c "It's morning already..."
    c "Natsuchi!"
    "Meizu rushed upstairs."
    scene bg play_bedroom
    with wipeleft_scene
    c "..."
    c "Thank god."
    "Meizu sees Natsuchi still sleeping."
    c "I may need to get back inside her room after all to get her other stuff."
    c "Good thing it's the weekends, there's no classes."
    c "I guess I have to go out and get her stuff."
    scene bg play_house2
    with wipeleft_scene
    c "This is it..."
    c "I hope her mom isn't around."
    "Meizu approached the door."
    "It seems to be left untouched since last night."
    c "Okay, this is good."
    c "I'm not really comfortable breaking in another's house..."
    c "But I did this yesterday already."
    "Meizu went inside once more."
    scene bg play_natsuki_bedroom
    with wipeleft_scene
    "Meizu took everything that Natsuchi needs."
    "Clothes, her school uniform, and... her manga collection."
    "She took it all and ran as fast as she could."
    pause (3.0)
    play sound closet_open
    $ k_name = "Natsuken"
    k "So... that's the person who took my daughter away from me..."
    show ken 3i at t11
    k "I'm afraid I'm gonna have to kill her..."
    scene bg play_bedroom
    with wipeleft_scene
    c "Natsuchi?"
    "Meizu still found Natsuchi sleeping soundly."
    c "Gee, Natsuchi is sure a heavy sleeper."
    show natsuki 1bp at t22 
    n "Who said that?!"
    "Natsuchi immediately got up."
    play music t2p 
    show cara 1bl at tf21 
    c "Natsuchi, you're awake!"
    n turned casual anno om "Why did you wake me up, dummy?"
    show cara 3bl at s21 
    c "I'm sorry if I woke you up..."
    show cara 1bf at t21 
    c "But hey, to be fair, it's almost noon right now."
    n turned casual neut om "Well, you got a point..."
    n rhip "But it's the weekends, there's no classes."
    n cross anno om "No excuse in waking me up like that."
    show natsuki neut cm at t22 
    c 1bc "I'm sorry, ok?"
    c "By the way..."
    c "I went to your house once more and took most of your stuff."
    "Meizu gave her a bag full of her clothes and stuff."
    "Natsuchi smiled upon seeing her manga collection."
    n 4bd "You seem to knew me better than I expected."
    n 4bz "This does put a smile on my face."
    c "Let's go eat breakfast before anything else..."
    n 1bd "Right."
    scene bg play_kitchen
    with wipeleft_scene
    "Meizu and Natsuchi ate a wonderful breakfast."
    c "Natsuchi, we need to plan everything about you."
    show cara 1bc at t21 
    c "Such as school..."
    c "Taking care of yourself..."
    c "And most importantly, how are you going to hide from your mom?"
    show cara 1bb at t21 
    show natsuki turned casual neut om at t22 
    n "I'm not really {i}that{/i} worried about myself..."
    n rhip "I'm more worried about my mom."
    show natsuki cm at t22 
    c 1bc "Let's go over the list first."
    c "School..."
    c "I don't think you can still go to school..."
    c "Your mom can easily find you there and take you."
    n om "I don't think she'd do anything rash against me on public places like the school."
    show natsuki cm at t22
    c "...okay..."
    c "Well, let's go over what's next."
    c "Taking care of yourself."
    n om "I can take care of myself just fine, I've been doing that every single day."
    n worr om "There may be times that I... starve myself tho."
    n happ ce om "But I don't think I'd worry about that now, I'm with you!"
    c 1be "... for the love of Renpy-sama..."
    c 1bh "Are you planning to mooch off of me?!"
    n oe lhip rhip "Just kidding."
    n "Of course I'll help in what I can..."
    n "I'll do some chores around here."
    n "I'll also look for some part time jobs on places that my mom won't suspect that I'm there."
    show natsuki cm ldown rdown at t22 
    c 1bf "Sounds like a plan."
    c 1bc "But... the last on the list..."
    c "As much as I'd love you to stay..."
    c "I can't hide you from your mom here {i}forever{/i}."
    c "She will find out that you're here in any given moment."
    show cara 1bb at t21 
    n neut om "I think this is a stretch but..."
    n "I have a distant relative far from here."
    n "She's been very nice to me when I stayed there for a week when I was little."
    n "I'm pretty sure she'll take me in."
    n "And my mom's afraid of her."
    show natsuki cm at t22
    c 1bc "Well, all you need to do is to get there, right?"
    n om "Yeah, pretty much."
    show natsuki cm at t22 
    c 1bf "Well, I think that takes care of everything on the list!"
    c 2bf "Let's execute that plan and stop this living nightmare of yours!"
    show cara 1ba at t21 
    n om "Meizu?"
    c 1bf "Yes, Natsuchi?"
    show cara 1ba at t21 
    n pout om "I'm worried about you."
    n "Sorry for putting you in this mess."
    n happ om "But thanks for your help nonetheless."
    show natsuki cm at t22 
    c 1bg "You don't have to worry about me."
    stop music fadeout 2.0
    "Meizu's phone rang."
    c 1bc "Oh, hold on a second."
    show cara at lhide 
    hide cara 
    c "Hello?"
    c "Right..."
    c "Okay..."
    c "Okay, I'll be there."
    "Meizu ended the call."
    show cara 1bc at l21 
    c "It's Satori's mom."
    c "She wants me to visit Satori in the hospital."
    c "Well, I guess I better get going."
    c "Are you gonna be okay here?"
    n pout om "Wait..."
    n "Satori's in the hospital?"
    c "It happened the same day you ran away."
    c "Actually, before I found you running away, I found Satori in her bedroom trying to turn herself off."
    n "I'm worried about her..."
    n neut om "I'll come with you."
    c "Are you sure about that?"
    n "I'd be extra careful, Meizu."
    n worr om "I'm worried about Satori."
    c "Alright."
    c "Let's go visit Satori."
    show cara at thide 
    hide cara 
    show natsuki at thide 
    hide natsuki 
    "Meizu and Natsuchi prepared and visited Satori."
    scene bg play_hospital
    with wipeleft_scene
    "We arrived just in time."
    play music t2p
    $ sc_name = "Satochi"
    sc "Oh, hi there!"
    show sayochi turned casual mb at t11
    sc "You must be Meizu."
    c "Yes I am."
    sc "And she is...?"
    c "Oh, she's Natsuchi, a friend of mine and Satori."
    sc lean casual mb "Oh hello there!"
    sc turned casual bd mb "Sorry for requesting this all of a sudden..."
    sc mg "But our younger sister Sato wants to go home now and play with her PS5."
    $ sy_name = "Sato"
    sy "Big Sis Satochi, I wanna go home now..."
    show sayochi at t22 
    show sayo 1bj at t21 
    sy "I have an online match with my not so sigma friends..."
    sy 4bv2 "If I didn't show up, they'll fanum tax my gyatt!"
    sc bb ee "Alright, Sato."
    sc "We're going home now..."
    show sayochi at rhide 
    hide sayochi 
    show sayo at rhide 
    hide sayo 
    "Satochi grabbed Sato's hand and left."
    sc "How many times do I have to tell you, don't speak that way!"
    sy "Big Sis, it's the goated way to speak!"
    stop music fadeout 2.0
    "We looked at Satori lying down in her bed."
    play music t3p
    show cara 1bc at t21
    c "I still couldn't believe that she would do that."
    c turned winter me be "I kept thinking to myself that it's all my fault..."
    show cara turned md at t21 
    "Natsuchi rubs Meizu's back."
    show natsuki turned casual pout om at t22 
    n "I... don't think it's your fault."
    show natsuki cm at t22 
    "Satori starts to wake up."
    s "..."
    s "Meizu?"
    s "And Natsuchi?"
    "Satori tried her best to sit on her bed."
    c "Satori... you shouldn't force yourself."
    s "It's okay, Meizu."
    n worr om "I'm sorry to hear about your situation."
    show natsuki cm at t22 
    s "..."
    s "It's okay."
    s "I'm sorry for making you worry."
    s "You're one of my best friends."
    c me "Satori..."
    c "We're always here for you, whatever you're facing."
    c eg "So please get better!"
    show cara at thide 
    hide cara 
    play sound fall 
    "Meizu gave Satori a gentle hug."
    c "I don't want to lose my childhood friend..."
    s "Meizu..."
    s "I'm sorry..."
    s "I made you worry..."
    show cara turned winter me be at t21 
    n om "Satori..."
    n "You know that I'm not as touchy as Meizu..."
    n "But you're the only best friend I have."
    n "I don't want to lose you too, of course."
    s "Natsuchi..."
    s "..."
    s "Alright."
    s "I'll try my best for the both of you..."
    s "To push myself to be happy."
    s "So that you're happy too."
    s "I love both of you."
    s "I don't want both of you to be sad."
    c 1bl "That's the spirit!"
    show cara 1bw at t21 
    show natsuki happ cm ce at t22 
    "Everyone smiled."
    show natsuki oe at t22 
    c 1bf "Well, anything that you need, Satori?"
    s "I'm kinda hungry..."
    c "Okay, I'll go get something to eat in here."
    s "Hospital food sucks."
    s "Go get me something tasty!"
    c "Alright. I'll see what I can find nearby..."
    c 1bc "Natsuchi, are you gonna be okay here?"
    show cara 1bb at t21 
    n om "Yeah, I'll just read my manga here..."
    s "Natsuchi, I wanna read too..."
    n "Sure, Satori."
    n neut om "But... this hasn't been animated yet..."
    n "Are you sure you want to be spoiled?"
    s "It's fine."
    s "I'll probably miss it anyways since I'm stuck here in this hospital for a couple more weeks."
    n "Ooookay."
    c 1bf "Well, with that taken care of, I'll be off now."
    show cara at lhide 
    hide cara 
    show natsuki at thide 
    hide natsuki 
    "Meizu left the hospital to get something to eat whilst Natsuchi sat beside Satori to read her the manga."
    scene black
    with wipeleft_scene
    stop music fadeout 2.0
    "Everything seems to be going well after that..."
    "And things are looking up for Meizu, Satori, and Natsuchi."
    "Natsuchi even got a part time job to sustain herself... and to help pay Meizu's bills."
    "Until Satori fully recovered and was discharged from the hospital."
    "Satori returned to the club even happier than she was before."
    scene bg play_club
    with wipeleft_scene
    show sayori 4x at lf31
    s "I'm back, guys!"
    show monika forward cry mb at t32 
    m "Satori!"
    m "We're so worried about you."
    play music t1p
    show sayori turned cry ma e4e lup rup at t21 
    play sound fall
    s "I missed you, Monique."
    m "We all missed you, Satori."
    show yuri turned sad mb e1a at t33 
    y "Satori! you're back!"
    show sayori at t31 
    s happ om oe "I missed you too, Yui."
    m 3b "Alright, everyone!"
    m "I think it's the best time to binge watch anime while we eat Natsuchi's muffins!"
    show sayori 4r at h31 
    s "Yay!"
    hide monika 
    hide sayori 
    hide yuri 
    with wipeleft 
    play music t2p 
    "To celebrate Satori's return, Monique and the others decide to just binge watch anime for the rest of club time."
    scene black 
    with wipeleft_scene
    "There's a lot that happened after Satori came back."
    "The anime club has been very productive after the festival..."
    scene bg play_club 
    with wipeleft_scene
    y "Hi, Meizu."
    c "Oh hello, Yui."
    show yuri 4a at t21 
    y "Care to... help me rearrange my anime figures collection?"
    show cara 1y at t22 
    c "Sure!"
    y 3d "Let's go!"
    show cara at thide 
    hide cara 
    show yuri at thide 
    hide yuri 
    "After Meizu helped for a while, Natsuchi walks in."
    n "Meizu!"
    show natsuki 1d at r33
    n "I just bought a new manga to read."
    n "I don't know if this is good, but since you're the manga expert, I'd lke to hear your thoughts."
    show cara 3l at t32 
    c "As much as I would love to... I'd--{w=1.0}{nw}"
    show yuri 1b at t31
    y "You can go ahead."
    y "You've done more than enough help."
    c turned rhold lbehind be me "Are you sure, Yui?"
    y 4d "Of course!"
    y 1b "I'll take care of this."
    c 1f "Alright."
    c "Thank you, Yui."
    show cara at rhide 
    hide cara 
    show natsuki at rhide 
    hide natsuki 
    show yuri 1a at t11 
    "Meizu and Natsuchi went to their usual spot."
    y turned sad "..."
    y "*sigh*..."
    y om "Out of all the times it was turning out good..."
    y ce "Natsuchi swoops in and takes it away from me."
    scene bg play_school_grounds
    with wipeleft_scene
    "As time progresses, Meizu and Natsuchi seems to start to develop something different."
    c "Natsuchi..."
    n "Yes, Meizu?"
    show cara 3l at t21 
    c "I've been thinking lately..."
    n "Thinking of leaving the anime club?"
    show natsuki turned anno om at t22
    n "You can't do that."
    n "How can I know if a manga I'm buying is good or not?"
    show natsuki cm at t22 
    c 3u "No, no, no not like that."
    n neut om "What, are you having some {i}women{/i} issues?"
    n "I have some right here. You need to go to the bathroom?"
    c 1h "No!"
    show cara turned ee be me at s21 
    c "*sigh*..."
    c 3c "I..."
    n 4d "Spit it out, Meizu!"
    c "I like you, Natsuchi."
    show cara 3b at t21
    show natsuki turned shoc md at t22 
    pause (0.5)
    show natsuki e2b at t22 
    pause (0.5)
    show natsuki e2c at t22 
    pause (0.5)
    n pout cm "..."
    n om "Let's talk about that... at home."
    c "..."
    c 3c "Okay."
    show natsuki at rhide 
    hide natsuki 
    "Natsuchi left Meizu sitting there."
    show cara turned ee be me at s21 
    c "*sigh*..."
    c 1c "I hope she's not mad at me."
    show cara at lhide 
    hide cara 
    pause (2.0)
    y "..."
    show yuri turned sad om at t11 
    y "Did I hear that correctly...?"
    y "So Meizu... likes Natsuchi."
    show yuri at lhide 
    hide yuri 
    pause (2.0)
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg play_lroom
    with dissolve_scene_full
    "Meizu sits in her couch until Natsuchi approaches her."
    play music t1p 
    show natsuki turned casual pout at t22 
    n "Meizu..."
    c "Oh, Natsuchi."
    show cara 1bb at t21 
    n om "I..."
    show natsuki cm at t22 
    c 1bc "Is it about what I said earlier?"
    show cara turned winter lbehind rhold me ec be at s21 
    c "You don't have to...{w=1.0} worry about that."
    n om "No, Meizu."
    n "I'm actually surprised."
    n "I just didn't know what to respond to you at the moment..."
    show natsuki cm at t22 
    show cara 1bl at t21 
    c "You don't have to rush yourself."
    show cara 1bb at t21 
    n sad om "No, I think I have to address this now."
    n pout om "I'm very grateful that you told that to me."
    n sad mc "And not just that..."
    n happ om "I'm very grateful that you have been there for me through and through."
    n sad mc "You never left my side, and you're always there for others, not just me."
    n happ om "You even helped Satori overcome her depression."
    n sad mc "And all I'm gonna say is..."
    n happ om "That I'll be happy if you not just {i}like{/i} me..."
    n blus "But {i}love{/i} me."
    n "I love you, Meizu."
    show cara 3bq at t21
    "Meizu was so shocked."
    show cara 3bq at t21 
    c "N-Natsuchi?!"
    c "I..."
    c 3bab "I don't know what to say..."
    n sad mc "Just say I love you too, damnit."
    n "I don't want this to get too cheesy it becomes cringy."
    c 3bl "Oh alright."
    c "I love you too, Natsuchi."
    show natsuki at thide 
    hide natsuki 
    show cara at thide 
    hide cara
    "And thus a wonderful relationship is formed between the two."
    scene black 
    with wipeleft_scene
    "They are so happy with each other."
    scene bg play_club 
    with wipeleft_scene
    show sayori 4r at t31 
    show monika 1j at t32 
    show yuri 3s at t33 
    "When everyone in the anime club knew about their relationship, everyone approved and applauded."
    "Or... is it?"
    scene black
    with wipeleft_scene
    "Things are about to get more interesting..."
    scene bg play_city
    with wipeleft_scene
    play music t4p
    "Meizu and Natsuchi are on a date somewhere in the city."
    "They heard someone down the road."
    $ mi_name = "Mikasa"
    mi "Fortunes! I tell fortunes!"
    n "Meizu?"
    show cara 1bf at t31 
    c "Yeah?"
    show natsuki 1bd at t32 
    n "Wanna try this one out?"
    mi "Hello, lovely couple!"
    show mizumi 1bb at t33 
    mi "Wanna try some of my fortunes?"
    c "Sure, it sounds fun."
    n "How do you tell fortunes anyways?"
    mi 1bg "Well this Time Tr-- erm, Fortune ring that I have can help me predict the future!"
    c 1by "Oh cool!"
    n 1bd "Let's do this!"
    show mizumi 1ba at t33 
    "Meizu and Natsuchi paid the fortune teller."
    mi 1bb "Let's see here..."
    show mizumi 1bn at t33 
    mi "..."
    mi "..."
    mi "..."
    mi 1bm "Oh... both of your futures seems rather... {i}rocky{/i}."
    c 1bc "Rocky?"
    show cara 1bb at t31
    n turned casual neut om "What's that supposed to mean?"
    show natsuki cm at t32 
    mi 1bf "All I'm going to say is that you'd be together... one will fall behind but will catch up later."
    mi "Also... there are two powerful negative energies that are ready to destroy your relationship."
    n om "Two?"
    c 1bc "One has to be your mom..."
    show cara 1bb at t31 
    show natsuki cm at t32 
    mi "You better be careful out there. One of you might succumb to the negative energy, you may fight it but you will fail."
    n happ om "Alright, thanks um..."
    mi 1bb "Mikasa. Nice meeting both of you."
    n "Thanks!"
    show cara at lhide 
    show natsuki at lhide 
    hide cara 
    hide natsuki 
    show mizumi 1ba at t11 
    "They paid and left Mikasa to continue their date."
    show mizumi 1bm at s11
    mi "Oh the terrible, terrible fate of those two..."
    stop music fadeout 2.0
    scene black 
    with dissolve_scene_full
    "Some time passed..."
    scene bg play_lroom
    with dissolve_scene_full
    play music t2p 
    "Natsuchi is out for work today."
    "Meizu is just chilling on her living room, watching anime."
    "Well, there are no classes after all..."
    show cara 1bf at t11
    c "I just finished another episode of '100 Girlfriends'..."
    c "I wonder when Season 2 comes out?"
    c "I'm actually excited about it!"
    show cara 1ba at t11
    "Meizu heard a knock on her door."
    c 1bf "Coming!"
    show cara at lhide 
    hide cara 
    c "Oh, hi Yui..."
    c "It was nice seeing you today..."
    c "Why the sudden visit?"
    y "I just wanted to see you..."
    y "I-I missed you to be honest."
    c "Missed me?"
    c "We saw each other in the club yesterday."
    c "But I guess... thanks?"
    y "Y-yeah..."
    c "Alright, come on in."
    show cara 1bf at t22 
    show yuri 1ba at t21 
    c "Natsuchi is not around so I'm just chilling here..."
    show cara 1ba at t22 
    y 1bf "Oh, so she's not here..."
    y turned casual lup rup happ om e4a "I'm glad that she isn't here..."
    show yuri oe cm at t21 
    c 1bf "Wanna watch some anime with me?"
    y 1bb "I cordially accept."
    show cara at thide 
    hide cara 
    show yuri at thide 
    hide yuri 
    "Meizu and Yui binge watched an anime titled: 'Spy Family Z'."
    "As they we're watching... Meizu is starting to notice that Yui is getting {i}too{/i} close to her."
    c "Y-Yui?"
    c "I c-couldn't concentrate on the show."
    y "Watching this anime soothes me..."
    y "I feeling like I would be Yin Fordheart."
    c "Why do you say so?"
    y "Because... If ever I love someone, and someone is gonna take me away from him/her, I'd go all in and fight for it."
    c "Interesting take..."
    c "Have you ever found someone to love and fight for, Yui?"
    y "Well... {i}yeah...{/i}"
    y "But I'm fighting a losing battle, Meizu."
    stop music fadeout 2.0 
    "They both stood up."
    show cara 1bc at t22
    show yuri turned casual sad at t21 
    c "Oh, come on, you shouldn't give up..."
    y 1bu "I..."
    c 1bf "Tell me who's this person, and I'll fully support you."
    y turned casual sad om "Are... you sure?"
    c 2by "Of course!"
    show cara 1by at t22 
    y turned casual shy e1 om "Well..."
    y bful "It's...{w=1.5} {i}you{/i}..."
    play music t10y
    show cara 3br at s22 
    c "... huh?"
    y e1 om nobl "Yes... it's you..."
    y turned rup lup sad ce om "I've been holding on to this for a very long time."
    y oe "I... liked you ever since."
    show cara 3bp at t22 
    "Meizu doesn't even know how to act..."
    y ldown rdown angr om "Now, since you said you'll support me..."
    y "I'll go ahead and do it as you said."
    y "Love me instead, Meizu."
    y "Who cares about that obnoxious brat?"
    y ce "Her job is probably getting coins under a vending machine."
    y oe "And for the record, I was the first person that did have feelings for you."
    c 3bq "Yui... stop."
    show cara turned winter lbehind rhold ee md at t22 
    y vang mc "Why would I...?"
    y yand om "You said you'd support me..."
    c 3br "This isn't it!"
    c "I don't want to destroy my relationship with Natsuchi!"
    y mg "Natsuchi, Natsuchi..."
    y vang om "It's all about her, right?"
    "Meizu just doesn't have the words to say."
    y happ om "Just come here..."
    show yuri cm at t11
    show cara 1bs at t22 
    "She took Meizu's hand..."
    show natsuki 1bd at l31 
    show yuri at t32 
    show cara at t22
    n "Meizu! I'm home I..."
    n turned casual shoc "..."
    show natsuki turned vang casual om lhip rhip at h31 
    n "What the heck is the meaning of this?!"
    show yuri at t32
    y e2a mc "Natsuchi! There you are!"
    c 1bq "I can explain..."
    y "She's starting a new relationship with me, that's what."
    y angr mb "And she even said that she'd {i}fully{/i} support me."
    c 1bh "Hey, that's not-- {nw}"
    y om "Shut it!"
    c "Are you seriously just gonna believe her?!"
    n cry "..."
    show natsuki at rhide 
    hide natsuki 
    "Natsuchi ran to the bedroom."
    c 1be "Alright, that's it."
    c 1bah "WHAT THE HECK ARE YOU EVEN THINKING?"
    c 1be "Yui, get out of my house."
    y neut om "W-why-- {nw}"
    $ style.say_dialogue = style.edited
    show yuri vsur ml lup rup at h32 
    c 1bah "GET THE FUCK OUT OF MY HOUSE!"
    $ style.say_dialogue = style.normal
    show yuri at lhide 
    hide yuri 
    show cara at t11
    "Yui ran away."
    show cara turned winter be ee me lbehind rhold at s11 
    c "*sigh*..."
    c "Natsuchi..."
    stop music fadeout 2.0
    scene black 
    with wipeleft_scene
    "Meizu immediately went to Natsuchi."
    "She locked the door."
    c "Natsuchi?"
    n "..."
    n "Go away!"
    c "I can explain..."
    n "I'm tired, I don't want to hear anything from you!"
    c "..."
    c "Are you going to believe her, more than me?"
    n "What I saw is believable enough."
    c "And are you seriously gonna jump to conclusions?!"
    n "Go away!"
    n "I don't want to hear anything from you..."
    c "..."
    c "Fine..."
    c "You win."
    c "If you need to talk it out... I'll be downstairs."
    "Meizu walked away the door as a sign of defeat."
    scene black 
    with dissolve_scene_full
    "While they we're sleeping..."
    c "..."
    c "Ack... can't breath..."
    "Meizu felt something soft is suffocating her."
    "Luckily, she managed to kick something..."
    play sound punch 
    k "{i}*grunts in pain*{/i}"
    "Meizu managed to broke free and immediately turned on the lights."
    scene bg play_lroom
    with wipeleft_scene
    show cara 1bah at t22 
    c "WHO ARE YOU?!"
    show ken 2i at t21 
    play music battle 
    k "I'm here to take my daughter back..."
    c 1bc "Wait..."
    c 1br "You're Natsuchi's mother?!"
    k "I'm here to take my daughter back and kill you for good."
    c 1bh "I... won't let that."
    k 1i "I'd like to see you try..."
    show ken at rhide 
    hide ken 
    show cara at rhide 
    hide cara 
    play sound punch
    pause (0.5)
    play sound punch
    pause (0.5)
    play sound punch 
    show cara 1br at r41
    pause (0.25)
    show cara at lhide 
    hide cara 
    show ken 1a at r41
    pause (0.25)
    show ken at lhide 
    hide ken 
    play sound punch
    pause (0.5)
    play sound punch
    pause (0.5)
    play sound punch 
    c "Owww!"
    "Even with Meizu's martial arts knowledge, she was knocked out by Natsuchi's mother."
    show ken 1i at l11
    k "You're quite tough."
    k "I liked that you're able to fight back."
    k "I'll let you live because of it, but I'll take my daughter now."
    c "... I...{w=2.0} won't"
    show black
    with dissolve_cg 
    c "Let...{w=2.0} you..."
    "Meizu passed out."
    stop music fadeout 2.0
    scene black 
    with dissolve_scene_full
    pause (1.0)
    scene bg play_lroom
    with dissolve_scene_full
    "Meizu woke up."
    c "Natsuchi!"
    "Meizu ran up to the bedroom."
    scene bg play_bedroom
    with wipeleft_scene 
    "And sure enough, she's not there..."
    "All of her stuff was taken away as well."
    c "I'm taking her back..."
    "She wasted no time."
    scene bg play_house2
    with wipeleft_scene
    "Meizu's back to this house."
    c "..."
    c "Here I go."
    scene black 
    with wipeleft_scene 
    "The house again, is empty."
    "No one is there."
    "Meizu went straight to her bedroom..."
    "She gently opens the door this time."
    c "...Natsu--{nw}"
    window hide(None)
    window auto
    play music td
    scene bg play_natsuki_bedroom
    show n_kill zorder 4 at face:
        xpos 640
        ypos 200
        zoom 0.75
    pause (3.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause (2.0)
    hide screen tear
    c "..."
    c "Natsuchi..."
    $ style.say_dialogue = style.edited
    c "NATSUCHI!!!"
    $ style.say_dialogue = style.normal
    scene black
    with dissolve_cg
    "Meizu took her hanging body down and laid it on the bed."
    c "Why, why did you leave me?"
    "Meizu ran outside."
    scene bg play_residential
    with wipeleft_scene
    show cara 1bac at t21 
    c "I don't know what to do now..."
    $ kt_name = "Katie"
    show kotonoha toward casual om at r22
    show cara 1bad at t21 
    kt "Are you ok?"
    c 1bac "I lost someone near and dear to me."
    c "She is dead now."
    show cara 1bad at t21 
    kt sad om "That's sad."
    kt "I don't know what to tell you..."
    kt neut om "Oh hey, I heard someone can {i}revive{/i}-- {nw}"
    c 1bac "You knew someone who can {i}revive{/i}?"
    c "Show me where this person lives!"
    kt "Oh... okay I'll show you..."
    kt "I actually need to go there since my dog died..."
    "She showed Meizu a small box with a dead dog inside."
    scene bg play_city 
    with wipeleft_scene
    kt "Here we are..."
    kt "All we need is to go inside this house..."
    scene bg play_lroom
    with wipeleft_scene
    "Both of them entered the house."
    $ a_name = "Amethyst"
    a "Hello, guys."
    show amy turned casual happ om at t33 
    a "Amethyst-sama, at your service."
    show cara 1bad at t31 
    show kotonoha toward casual sad e1a mb at t32 
    kt "Oh, Amethyst-sama, please revive my dead dog..."
    kt "She's the only thing in the world that mattered to me."
    a lspecs "Oh sure... this shouldn't be an issue."
    show amy ldown neut ce cm at t33 
    a "..."
    $ style.say_dialogue = style.edited
    show amy b1e oe om at t33
    a "Secret Dark Arts Spell: - Resurrection!"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    $ style.say_dialogue = style.normal
    show amy brow cm at t33 
    "A bright light enveloped the room."
    "Soon after, the dog opened its eyes and moved."
    kt happ om "Thank you, Amethyst-sama!"
    show kotonoha at lhide 
    hide kotonoha
    "Kotonoha paid her and left."
    a happ om "Anything I can help you with?"
    show amy cm at t22
    show cara at t21 
    c 1bac "Oh Amethyst-sama."
    c "I have a friend that just died today..."
    c "Are you able to revive her?"
    show cara 1bad at t21
    a om "Oh... sure!"
    a lspecs "Where is your animal friend?"
    c 1bac "Oh, she's a {i}human{/i} person."
    show cara 1bad at t21 
    a neut om ldown "Oh..."
    show amy turned casual nerv mc e1a at s22 
    a "Well, sorry for assuming."
    show amy turned happ om at t22
    a "But... since she's a person..."
    a pout om "I'm sorry, I can't do revival spells on humans at this point."
    a "I need a full moon in order to do that."
    a "And since the full moon is still in two weeks..."
    a "And I can only revive dead beings within 3 days after they died..."
    a cm "Then, I'm sorry, I couldn't help you."
    c 1bac "Nooo..."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "After a few weeks after Natsuchi's death..."
    scene bg play_bedroom
    with dissolve_scene_full
    c "..."
    "Meizu has lost interest in everything."
    "She quit the anime club, even school in general."
    "She's just an empty shell of her former self."
    "And just now, something snapped into her head."
    c "Today... is the day."
    "She wrote a note and then put it on her door."
    $ show_poem(poem_play, paper_sound=audio.page_turn, music=False, from_current=False, revert_music=False)
    c "I'm not gonna waste time anymore."
    scene bg play_road
    with wipeleft_scene
    c "..."
    show cara turned winter be me at tf21 
    c "..."
    c "Soon we'll be together, Natsuchi."
    s "Stop!"
    show sayori turned casual cry at t22 
    c eg mb "Oh how the tables have turned..."
    c "I still remember how I stopped you from turning yourself off."
    s lup rup b1e om "That's why I'm here to stop you from doing so!"
    show sayori cm at t22 
    c me "Why..?"
    c "Natsuchi is gone..."
    show cara md at tf21 
    s vang om e1h "So what if she's gone?!"
    s "Is this what Natsuchi would've wanted for you?!"
    show sayori turned casual brow cry cm at t22
    c eh "Yeah... you're right."
    s "So let's stop this then and come home with me..."
    show cara ma rhold lbehind at t11
    play sound fall
    c mb "You'll always be my dearest friend..."
    c eg "Please don't end up becoming like me."
    show cara at rhide 
    hide cara 
    play sound fall
    show sayori om at h22 
    s "Meizu!!!"
    scene black 
    with dissolve_cg
    s "Meizu!!"
    s "{b}MEIZUUUUUUUUU!{/b}"
    scene black with dissolve_scene_full
    pause (2.0)
    scene bg stage 
    with dissolve_scene_full
    play music t4p 
    "Everyone were astounded by the performance of my girlfriends."
    pr "What an astounding performance from the Literature Club!"
    pr "Let's give them a round of applause!"
    "Everyone clapped and cheered."
    "Well the rest of the school event is rather standard."
    "I enjoyed it all throughout."
    "Until it's time to go home..."
    scene bg bedroom
    with wipeleft_scene 
    "Well, my girlfriends are tired, so I let them go home their separate ways."
    "And so am I basically..."
    "Let's get the sleep going..."
    stop music fadeout 2.0
    scene black 
    with dissolve_scene_full

    return