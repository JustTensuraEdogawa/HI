label mod_script_4:

    scene black

    play music m1

    r "Hi, [player]."
    mc "Hi, Renpy-sama."
    r "You did well with Natsuki."
    r "You broke her out of her tsundere shell."
    mc "Thanks to you, and to Aijou Rensho, I wouldn't have done it."
    r "Nice."
    r "I won't be here for long."
    r "Keep up the good work, [player]."
    r "The upcoming days and events will be more challenging."
    r "Hopefully you're up to it."
    mc "Yes, Renpy-sama."
    "Out of whim, I asked him a question."
    mc "What you're up to?"
    r "Well I'm play--"
    r "--Erm... I'm actually working on a game called: {i}'Monique After Story'{/i}"
    r "I have to boot up the game now or there will be consequences for me."
    "I laughed."
    mc "I thought I was the only NEET."
    r "I-It's for training purposes, ok?"
    r "I need to make sure that the visual novel simulation will run without breaking the character there and the game."
    mc "Whatever makes you sleep at night, bro."
    r "That's Renpy-sama to you!"
    r "Anyways, time to wake up!"
    mc "Ok. Bye Renpy-sama!"

    stop music

    scene bg bedroom

    "BZZT. BZZT. BZZT."
    "Morning, world."
    "I'm excited again for another day!"
    "Time to meet up with my girlfriends."
    "I showered on my bathroom and prepared myself."

    scene kitchen
    with wipeleft_scene

    play music t2

    "I went downstairs to the kitchen to prepare my breakfast."
    "But... as I went down there, I smelled something nice."
    "Something {i}mouth-watering.{/i}"
    "I went and looked, and saw Sayori and Natsuki there."
    "Natsuki is cooking and Sayori is sitting down on the dinner table."
    "I approached them."
    mc "Ohayou, Sayori!"
    show sayori 1a at t21
    s "Morning, [player]."
    show sayori 4a
    "I gave Sayori a hug."
    mc "Morning, Natsuki."
    "I gave her a hug from behind."
    show natsuki 1v at t22
    n "Eyaaah!"
    "She almost dropped the spatula she's holding."
    n "What are y-you doing you pervert?!"
    n "Can't you see I'm cooking here?!"
    mc "Sorry about that."
    show sayori 4a at thide
    show natsuki 1v at thide
    hide sayori
    hide natsuki
    "And with that, I sat on the dinner table."
    mc "Sayori, how did both of you get in by the way?"
    show sayori 1a at t11
    s "I knew you still leave a spare key under your mat."
    s "You always leave a spare key in case you forgot your key when going out."
    s "I'm shocked you don't remember."
    show sayori 1a at thide
    hide sayori
    "I'm so happy right now."
    "My girlfriends are here for me, and one of them is preparing my breakfast!"
    "I approached Natsuki again."
    mc "What are you making?"
    show natsuki 1y at t11
    n "Why, I'm making breakfast, dummy!"
    n "Isn't it obvious?"
    mc "I mean, what breakfast?"
    show natsuki 1a at f11
    n "I'm making bacon and eggs."
    n "I already finished the eggs."
    mc "Thank you."
    mc "You're really sweet, you know that?"
    show natsuki 1a at t11
    "Natsuki starts to get flustered again."
    n 1o "Khhhh!"
    mc "You'll be a decent wife when you get married."
    show natsuki 1p at h11
    n "What you're saying?"
    n "You want to get smacked in the head?"
    mc "No, no. Anyways thank you Natsuki."
    "As I sat back down to the dinner table, I heard her mutter."
    n 1u "I don't mind getting married, as long as it's you."
    n "It's not like I wanted to be your wife or anything..."
    show natsuki 1u at thide
    hide natsuki
    "As Sayori and I am waiting for our breakfast, I heard a knock on the front door."
    s "I'll get it."
    "And with that, Sayori went to the door."
    "And went back with an unexpected visitor."
    show sayori 1a at l22
    show yuri 1a at l21
    y "Morning, [player]."
    mc "Yuri? Morning!"
    mc "What makes you visit me here?"
    show yuri 4a at f21
    y "Erm... I..."
    y "I was just wondering... if we could walk together to school."
    show yuri 4a at t21
    "Hearing that from her makes me happy."
    "She's cute."
    mc "Of course!"
    mc "I'd love to walk with you to school!"
    show sayori 4r at h22
    s "Yay! more people to walk with!"
    mc "And hey Yuri, you could also join us here. Come sit down."
    "I prepared a seat for Yuri to sit on."
    y 3b "I'd love to."
    y "I cordially accept."
    "She sat down on the dinner table."
    show sayori 4r at thide
    show yuri 3b at thide
    hide sayori
    hide yuri
    "We finished our wonderful time of breakfast."
    "And we decided to hit the road so that we won't be late."
    "I quickly packed all that I need before leaving the house."

    scene bg residential_day
    with wipeleft_scene

    "As we walk down the road, Yuri asked me something."
    show yuri 1b at t11
    y "Have you read the book yet?"
    mc "Umm..."
    "Bruh."
    "I haven't read the book yet!"
    "...make an excuse, make an excuse..."
    "Hope this works."
    mc "Actually... I've been thinking to start reading it with you so that you can discuss it with me."
    mc "You said it yesterday, right?"
    show yuri 1n at s11
    y "Umm..."
    "She started to fluster."
    y 4b "Y-yeah... I did s-say that."
    show yuri 1d at t11
    y "Sure! I'd love to discuss it with you!"
    show yuri 1d at thide
    hide yuri
    "And we continued our journey."
    "We are still miles ahead of our journey."
    
    menu:
        "It's time to have some fun!"
        "Grab Natsuki's hand.":
            n "Eyaaah!"
            show natsuki 1v at t11
            n "You wanted to get punched again?!"
            mc "No, no, I just wanted to see your reaction."
            mc "And besides, I also wanted to thank you for making us breakfast."
            show natsuki 1e at f11
            n "Y-you don't have to startle me to thank me!"
            show natsuki 1i at t11
            n "...Just... let me know next time."
            n "I wouldn't mind holding your hand."
            n "It's not like I love holding your gross hand or anything."
            mc "Okay, Natsuki."
            mc "I love you."
            n 42c "I... l-l-love you too, [player]."
            show natsuki 42c at thide
            hide natsuki
        "Ruffle Sayori's hair.":
            "I decided to walk behind Sayori."
            "I ruffled her hair."
            show sayori 4p at t11
            s "[player]!"
            s 5c "You're a real meanie, you know that?"
            mc "Hahaha..."
            mc "Sorry, sorry."
            mc "I just wanted to see how my girlfriend is doing."
            show sayori 2a at t11
            s "Well, thank you for asking."
            show sayori 4r at h11
            s "I am perfectly fine!"
            s "As long as I am with you, I'll be perfectly fine, [player]."
            mc "That's great to hear."
            s "I love you."
            mc "I love you too, Sayori."
            show sayori 4r at thide
            hide sayori

    scene bg class_day
    with wipeleft_scene

    "And we arrived at the school before we know it."
    "Here I am in class, waiting for it to be over soon."
    "It's kinda dull and boring to sit here."
    "And I have my girlfriends waiting in the club."
    "Speaking of the club..."
    "I think I should spend time with Yuri today."
    "Given that she gave me a book yesterday and I didn't even touch it yesterday, I should be ashamed of myself."
    "I must make it up to her."
    "While I'm drowning with Yuri thoughts, classes has ended."
    "Well off to the Literature Club."

    stop music fadeout 2.0

    scene bg club_day
    with wipeleft_scene
    play music t3
    "Another day passes, and it's time for the club meeting already."
    "I've gotten a little more comfortable here over the past couple days."
    "Entering the clubroom, the usual scene greets me."
    show sayori 2x zorder 2 at t11
    s "Hi [player]~"
    mc "Yo, Sayori."
    mc "Looks like you're in a good mood today."
    s 1q "Ehehe~"
    s "I'm just still not used to you being in the club, that's all."
    mc "I see..."
    mc "...That's a pretty simple thing to get you in a good mood."
    mc "But I guess it's always the simple things with you, anyway."
    s 1d "Speaking of which..."
    s "I'm kinda hungry..."
    s "Will you come with me to buy a snack?"
    "This is one of her antics with me so that I'll buy her a snack."
    "I actually don't mind, since she is mt girlfriend after all."
    mc "Sure Sayori!"
    "As soon as we are about to leave, Sayori gets smacked by something flying."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p zorder 3 at hf32
    "{i}Pwap!{/i}"
    hide white
    s 4p "Kyaa--!"
    "It turns out to be a giant cookie wrapped in plastic."
    show sayori 4r at h11
    s "Yay! A cookie!~"
    s "I wonder where it came from?"
    "Sayori glances around."
    s 4m "I-Is this a miracle??"
    s "Am I being blessed by the cookie gods?"
    n "A cookie goddess, more like!"
    "I turned around and saw Natsuki coming towards us."
    show sayori zorder 2 at t22
    show natsuki 3z zorder 3 at l21
    mc "Hi, Natsuki the cookie goddess!"
    show sayori 4n
    n "Ahahaha!"
    "Natsuki punched me gently."
    show natsuki 3l zorder 3 at t21
    n "I {i}was{/i} just gonna give it to you."
    n 3d "It was totally worth seeing your reaction, though. Ahaha!"
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 4m "N-Natsuki!"
    s "That's so nice of you!"
    s 4s "I'm so happy..."
    "Sayori hugs the cookie."
    show sayori zorder 2 at t22
    mc "Jeez, just eat it..."
    "Sayori rapidly tears open the wrapper and takes a big bite."
    show sayori zorder 3 at f22
    s 4q "Sho good..."
    show sayori zorder 3 at hf22
    s 4o "Mmf--!"
    "Sayori suddenly clasps her hands over her mouth."
    s 4p "I bit my tongue..."
    show sayori zorder 2 at t22
    show natsuki zorder 3 at f21
    n 3a "Ehehe."
    n "You're going through a lot over just one cookie."
    "Natsuki takes a bite of her own cookie."
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 1c "Ah, yours looks really good too, Natsuki!"
    s "Can I try it?"
    show sayori zorder 2 at t22
    show natsuki zorder 3 at f21
    n 4e "Jeez..."
    n "Beggars can't be choosers!"
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 1h "But yours is chocolate..."
    show sayori zorder 2 at t22
    show natsuki zorder 3 at f21
    n 4c "Yeah, why do you think I gave you that one?"
    show natsuki zorder 2 at t21
    show sayori zorder 3 at f22
    s 1g "Fine..."
    s 1q "Still, I'm really happy that you shared this one with me."
    s "Ehehe~"
    show sayori behind natsuki zorder 2 at t21
    "Sayori gets out of her seat and goes behind Natsuki, then wraps her arms around her."
    n 12c "Ah-- Jeez..."
    n "I get it, I get it."
    "Cookie still in hand, Natsuki reaches up to nudge Sayori off of her."
    show sayori 1n at h21
    s "...{i}Om.{/i}"
    "Sayori suddenly leans down and takes a bite out of Natsuki's cookie."
    n 1p "{i}H-Hey!!{/i}"
    n "Did you seriously just do that?!"
    s 1q "Uhuhuhu!"
    show sayori at lhide
    hide sayori
    "Mouth full, Sayori trots away to safety."
    "I started to laugh, seeing how adorable they are."
    show natsuki zorder 3 at f21
    n 1w "Jeez! You're such a kid sometimes!"
    n 1h "Monika! Can you tell Sayori--"
    n 1c "--Eh?"
    "Natsuki glances around."
    "Monika isn't in the clubroom."
    n 4q "Ugh..."
    n "Where's Monika, anyway?"
    "I also see Yuri from her seat coming towards us as well."
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "Good question..."
    y "Have any of you heard anything about her being late today?"
    show sayori 1b zorder 3 at f32
    show yuri zorder 2 at t33
    s "Not me..."
    show sayori zorder 2 at t32
    mc "Yeah, I haven't either."
    show yuri zorder 3 at f33
    y 2l "Hm..."
    y "That's a bit unusual."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "I hope she's okay..."
    show sayori zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "Of course she's okay."
    n "She probably just had something to do today."
    n "She's the Club President after all..."
    show natsuki zorder 2 at t31
    show sayori 1l zorder 3 at f32
    s "I guess you're right, Natsuki."
    show sayori zorder 2 at t32
    show yuri 1a zorder 3 at f33
    y "You should be expecting that Sayori."
    y "You're the Vice President. You should be expecting her to be doing a lot of stuff."
    y "And also you should be expecting some of those tasks to be handed to you as well."
    show yuri zorder 2 at t33
    show sayori 1r zorder 3 at f32
    s "Ehehe, that's true..."
    show sayori zorder 2 at t32
    show natsuki 1l zorder 3 at f31
    n "Seriously Sayori, How come you're the Vice President but you do not know about this?"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "Suddenly, the door swings open."
    show monika 1g at l41
    m "Sorry! I'm super sorry!"
    mc "Ah, there you are..."
    m "I didn't mean to be late..."
    m "I hope you guys weren't worried or anything!"
    mc "It's okay, Monika."
    mc "What held you up, anyway?"
    show monika zorder 3 at f41
    m 1e "Ah..."
    m "Well, my last period today was study hall."
    m "To be honest, I kind of just lost track of time..."
    m "Ahaha..."
    show monika zorder 2 at t41
    show natsuki 2c zorder 3 at f43
    n "That makes no sense, though."
    n "You would have heard the bell ring, at least."
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1m "I must not have heard it, since I was practicing piano..."
    show monika zorder 2 at t41
    show yuri 1e zorder 3 at f44
    y "Piano...?"
    y "I wasn't aware you played music as well, Monika."
    show yuri zorder 2 at t44
    show monika zorder 3 at f41
    m 1l "Ah, I don't, really...!"
    m "I kind of just started recently."
    m 1m "I've always wanted to learn piano."
    show monika zorder 2 at t41
    show sayori 4x zorder 3 at f42
    s "That's so cool!"
    s "You should play something for us, Monika!"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "That's..."
    "Monika looks at me."
    m 1a "Maybe once I get a little bit better, I will."
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 4q "Yay~!"
    show sayori zorder 2 at t42
    mc "That sounds cool."
    mc "I'd also look forward to it."
    show monika zorder 3 at f41
    m 1b "Is that so?"
    m "In that case..."
    m "I won't let you down, [player]."
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    show monika 5 zorder 2 at t11
    hide sayori
    hide natsuki
    hide yuri
    "Monika smiles sweetly."
    mc "Ah..."
    mc "I didn't mean any pressure or anything like that!"
    m 1a "Ahaha, don't worry."
    m "I've been practicing a whole lot recently."
    m "And I'd really love the chance to share once I'm ready."
    mc "I see..."
    mc "In that case, best of luck."
    m 1j "Thanks~!"
    m 1a "So, I didn't miss anything, did I?"
    mc "Not...not really."
    show monika zorder 1 at thide
    hide monika
    "I choose to leave out Sayori's mischievous escapade."
    "I'm sure Natsuki will end up complaining to her, anyway."
    "It looks like everyone has already settled down."
    "Sayori somehow already finished her entire cookie."
    "Yuri is back to her book, and Natsuki disappeared into the closet."
    
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t6 

    "I'm really curious to talk to Yuri a little bit more..."
    "But at the same time, I would feel bad for distracting her from reading."
    "I catch a glimpse of the cover of her book."
    "It looks like the same book that she lent to me..."
    "More than that, she seems to be on the first few pages."
    show yuri 4a zorder 2 at t11
    y "Ah..."
    "Crap--"
    "I think she noticed me looking at her..."
    "She sneaks another glance at me, and our eyes meet for a split second."
    y 4b "..."
    "But that only makes her hide her face deeper in her book."
    mc "Sorry..."
    mc "I was just spacing out..."
    "I mutter this, sensing I made her uncomfortable."
    y 1i "Oh..."
    y "It's fine..."
    y 1a "If I was focused, then I probably wouldn't have noticed in the first place."
    y "But I'm just re-reading a bit of this, so..."
    mc "That's the book that you gave me, right?"
    y "Mhm."
    y "I wanted to re-read some of it."
    y 2q "Not for any particular reason...!"
    mc "Just curious, how come you have two copies of the same book?"
    y "Ah..."
    y "Well, when I stopped at the bookstore yesterday--"
    y 3o "Ah, that's not what I meant..."
    y "I mean--"
    y 1w "I...just happened to buy two of them."
    mc "Ah, I see."
    "There's something fairly obvious here that Yuri isn't telling me, but I decide to let it go."
    mc "I'll definitely start reading it soon!"
    y 2u "I'm glad to hear..."
    y "Once it starts to pick up, you might have a hard time putting it down."
    y 2c "It's a very engaging and relatable story."
    mc "Is that so...?"
    mc "What's it about, anyway?"
    y 1f "Well..."
    y "Mmm..."
    "Yuri closes the book and scans her eyes over the back."
    "The book is titled \"Portrait of Markov\"."
    "There's an ominous-looking eye symbol on the front cover."
    y 1a "Alright..."
    y "I just wanted to make sure I don't accidentally give anything away."
    y "Basically, it's about this girl in high school who moves in with her long-lost younger sister..."
    y "But as soon as she does so, her life gets really strange."
    y 1m "She gets targeted by these people who escaped from a human experiment prison..."
    y "And while her life is in danger, she needs to desperately choose who to trust."
    y 1i "No matter what she does, she ends up destroying most of her relationships and her life starts to fall apart..."
    mc "That's kind of--!"
    "That's kind of dark, isn't it?"
    "Yuri made it sound like it was going to be a nice story, so that dark turn came from nowhere."
    y 1c "Ahaha."
    "Yuri gently giggles, all of a sudden."
    y "Are you not a fan of that sort of thing, [player]?"
    mc "No, it's not that..."
    mc "I'm used to horror stuff, since I played some horror video games before."
    mc "Like {i}'Biohazard: The fall of the Raincoat Corp.'{/i} and {i}'Left2Die'{/i}"
    mc "I've watched some horror movies as well..."
    mc "Like {i}'Wrong Detour'{/i} and {i}'That'{/i}"
    mc "I can definitely enjoy those kinds of stories, so don't worry."
    y 2u "I hope so..."
    "Yeah... I totally forgot that Yuri is into those things."
    "She's so shy and reclusive on the outside, but her mind seems to be completely different."
    y "It's just that those kinds of stories..."
    y 1a "They challenge you to look at life from a strange new perspective."
    y "When horrible things happen not just because someone wants to be evil..."
    y 1m "But because they have their own goals, or their own philosophy that they believe in."
    y "Then suddenly, when you thought you related to the protagonist..."
    y "They're made out to be the naive one for letting their one-sided morals interfere with the villain's plans."
    y 3v "I'm...I'm rambling, aren't I...?"
    y "Not again..."
    y 4b "I'm sorry..."
    mc "Hey, don't apologize...!"
    mc "I haven't lost interest or anything."
    y "Well..."
    y "I guess it's alright, then..."
    y 4a "But I feel like I should let you know that I have this problem..."
    y "When I let things like books and writing fill my thoughts..."
    y "I kind of forget to pay attention to other people..."
    y 3t "So I'm sorry if I end up saying something strange!"
    y "And please stop me if I start talking too much!"
    mc "That's--"
    mc "I really don't think you need to worry..."
    mc "That just means you're passionate about reading."
    mc "The least I can do is listen."
    mc "It's a literature club, after all..."
    y 4a "Ah--"
    y "That's..."
    y "Well, that's true..."
    mc "In fact..."
    mc "I might as well get started reading it, right?"
    y 3n "Y-You don't have to!"
    mc "Ahaha, what are you saying?"
    mc "Just a moment ago, you said you were looking forward to it."
    mc "And remember earlier, you would like me to discuss it with you, right?"
    y 3o "..."
    mc "Let me just get the book..."
    "I quickly retrieve the book that I had put into my bag."
    mc "Also, this is to make it up to you for not reading it yesterday."
    mc "Alright...it's fine if I sit here, right?"
    "I slip into the seat next to Yuri's."
    y 3n "Ah...!"
    y "Yeah..."
    mc "Are you sure?"
    mc "You seem a little apprehensive..."
    y "That's..."
    y 4b "I'm sorry..."
    y "It's not that I don't want you to!"
    y "It's just something I'm not very used to..."
    y "That is, reading in company with someone."
    mc "I see..."
    mc "Well, just tell me if I end up distracting you or anything."
    y "A-Alright..."
    show yuri zorder 1 at thide
    hide yuri
    "I open the book and start the prologue."
    "I soon understand what Yuri means about reading in company."
    "It's as if I can feel her presence over my shoulder as I read."
    "It's not a particularly bad thing."
    "Maybe a little distracting, but the feeling is somewhat comforting."
    "Yuri is in the corner of my eye."
    "I realize that she's not actually looking at her own book."
    "I glance over."
    "It looks like she's reading from my book instead--"
    show yuri 3n zorder 2 at t11
    y "S-Sorry!"
    y "I was just--!"
    mc "Yuri, you really apologize a lot, don't you?"
    y "I...I do?"
    y 4a "I don't really mean to..."
    y "Sorry..."
    y 4c "I mean--!"
    mc "Ahaha."
    mc "Here, this should work, right?"
    "I slide my desk until it's up against Yuri's, then hold my book more between the two of them."
    y 2v "Ah..."
    y "I suppose so..."
    "Yuri timidly closes her own copy."
    "Once we each lean in a little bit, our shoulders are almost touching."
    "It feels like my left arm is in the way, so instead I use my right hand to hold the book open."
    mc "Ah, I guess that makes it kind of difficult to turn the page..."
    y "Here..."
    scene y_cg1_base with dissolve_cg
    "Yuri takes her left arm and holds the left side of the book between her thumb and forefinger."
    mc "Ah..."
    "I do the same with my right arm, on the right side of the book."
    "That way, I turn a page, and Yuri slides it under her thumb after it flips to her side."
    "But in holding it like this..."
    "We're huddled even closer together than before."
    "It's actually kind of distracting me...!"
    "It's as if I can feel the warmth of Yuri's face, and she's in the corner of my vision..."
    show y_cg1_exp1 at cgfade
    y "...Are you ready?"
    mc "Eh?"
    y "To turn the page..."
    mc "Ah...sorry!"
    mc "I think I got a bit distracted for a second..."
    "I glance over at Yuri's face again, and our eyes meet."
    "I don't know how I'll be able to keep up with her..."
    y "Ah..."
    show y_cg1_exp2 at cgfade
    y "That's okay."
    y "You're not as used to reading, right?"
    y "I don't mind being patient if it takes you a bit longer..."
    y "It's probably the least I can do..."
    y "Since you've been so patient with me..."
    mc "Y-Yeah..."
    mc "Thanks."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "We continue reading."
    "Yuri no longer asks me if I'm ready to turn the page."
    "Instead, I just assume that she finishes the page before me, so I turn it by my own volition."
    "We continue the first chapter in silence."
    "Even so, turning each page almost feels like an intimate exchange..."
    "My thumb gently letting go of the page, letting it flutter over to her side as she catches it under her own thumb."
    mc "Hey, Yuri..."
    mc "This might be a silly thought, but..."
    mc "The main character kind of reminds me of you a little bit."
    show y_cg1_exp1 at cgfade
    y "You...think so?"
    y "How does she?"
    mc "Well, I guess she's more blunt in a lot of ways..."
    mc "But she also second-guesses all of the things that she says and does."
    mc "Like she's afraid she'll do something wrong."
    mc "It's not like I can see into your head or anything..."
    mc "But they're kind of reminiscent of some of your mannerisms."
    y "I-I see..."
    scene bg club_day
    show yuri 2t zorder 2 at i11
    with dissolve_cg
    "Yuri remains silent for a moment."
    y "But [player]..."
    y "That's probably..."
    y "...a terrible thing to have in common with her!"
    y 4b "Uuuh, that's so embarrassing that you think that..."
    mc "W-Wait!"
    mc "I didn't mean it in a bad way or anything!"
    mc "Sorry, I really didn't know you were self-conscious about that sort of thing..."
    y "..."
    mc "I guess I more meant that it's kind of cute..."
    y 3q "A-Ah--"
    y "What are you saying all of a sudden...?"
    y "I...!"
    "I need to relieve her of the pressure."
    mc "Yuri..."
    show yuri 3p at s11
    "I held her hand."
    mc "What I mean is..."
    mc "You don't have to be embarassed about yourself."
    mc "It's cute to me that you are being yourself..."
    mc "...yet you still are able to manage to approach me."
    mc "As Sayori said yesterday, we can get along pretty well!"
    mc "And I can say we a pretty similar as well!"
    mc "I am a NEET that just likes to isolate myself and focus on my hobbies: Games and Anime."
    mc "And I am not saying that it's a bad thing."
    mc "We have similarities, as well as differences."
    mc "And that's what makes us compliment each other."
    mc "Monika was talking about piano earlier."
    mc "And I'd say that in playing it, it consists of melody and harmony."
    mc "Melody and harmony are different parts, but they compliment each other."
    mc "That's what I mean when it comes to you."
    mc "All I'm saying is that... You're Yuri."
    mc "And you're perfect the way you are."
    mc "Don't be embarassed."
    show yuri 3w at t11
    y "A-alright."
    y "I won't feel embarassed."
    y "For you [player]."
    y "Thank you."
    "I guess that calmed her down."
    mc "Anyway..."
    mc "You know what I'm trying to say, so..."
    y 1s "You're very thoughtful, [player]."
    "Yuri takes a step closer to me, then briefly squeezes my hand."
    "I think this is it for her."
    show yuri 2s at face(y=600) with dissolve
    stop music fadeout 2.0
    y "I kind of like that about you..."
    y "Correction,"
    y "I kind of {i}love{/i} that about you..."
    mc "Yuri--"
    y "Shh."
    "She put her finger at my lips."
    y "You want me to be myself, right?"
    y "So here am I... being {i}myself{/i}."
    show yuri 4b 
    "I think I know where this is going."
    "She seems to be hesitant still."
    mc "Go on. I will listen."
    y 4a "[player]..."
    y "I... I--"
    y 4c "I love you, [player]."
    y "I don't care if Sayori, Natsuki, or Monika is listening."
    y "What's important is what I feel."
    y "And I wanted to really show it to you."
    y 4a "[player]..."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"
    hide yuri
    "How am I supposed to respond to that?"
    "Wait. I should know what's my response to that."

    show black with dissolve_cg

    menu:
        "And of course, my response to her would be--"
        "I accept your confession, Yuri. I love you too.":
            hide black with dissolve_cg
            call positive_reply_3
        "I love you, Yuri... As a friend.":
            call silly_reply_3

    return

label positive_reply_3:
    show yuri 4a at face(y=600) with dissolve
    mc "Yuri..."
    mc "I accept your confession."
    mc "I love you too."
    mc "And I will be happy to be your boyfriend."
    show yuri 3m 
    "And with that, Yuri seems to be fully calmed down now."
    y "You're so sweet, [player]."
    y "I know you've been dealing with Sayori and Natsuki's antics."
    y 3j "And adding me to the mix is..."
    y "Are you sure you'll be okay?"
    mc "I don't mind."
    mc "I love you as much as I love them."
    mc "If i don't, then that would make me a liar, would it?"
    y "Y-yeah..."
    y "No worries, [player]. I will behave myself."
    "She leans in forward towards my face closer."
    show yuri 3l
    "She's leaning in for a kiss."
    "Not this again."
    "My heart beats faster as she approaches."
    m "Okay, everyone!"
    "Nice save again, Monika."
    "I owe you big time."
    show yuri 3n zorder 2 at t11
    y "M-Monika?"
    show monika 4 at l31
    show yuri 3n at h11
    y "...!"
    play music t5
    show monika zorder 3 at f31
    m "I think it's about time we share today's poems with each other."
    m "We might not have enough time if we wait too long."
    show monika zorder 2 at t31
    show yuri zorder 3 at f11
    y 3w "Ah..."
    "Yuri exhales, spared from finishing her thought."
    show yuri zorder 2 at t11
    show monika zorder 3 at f31
    m 1 "Is that alright, Yuri?"
    m "You look kind of down..."
    m "I'm sorry if you haven't been looking forward to this..."
    show monika zorder 2 at t31
    show yuri zorder 3 at f11
    y 3v "Ah, it's not..."
    y "...It's fine."
    show yuri zorder 2 at t11
    show monika zorder 1 at thide
    hide monika
    "Yuri releases her hand from the book, causing it to close on top of my thumb."
    mc "Alright..."
    mc "I guess I'll do some more reading tonight."
    mc "Or would you prefer I only read it with you?"
    y 2f "Um...!"
    y "I...guess I don't have too much of a preference either way..."
    mc "Hmm..."
    mc "In that case, I'll read a little more tonight."
    mc "It'll be more fun to read with you after it picks up a bit, you know?"
    y 2a "That's good reasoning."
    y "In that case, feel free to finish the first two chapters in your own time."
    mc "Alright!"
    show yuri zorder 1 at thide
    hide yuri
    "I stand up."
    "I make a mental note of where I left off in the book, then slip it back into my bag."

    scene bg club_day
    with wipeleft_scene

    "Time for poem sharing."
    show monika 1d zorder 1 at t41
    show sayori 4n zorder 2 at t42
    show yuri 3e zorder 3 at t43
    show natsuki 1k zorder 4 at t44
    "I showed all new 4 poems again to each one of them."
    "As expected, they all were astonished."
    show natsuki 1m at f44
    n "How are you writing poems this good, [player]?"
    show natsuki 1m at t44
    show yuri 1f at f43
    y "Yeah, [player]. I thought you never had experience in writing literature."
    show yuri 1f at t43
    show sayori 1x at f42
    s "Maybe [player] is trying so hard to impress you!"
    s "I just love your poems [player]."
    show sayori 1a at t42
    show yuri 1n at s43
    show natsuki 1n at s44
    "Natsuki and Yuri got flustered."
    show monika 5a at hf41
    m "I knew you were trying to impress!"
    m "But to be honest you seem to be doing pretty good so far."
    mc "Ehehe..."
    show monika 1a at t41
    "I do not know what to say at this point."
    mc "Anyways... Can I read your poems now?"
    "I read their poems one by one."
    hide sayori 
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    call showpoem (poem_test)
    "And that concludes my time at the club."
    
    stop music fadeout 2.0

    play music t8

    "I am ready to pack my stuff to go home."
    show sayori 1a at t11
    s "Me and Natsuki will be waiting outside."
    show sayori 1a at thide
    hide sayori
    "As I finish packing up, Yuri approaches me once more."
    show yuri 4a at t11
    y "[player]... can I walk with you again today as you go home?"
    mc "Sure, Yuri!"
    y 3m "Thank you, [player]."
    y "I love you."
    mc "I love you too."

    scene bg corridor
    with wipeleft_scene

    "I saw Sayori and Natsuki waiting outside the corridor."
    show sayori 1a at t21
    show natsuki 1a at t22
    mc "Ready to go home?"
    mc "Yuri is coming with us."
    mc "Also... will you accept Yuri as well to be my 3rd girlfriend?"
    show sayori 4r at h21
    s "Of course! The more the merrier!"
    n 4k "I don't mind really [player]."
    mc "Thank you so much both of you."
    "And thus all 4 of us walked together."

    scene bg residential_day
    with wipeleft_scene

    "As we walked down the road, Yuri seems to be uneasy."
    "It feels like she wants to do something for me... or I guess vice-versa."
    
    menu:
        "It's time for me to act."
        "Grab her hand.":
            "I grabbed Yuri's hand."
            show yuri 2p at h11
            y "[player]..."
            mc "Why?"
            mc "You seem... uneasy."
            mc "Maybe this helps you feel a bit relaxed."
            y 4c "Um... I- I just don't know how to react."
            y 1b "But thanks for your kind gesture."
            y 3d "I appreciate it."
        "Offer her your hand.":
            mc "Yuri..."
            show yuri 1a at t11
            mc "You seem... uneasy."
            "I extended my hand to her."
            mc "Here. come hold my hand."
            mc "Maybe this helps you feel a bit relaxed."
            "Yuri seems to be happy with my gesture."
            y 1b "Thanks for your kind gesture."
            y 3d "I'd love to!"
            "She took my hand and we continued walking."

    "Sayori noticed my gesture to Yuri and started to approach me."
    show yuri 3d at t33
    show sayori 1a at t32
    s "[player], I want to hold your hand as well~"
    "She started to hold my other hand."
    "Natsuki started to see the 3 of us."
    show natsuki 1p at t31
    n "Hey, I want to hold hands with [player] too!"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "She started to run..."
    "But she tripped on a rock."
    play sound fall
    show natsuki 1v at t11
    n "Eyaaah!"
    mc "Are you okay, Natsuki?"
    "I took her hand and tried to make her stand up."
    show natsuki 1v at s11
    n "O-ow! my ankle seemed to have been sprained."
    "She can barely stand on her own."
    "I think I know what I should do here."
    "I offered her to climb on my back."
    mc "Natsuki, climb on my back."
    mc "I'll carry you."
    show natsuki 4p at t11
    n "Eh? Y-you.. c-carry.. m-me?!"
    mc "Yes. I'd be gladly carrying you. You're my girlfriend after all."
    n 1s "Uuuuuuu..."
    n "Fine."
    n "But just this once!"
    n "It's not like I'll enjoy riding your back or anything..."
    show natsuki 1s at thide 
    hide natsuki
    "She climbed up my back."
    "I carried her then resumed holding hands with Yuri and Sayori."
    show yuri 1a at t31
    y "Look at how sweet you both are."
    show sayori 4s at t33
    s "Yeah, Natsuki. I kinda feel a little bit jealous now~"
    show natsuki 1v at t32
    n "S-stop it! You're embarassing me!"
    "I laughed."
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft

    scene bg house
    with wipeleft_scene

    "We arrived at my house."
    show yuri 1a at t11
    y "I'll take Natsuki off your back now. We'll go home together from here."
    show yuri 1a at t21
    show natsuki 1s at t22
    n "Uuuuu... I wanted to stay a bit more here."
    n "It's not like I'm enjoying myself or anything."
    n "But fine."
    show yuri 1a at thide
    show natsuki 1s at thide
    hide yuri
    hide natsuki
    mc "Thank you, Yuri."
    mc "See you tomorrow."

    scene bg bedroom
    with wipeleft_scene

    "Okay, 3rd girlfriend acquired!"
    "My only goal is to find diamonds..."
    "Which is acquiring all 4 of them."
    "It's been a fun ride today."
    "I have to prepare for tomorrow."
    "I need to get my poems ready."
    "Prepare yourself, [player]."
    "I'll make Renpy-sama proud of me."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    return 

label silly_reply_3:
    "Bruh."
    "You're getting on my nerves."
    "I don't even know what to do with {i}you.{/i}"
    "{i}You{/i} really are a degenerate person."

    menu:
        "Work with me here, okay?"
        "I accept your confession, Yuri. I love you too.":
            hide black with dissolve_cg
            call positive_reply_3
    
    return