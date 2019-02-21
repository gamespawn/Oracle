init python:
    claire_convo = 0
    coffeemaker = False
    claireweather1 = False
    claireweather2 = False
    claireweather3 = False
    claireplans1 = False
    claireplans2 = False
    claireplans3 = False
    clairenew1 = False
    clairenew2 = False
    clairenew3 = False

default messagecount = 0
default messageflag = 0


define i = Character ("Ish")
define s = Character ("Sylvie")
define L = Character ("Lachesis")
define u = Character ("???")
define k = Character ("Kassandra")
define c = Character ("Claire")
define v = Character ("Valenzia")
define I = Character ("Inigo")
define A = Character ("Aliya")
define f = Character ("Fariha")
define a = Character ("Astolfo")
define l = Character ("Lyra")
define r = Character ("Ricardo")
define Q = Character ("All")


image report = "MRP.png"
image sylvie normal = "Test_normal.png"
image sylvie worried = "Test_worried.png"
image sylvie happy = "Test_happy.png"
image sylvie angry = "Test_angry.png"
image sylvie sad = "Test_sad.png"

image testpoint = "testpoint.png"
image testpoint2 = "testpoint2.png"
image testpoint3 = "testpoint3.png"
image testpoint_idle = "idle.png"


label start:
    "(Here we go...)"
    v "Captains!"
    v "I have an announcement to make."
    v "Starting today, Ish here will be the newest Captain to join your ranks."
    f "Wait, Ish?"
    f "Why didn't you {i}tell{/i} me that you got promoted?"
    i "Sorry, hun. It was kind of a secret."
    A "Oooo. Secrets in the relationship...!"
    i "Wait it's not like--"
    v "Let me get through this, and then you all can start sounding off."
    A "..."
    f "..."
    i "..."
    v "Excellent. Now, as I was saying..."
    v "I expect you to treat her as you would each other."
    v "You're a unit, and she's proven herself an asset to this group."
    v "From today forward, she's no longer your student or inferior, but your equal."
    v "Please keep this in mind."
    v "And absolutely {i}no{/i} random pie throws, Aliya."
    A "I'll... {i}try.{/i}"
    v "Aliya."
    A "... Fiiiiiine."
    v "Excellent!"
    v "Since we're all fine here, I'll let you guys out for a little while so that you can get acquainted."
    I "But we already know her."
    v "Take a break when you're given one, Inigo."
    v "Show Ish how we do things around here, and make sure she feels welcome."
    v "And most importantly, get out of my office! There's much better places to be."
    Q "YES, COMMANDER!"

    "A bit later..."
    I "... And {i}this{/i} is your new office."
    i "Whoa...!"
    i "This is huge!"
    I "As I'm sure you've noticed, being a Captain is definitely a whole new world."
    i "We get assigned to major cases, right?"
    i "As much as I enjoyed being your Lieutenant, paperwork isn't really my speed."
    I "Exactly why I picked you to be our next Captain after Captain Alvarado retired."
    i "Wow... I, uh... Thanks!"
    I "Don't thank me with words."
    I "Show me you're deserving of the position by doing your best."
    i "I will!"
    I "Excellent."
    I "I'll leave you to start getting settled in here. I'll be back around to let you know about your first assignment."
    i "Yes, Captain Cruz. Thank you!"
    I "Hm."
    "(Wow, this office is really mine?)"
    "(Dang. I guess no more cubicle, huh?)"
    "(...)"
    "(Oh, Sisters, I'm gonna be bored in here, aren't I?)"
    "*Knock, Knock!*"
    f "I've got something for a certain Captain Isabel Meseta!"
    i "I wonder what that is!"
    f "You won't have to wonder too long!"
    i "Wait, Fari, can you close the door before you start?"
    f "Of course, of course. Wouldn't want to get you in trouble on your first day."
    f "Now, where was I...?"
    i "You could probably start with what's in your ha--"
    f "Right! Congratulating my amazing, super-duper fiancee on becoming a Captain!"
    i "Aw, thank you!"
    i "Fari, I'm so excited. I feel like I can start doing something... {i}big{/i}, y'know?"
    i "I feel almost dumb for being this giddy over it..."
    f "Heh. I definitely get what you mean."
    f "It's definitely a far cry from being a Lieutenant."
    f "There's so much that goes on behind the scenes that you don't really hear about as a regular citizen, or even as high as a lieutenant."
    f "And we're in a position to help deal with that. As Captains, we're the first ones to deal with big situations, and you should definitely feel giddy about ti!"
    i "Thanks. I feel a bit better, but I'm still not sure I'm ready."
    f "No one is when they start."
    f "It's just a matter of rising up to the challenge!"
    i "You know what? {i}Hell{/i} yeah! I can *eventually* do this!"
    f "That's... kinda the spirit!"
    i "You'll help me though, right?"
    i "I don't wanna mess this up."
    f "Of course I will. If one of us is unemployed, how're we going to pay rent in these parts?"
    f "The Capital's a bit too expensive to slack on money."
    i "Heh, you're right, you're right."
    i "Speaking of work, do you know anything about my first assignment?"
    f "Oh, shoot, {i}that's{/i} what I was going to--"
    "*Knock, Knock!*"
    i "Come in!"
    I "Captains Meseta and al-Rami, pardon the interruption."
    f "No worries. What's going on?"
    I "I'm here discuss the nature of your first assignment."
    I "Seems like I came just in time."
    f "Captain Cruz, if I may interrupt."
    I "For what?"
    f "Vice Oracle Azu sent this case file down for Captain Meseta."
    "(Oh, boy.)"
    "(I didn't think she'd get on me {i}this{/i} quickly.)"
    I "She's already giving her a case file? What for?"
    f "I don't know, actually! I'm kind of intrigued, though."
    f "Aren't you?"
    I "..."
    I "Perhaps a small amount."
    f "Well, hon--I mean Captain Meseta, open it!"
    "(Well, here goes nothin'.)"
    i "..."
    i "What the...!"
    f "A missing persons case?"
    I "Is this some kind of out-of-season April Fool's joke?"
    i "A missing persons report would've been national news."
    i "And this was well over four years ago!"
    f "This is definitely big."
    f "I'm almost certain that this was done completely under the table."
    I "That's the only way this would go undetected."
    f "Ish, you've definitely got a big job ahead of you."
    i "Yeah, it certainly seems like it."
    f "Well, remember that you've got the other Captains to help out if you need to."
    I "Indeed. Don't hesitate if you need assistance."
    i "I, uh... Thanks. Thanks a lot."
    f "Don't sweat it."
    f "I should probably get going, though. I've got my own assignments to get through."
    I "Like scrubbing the bathroom like the Commander ordered you to?"
    i "Wait, what?"
    f "D-don't worry about it! It's just some stupid bet."
    I "You had an obligation to send your weekly report in, and you did not."
    I "It would happen to the rest of us if we didn't."
    I "Also, Captain Meseta, remember to submit your reports. Two to five pages."
    i "W-will do, Captain."
    I "Excellent. Best of luck on your first assignment."
    i "Thanks."
    f "I guess I'll get going, too."
    f "Are we still on for lunch after work?"
    i "Maybe, if you don't smell like the bathroom."
    f "... Please don't make me think about that."
    f "Yeah, I'm gonna go now."
    f "See you in a few hours!"
    i "See ya!"
    "..."
    "(Alright. Let's take a look at this file.)"

    show report
    with fade

    "(Wait, I know her!)"
    "(No, no, {i}no{/i}...)"
    "(This can't actually be happening!)"
    "(...)"
    "(Dang it, Kira. How'd you get here?)"
    jump docscan

label docscan:
    call screen doc1

label picture1:
    hide screen doc1
    "(Sisters, that's a blast from the past.)"
    "(She was real proud of those freckles back then, but did everything she could to get rid of those glasses.)"
    "(Kira even broke her nose trying to walk without 'em one time in Sophomore year.)"
    "(...)"
    "(Hard to think that was almost twelve years ago.)"
    "(Come to consider it, that photo's not recent at all.)"
    "(We took that for her right before we wanted to get her a makeover for the Sweetheart's Gala.)"
    "(She said that she wanted \"one last look at how she looked before this inevitable debacle.\")"
    "(...{i}This{/i} is the last photo they had of her?)"
    "(How long has she been out of contact?)"


    jump docscan

label descrip1:
    hide screen doc1
    "(Her birthday was a week ago.)"
    "(She'd be... twenty-five.)"
    "("


label bedroom:
    v "Lieutenant Meseta!"
    i "Y-yes, Captain?"
    v "You and Lieutenant al-Rami are on patrol near the Legislative District today."
    f "Sorry, Ish. I tried getting the Gourmet District, but the order came from higher than expected."
    v "Indeed. Vice Oracle Azu wishes to see the two of you."
    i "Snap, really?"
    i "I wonder what it's about?"
    f "Not sure, but she's definitely asking."
    "(I'm willing to bet it's about the wedding...)"
    v "She is indeed."
    v "Before you head out, though, may I have a word with you in private, Lieutenant Meseta?"
    i "Um, sure."
    f "I'll go ahead and wait for you outside."
    i "Alright, I'll be right there."
    v "..."
    v "Ishabel."
    "(Oh, no.)"
    i "Yes, Captain?"
    v "I'm not sure how much of this you've been made aware of yet, but I find it my responsibility as your employer, as well as someone who cares about you, to be up front with you."
    v "Please, hae a seat. We'll be here for a bit."
    i "A-alright."
    i "What's going on?"
    v "It has been recommended to me that I... {i}remove{/i} you from your post."
    i "... What?"
    v "That's what I said, too."

    return

### CELLPHONE IMPLEMENTATION * CELLPHONE IMPLEMENTATION * CELLPHONE IMPLEMENTATION *


#### this code is made for 1920 x 1080 so if you use another dimension youre going to have to fiddle with the numbers to make this work
## rest of the code happens in screens.rpy and options.rpy




label phonestart:
    # always start with this, it hides the regular text box, brings up the phone and has a short delay
    # most of these calls include delays to make this look nicer
    # you can find the code behind these calls in options.rpy
    call phone_start

    if messagecount == 0 and messageflag == 0:
        jump message1

    if messagecount == 1 and messageflag == 1:
        jump message2

label message1:

    # this brings up the message, first slot is the name, and second is the content
    # notice how it has _start at the end, the first one is special as there are no delays before it. use this for the first message
    call message_start("nadia", "hey, this is a phone texting thingy")

    # added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
    call reply_message("oh really? what does it do lol")

    # this one is the same as the above one, but instead it has one more place for you to set an image
    # you have to make the image be small enough to fit the screen or its gonna stretch weird!
    call message_img("nadia", "it works with images too!","images/pic1.png")
    call message_img("nadia", "receive cute pics from your friend","images/pic2.png")
    call message("nadia", "the text box changes depending on how much content there is. dont put too big images or its gonna look weeeeiiiird")
    call message("nadia", "you can also do menus here")

    # the next line is the menu system, first and third slot are the menu options, second and fourth one are what happens when you click it

    # i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
    call screen phone_reply("awesome!","choice1","lame","choice2")
    # i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
    ##call screen phone_reply3("awesome!","choice1","lame","choice2","im gay","choice3")

label choice1:
    # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
    call phone_after_menu

    # whenever you put the sender name to be "me" it is the player characters own message!
    call message_start("me", "awesome")
    call message("nadia", "i hope you like it")

    jump aftermenu

label choice2:
    call phone_after_menu
    call message_start("me", "lame")
    call message("nadia", "well, its a shame but your feelings are valid")

    jump aftermenu

label choice3:
    call phone_after_menu
    call message_start("me", "im gay")
    call message("nadia", "nice")

    jump aftermenu

label aftermenu:
    call message("nadia", "check the code for comments on how the code works, thanks for your time!")
    call message("nadia", "the base for this code and this stretched phone background comes from cute demon crashers")
    call message("nadia", "the images were drawn by my gf @sloppydraws")

    # this one puts away the phone!
    call phone_end



label message2:
    call phone_start

    call message("Kainda", "Sorry.")

    call phone_end
