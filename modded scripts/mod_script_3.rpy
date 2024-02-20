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

    scene bg house
    with wipeleft_scene
    
    mc "WWWWWWWWWW--"

    scene bg club_day
    with wipeleft_scene

    mc "WWWWWWWWW--"

    scene bg residential_day
    with wipeleft_scene

    mc "WWWWWWWCH!"
    "That was one heck of a punch."
    "A punch that even Captain Eagle would be proud of."
    "I think I flew over multiple background sceneries there."
    "I even thought I was in the clubroom for a moment."
    "I get up from the ground."
    show natsuki 4p at t21
    n "{b}That's what you get you p--{/b}"
    n 1m "[player]?"
    show sayori 4m at t22
    s "[player], are you okay?"
    mc "Y-yeah..."
    show sayori 4m at thide
    hide sayori
    show natsuki 4p at t11
    "I simply shook off the dust on me."
    show natsuki 1v at h11
    n "...W-why would y-you do that to m-me? You dummy! dummy! dummy!"
    mc "Why not? I think it's cute."
    n 4o "Khhhh!"
    n 4w "Next time... don't do it again to girls..."
    n 42c "...Unless you really like them..."
    n "You dummy."
    mc "Ah, sorry about that..."
    mc "But I like you though, Natsuki."
    show natsuki 1p at h11
    "Natsuki got all flustered when I said that."
    n 1w "You really are a BIG DUMMY."
    show natsuki 1w at f11
    n "A capital {b}B-I-G D-U-M-M-Y!{/b}"
    n 4p "Get it?"
    mc "Okay, okay..."
    show natsuki 1w at t11
    "This girl is just too cute and adorable..."
    "I invited her to come join me and Sayori to walk to school."
    mc "I was just wondering if all 3 of us want to walk to school together!"
    show natsuki 1k at f11
    n "Walk with you, [player]?"
    n 1y "Well, if you really want me to walk with you badly, then I wouldn't mind!"
    show natsuki 1y at t11
    n "It's not like I took this route so that maybe I could walk with you or anything anyways!"
    "I laughed."
    show natsuki 4o at f11
    n "Why are you laughing? You want another punch?"
    mc "No, no, it's just you're too adorable and cute!"
    show natsuki 1v at h11 
    n "I'm.{w} Not.{w} Cute!"
    "I stopped laughing."
    mc "Okay, okay. Anyways, come, we will be late for school."
    "And so the three of us walked to school together."
    
    scene bg class_day
    with wipeleft_scene

    "We went to our respective classes."
    "I can't wait to see my girlfriends again!"
    "I wonder..."
    "I should spend time with Natsuki today."
    "She seems to be fun to hang out with."
    "Given she is the epitome of a cute tsundere girl."
    "And she seems to be interested in manga."
    "..."
    "And with that thought in mind, the classes we're over before I know it."

    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene

    play music t3

    show monika 5 zorder 2 at t11

    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika zorder 1 at thide
    hide monika
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show yuri 1a zorder 2 at t32
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    show natsuki 4e zorder 2 at t33
    n "Oh, come on! Like he deserves any slack."
    n "Sayori told me you didn't even want to join any clubs this year."
    n "And last year, too!"
    n 4c "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    n 4y "But it's not like I care if you want to be with us here or anything!"
    show monika 2b at l41
    m "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika at lhide
    hide monika
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show yuri zorder 2 at t22
    show sayori 2x zorder 3 at f21
    s "Don't worry, guys~"
    s "[player] always gives it his best as long as he's having fun."
    s "He helps me with busywork without me even asking."
    s "Like cooking, cleaning my room..."
    show sayori 2a zorder 2 at t21
    show yuri zorder 3 at f22
    y 2m "How dependable..."
    show yuri zorder 2 at t22
    mc "Sayori, that's because your room is so messy it's distracting."
    mc "And you almost set your house on fire once."
    show sayori at s21
    s 5 "Is that so... Ehehe..."
    show yuri zorder 3 at f22
    y 1s "You two are really good friends, aren't you?"
    y "I might be a little jealous..."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 1 "How come? You and [player] can become good friends too!"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 4b "U-Um..."
    show yuri zorder 2 at t22
    mc "Sayori's right, Yuri. We can be good friends!"
    mc "I'd love you to reach out to me."
    show sayori zorder 3 at f21
    s 4x "Oh, oh! Yuri even brought you something today, you know~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 3n "W-Wait! Sayori..."
    show yuri zorder 2 at t22
    mc "Really, Yuri? You brought something for me?"
    mc "How thoughtful of you."
    show yuri zorder 3 at f22
    y 3o "Um... Not really..."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 4r "Don't be shy~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y "It's really nothing..."
    show yuri zorder 2 at t22
    mc "What is it?"
    show yuri zorder 3 at f22
    y 4c "N-Never mind!"
    y "Sayori made it sound like a big deal when it's really not..."
    y "Uuuuh, what do I do..."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 1g "Eh? I'm sorry, Yuri, I wasn't thinking..."
    show sayori zorder 1 at thide
    hide sayori
    show yuri zorder 2 at t11
    "I guess that means it's up to me to rescue this situation..."
    mc "Hey, don't worry about it."
    mc "First of all, I wasn't expecting anything in the first place."
    mc "So any nice gesture from you is a pleasant surprise."
    mc "It'll make me happy no matter what."
    y 3v "I-Is that so..."
    mc "Yeah. I won't make it a big deal if you don't want it to be."
    y "Alright..."
    y 1a "Well, here."
    "Yuri reaches into her bag and pulls out a book."
    y "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show yuri at sink
    y 4b "Discuss it...if you wanted..."
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    "She even picked out a book she thinks I'll like, despite me not reading much..."
    mc "Yuri, thank you! I'll definitely read this!"
    "I enthusiastically take the book."
    show yuri 2m zorder 2 at t11
    y "Phew..."
    y 2a "Well, you can read it at your own pace."
    y "I look forward to hearing what you think."
    show yuri zorder 1 at thide
    hide yuri

    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sayori and Monika are having a cheery conversation in the corner."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Natsuki is rummaging around in the closet."
    "Seeing Natsuki is kind of worried about something, I approached her."
    
    stop music fadeout 2.0
    scene bg closet
    with wipeleft_scene

    play music t6

    mc "You looking for something in there?"
    "I asked, seeing how she looks freaked out."
    show natsuki 4s at t11
    n 4x "Freaking Monika... mmmmmmmmmmmmmmmmmmmmmmmmmmmm!..."
    n "She never puts my stuff back in the right spot!"
    n "What's the point in keeping your collection organized if someone else is just gonna mess it up?"
    "Natsuki slides a bunch of stacked books and boxes across the shelf."
    mc "Manga..."
    n 2c "You read manga, right?"
    mc "Ah--"
    mc "...yeah, I do."
    mc "I actaully started reading manga when their anime adaptations from TV left me on a cliffhanger."
    "Manga is one of those things where you can't admit you're really into it until you figure out where the other person stands."
    mc "...How did you know, anyway?"
    n 2k "I heard you bring it up at some point."
    n "Besides, it's kind of written on your face."
    "What's that supposed to mean...?"
    mc "I-I see..."
    "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
    "Curious, I pull it out of the stack."
    n 1b "{i}There{/i} it is!"
    "Natsuki snatches it out of my hand."
    "She then turns to a box of manga and slips the volume right into the middle of the rest."
    n 4d "Aah, much better!"
    n "Seeing a box set with one book missing is probably the most irritating sight in the world."
    mc "I know that feel..."
    "I get a closer look at the box set she's admiring."
    mc "Parfait Girls...?"
    "It's a series I've never heard of in my life."
    "I actually do not read any manga counterparts until I watched its anime first."
    n "Is there a problem, [player]?"
    mc "No, not at all..."
    mc "I haven't heard of the anime series... so I don't know that."
    mc "I'm just curious, that's all."
    show natsuki 4z at f11
    n "You're not just a big dummy then, you're a dork as well."
    n "I could probably imagine you to be like that one NEET manga character that I read once that died through shock..."
    n "And peed on his pants in the process..."
    "She giggles uncontrollably."
    mc "Hey! I'm not {i}that{/i} bad, Natsuki."
    mc "I may consider myself a NEET, but not that extent."
    mc "Although it would be fun to be reincarnated like him to a wonderful world."
    mc "And meet you there, who would likely be the person who casts explosions all the time."
    n 1u "..."
    show natsuki 1d at f11
    n "Well, if I met you there, I would always cast the explosion on you, not on some random castle that has a Demon Lord in it."
    n "But anyways..."
    show natsuki 1y at t11
    n "Not all manga are boring if they have no anime counterpart."
    n 4y "If an anime has been released it means that it's manga counterpart is popular as well!"
    n "That's why they decide to animate it in the first place!"
    n "And FYI, [player], Parfait Girls is releasing its first anime episode this coming Saturday!"
    n "So a word from yours truly:"
    n 4l "Consider this a lesson straight from the Literature Club: Don't judge a book by its cover!"
    n "In fact--"
    "Natsuki pulls out the first volume of Parfait Girls from the box."
    n "I'm gonna show you exactly why!"
    "She shoves the book right into my hands."
    mc "Ah..."
    "I stare at the cover."
    "It features four girls in colorful attire striking animated feminine poses."
    "It's...exceedingly \"moe\"."
    n 4b "Don't just stand there!"
    mc "Uwa--"
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki grabs my arm and pulls me out of the closet."
    "She then takes a seat against the wall, beneath the windowsills."
    "She pats on the ground next to her, signaling me to sit there."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "Wouldn't chairs be more comfortable...?"
    "I take my seat."
    n 2k "Chairs wouldn't work."
    n "We can't read at the same time like that."
    mc "Eh? Why's that?"
    n 2o "Do you realy wanna make me say it?!"
    mc "Ah...I guess it's easier to be close together like this..."
    n 2o "--!"
    n 5r "D-Don't just say that!"
    n "You'll make me feel weird about it!"
    mc "Sorry..."
    "Natsuki scootches an inch closer to me."
    n 42c "But It's not like I'm enjoying it or anything!"
    show natsuki 5g
    "I didn't exactly expect to be sitting this close to her, either..."
    "Not that I can say it's a particularly bad thing."
    "I open the book."
    "It's only a few seconds before Natsuki once again inches closer, reclaiming the additional space while she hopes I won't notice."
    "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    n 1k "Wow, how long has it been since I read the beginning...?"
    mc "Hm?"
    mc "You don't go back and flip through the older volumes every now and then?"
    n 2k "Not really."
    n "Maybe sometimes after I've already finished the series."
    n 2c "Hey, are you paying attention?"
    mc "Uh..."
    "I am, but nothing's really happened yet, so I can talk at the same time."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    "I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    mc "So..."
    mc "What should I expect from this?"
    mc "Is there going to be plot?"
    n 4w "Well, obviously!"
    n "You think I would enjoy something that didn't have a plot?"
    n 4c "I mean..."
    n 2c "Well, I guess I know what you're saying..."
    n 2k "A lot of the beginning is about simple things..."
    n "Like there's a really funny chapter where they're obsessed with a guy at the ice cream shop..."
    n 2c "But that just helps you get to know the characters!"
    n "And besides, it's still entertaining."
    n 2d "But later on, there's all kinds of drama..."
    n "Like when they get into all their backstories, and when some of the romance starts to happen..."
    n "That's really what makes it so good."
    n 2a "There are so many touching parts."
    mc "Ah, is that so?"
    mc "It sounds like you really know what you're talking about."
    mc "Maybe I underestimated you."
    n 2z "Ehehe."
    n 1f "...Hey, wait!"
    n "What's {i}that{/i} supposed to mean?!"
    mc "Uwa--"
    "Natsuki gives me a little shove."
    mc "I just meant that I haven't yet seen you at your full power..."
    n 5s "Hmph. Good save."
    mc "Ah... This chapter seems like it's about baking."
    mc "This is just a guess, but is there a lot of baking in this manga?"
    n 5b "Well--"
    "Natsuki pauses for a moment, as if she doesn't want to admit something."
    n 2q "...Yeah."
    n "Why does that matter?"
    mc "It doesn't, I was just curious..."
    mc "Since you enjoy baking too, right?"
    n 1o "That's--"
    n "Just a coincidence!"
    n 1t "I just happened to get into baking around the same time I got this manga."
    n "Like I would ever get into anything because it's in a manga."
    n 4y "I feel bad for anyone that impressionable."
    n "Ahaha!"
    "Definitely not a coincidence..."
    "I guess that explains Natsuki's interest in baking."
    "Still, of all the hobbies to pick up from a manga, that's definitely one of the better ones."
    "Not to mention she's really good at it, so who am I to judge?"
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    "..."
    "We read on for a few more minutes."
    "I've finished a couple chapters at this point."
    mc "..."
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even though you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "Don't you share your manga with your friends?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    mc "Ah... Sorry..."
    n "Hmph."
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part??{/i}"
    n "I mean, I feel like I can't even keep it in my own room..."
    n "I don't even know what my dad would do if he found this."
    n "At least it's safe here in the clubroom."
    show n_cg1_exp3 at cgfade
    n "'Cept Monika was kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well, it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...So?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    "Suddenly, Natsuki starts laughing."
    hide n_cg1_exp3
    show n_cg1_exp1 at cgfade
    n "Ahahaha!"
    n "I totally forgot that happens!"
    "Natsuki puts her finger on one of the panels."
    n "Minori is my favorite character."
    n "You always feel a little bad for her, since she's so unlucky."
    n "But it gets especially bad when--"
    hide n_cg1_exp1
    n "Uu..."
    n "I shouldn't be talking about that yet!"
    n "Just finish this chapter!"
    scene bg club_day
    with dissolve_cg
    "Natsuki's voice sparkles with excitement."
    "It's a stark contrast to her usual bossy tone."
    "But if she's not used to sharing her favorite manga with her friends, I can understand why."
    "It's hard to express in words the feeling you get when connecting with someone like that."
    "And being able to provide that to Natsuki, for whom it's a rare experience..."
    "The thought makes me smile a little to myself."
    show monika 4b zorder 3 at f21
    m "Okay, everyone!"
    mc "Eh?"
    m "Are you all ready with today's poems?"
    mc "..."
    show monika zorder 2 at t21
    show natsuki 4w zorder 3 at f22
    n "Oh, come on!"
    n "Could your timing be any worse?"
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 5 "Sorry~!"
    m "I just need to make sure we have enough time."
    m "Though you do look pretty cozy over there. Ahaha!"
    show monika zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "Eh...?"
    n 1p "A-Ah!"
    "Natsuki suddenly notices how close she's gotten to me."
    "She hastily slides herself a good twelve inches away from me."
    show monika zorder 1 at thide
    show natsuki 1s zorder 2 at t11
    hide monika
    mc "Alright..."
    mc "Guess I'll stop here for now."
    "I close the book and hand it towards Natsuki."
    n 2m "You're just giving it back...?"
    n "Don't you want to know what happens?"
    mc "Ah... Yeah, but..."
    mc "Monika just said--"
    n 2u "Don't be dumb."
    n "Just take it home with you."
    mc "Eh?"
    mc "...Is that really alright?"
    "I say that mostly because I really didn't plan on using my spare time to read this..."
    n 4h "Well, of course."
    n "It would take forever to finish if you didn't take it home."
    n "Just finish that one before tomorrow, so we can start the next one."
    n 4g "And if it gets bent, I'll kill you."
    mc "By tomorrow...?"
    show natsuki zorder 1 at thide
    hide natsuki
    "I only got partway through the volume so far."
    "I might fall behind on some shows if I try to get through this..."
    "But I suppose that's a necessary sacrifice in exchange for seeing Natsuki's enthusiastic face."
    "Or am I more scared of what will happen if I {i}don't{/i} finish it...?"
    mc "Alright, then!"
    "I stand up."
    "I return to where I put my stuff and carefully slip the book into my bag."

    return
