label mod_script_1:
 
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2

    mc "Aaand, done."
    "I finished another episode of my favorite anime {i}'The 100 Girls who Super Duper Liked You'{/i}."
    mc "Aijou Rensho is such a chad, making all of his girlfriends happy."
    mc "It doesn't make sense. How does he do it?"
    mc "He has 6 girlfriends now. How will he be doing if he has all 100 of them?"
    "All of this thinking makes my stomach growl."
    mc "Welp, I can't think stright if my stomach is not happy."
    mc "Guess I'll go to the kitchen to get something to eat."
    "I went downstairs to get something to eat."

    scene bg kitchen
    with wipeleft_scene

    mc "I wonder what's in the menu today?"
    "I gently open the fridge."
    mc "Ah great. Just more... {i}ika.{/i} (squid)"
    "I pulled out my leftover bowl of fried calamari inside the fridge."
    "I preheated them in the oven and ate it quickly."

    scene bg bedroom
    with wipeleft_scene

    mc "There goes another weekend for me. Tomorrow I will be in school again and nothing extraordinary will happen as usual."
    "My life has been always as normal as can be. I am your typical highschool student that has no girlfriends."
    "I will never get one because it's impossible for me."
    "That's why my usual routine every weekend is to play games and watch anime."
    "You can consider me to be a NEET, I don't care."
    "But deep down... I want to at least have some friends."
    mc "I wish I could be like Aijou Rensho..."
    mc "I wanted to experience what it feels like to have at least 1 girlfriend."
    "With that in my mind, I dosed of to sleep."

    scene black
    with wipeleft_scene

    stop music

    play music m1

    r "I can fix that for you, [player]."
    mc "Who the he-"
    $ r_name = "Renpy"
    r "Hi, [player]. I have been watching you every single day."
    mc "Wait, who are you? Where are we? Is this a dream?"
    r "Well, yes. You're inside your dream right now."
    r "And I am Aijou Renparou. Or Renpy for short."
    mc "Aijou... Renparou? WAIT, are you related to Aijou Rensho?"
    r "Um, yeah. Sort of. I created him."
    mc "You... created him?"
    r "Yes, he is a creation of mine who has a fraction of my power."
    mc "Your power? Are you some sort of God?"
    r "Why, yes I am. I am Renpy, the God of all visual novels. I created you and this world."
    mc "Wait, Visual Novels? Like the favorite romance game that I always play, {i}'Lub-dub Literature Club'{/i}?"
    mc "And what do you mean by creating me? Am I a visual novel character?"
    r "That's one way to put it I guess."
    r "You were created when the {i}player{/i} started this game."
    r "... I know it's going to be hard processing all of this..."
    r "... but my main point is that I came to you so I can fix your life."
    r "... Nobody wants their main character be a boring NEET for the rest of their life."
    r "... Sooooooooo, I'm letting you experience what Aijou Rensho experienced."
    r "You're getting a girlfriend!"
    mc "Huh?"
    r "... Aaaand not just one, but 100 Girlfriends!"
    mc "Wait, what?"
    r "Thank me later."
    "I am dumbfounded after this 'entity' spoke to me about having 100 girlfriends like it's nothing."
    mc "Wait, wait, Renpy, sir."
    r "Call me 'Renpy-sama'. And do you have something to ask me, my dear friend?"
    mc "I just couldn't handle all of this... things especially in a dream. Maybe my mind is just playing tricks on me."
    mc "I'm not really sure if I'll believe you or not."
    mc "And also... I have been to programming class before but... isn't Renpy a girl?"
    r "Oh, right. You must be talking about my twin sister, Aijou Renpirou."
    r "She gave me this world to play with. She's working on other visual novels."
    r "And as far as believing me..."
    r "In the words of a famous talk-no-jutsu master, {i}'believe it!'{/i}"
    r "But you would like some sort of evidence so..."
    menu:
        "Aijou Renparou is a handsome God.":
            call forced_choice
        "Aijou Renparou is a handsome God.":
            call forced_choice
        "Aijou Renparou is a handsome God.":
            call forced_choice

    r "Okay that's enough for you [player], you have to wake up now or you'll be late for school!"
    mc "Wait, Wait I have mo-"

    scene bg bedroom
    stop music

    "BZZT! BZZT! BZZT!"
    "I shut off the alarm clock."
    "What the heck was that dream I had?"
    "Probably one of the weirdest ones."
    mc "Welp, time for me to get dressed for school..."
    return

label forced_choice: 
    
    mc "Aijou Renparou is a handsome God."
    mc "Wait, why did I say that?"
    r "There is the evidence that you need. There was a pre-written option displayed and it was chosen and it made you react."
    r "I can make you say and do what I want, but I want you to enjoy."
    mc "So That was your doing?"
    r "Yes, my good friend."
    r "Do you now believe me?"
    mc "I-I guess so..."
    "I don't really know what to answer at this point."
    mc "So how will you give me 100 Girlfriends?"
    r "Just trust the process and carry on."
    r "You will love it!"
    mc "O-okay, I guess."
    r "Oh and I'll give them to you as a challenge."
    r "You up for a game?"
    mc "Oh yes, I love games! What kind of game?"
    r "This is the only rule that you must follow with this game..."
    r "If any of these girlfriends gets rejected/neglected by you, I have no choice but to delete them."
    mc "DE-DELETEEEEEEEE?"
    mc "Why would you do such a thing?"
    r "It's simple, I need some sort of free space in order to run the world daily without crashing."
    r "And deleting would be the best option in order for the game to be functional again."
    r " So yeah..."
    mc "How will I know if a girl will become my girlfriend?"
    r "Oh you know, the same thing how Aijou Rensho got his."
    r "A zing! There will be a zing when your eyes meet!"
    mc "Ah, I see..."
    return