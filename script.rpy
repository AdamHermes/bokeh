define a = "Amelia" # gán biến cho tên nhân vật
define l = "Layla"
define c = "Charlotte"
define m = "me"
define s = "someone"
define om = "Old man"
label start:

    play music "bgmusic.mp3"#chạy nhạc
    image v1 = im.Scale("ameliav1.png", 1100, 950)#chỉnh kích cỡ hình
    scene city: #show background
        size(1920,1080)
    show v1 #show nhân vật đặt lên trước background
    a "Hello and welcome to Chasing Star."#thoại nhân vật
    a "Hope you will enjoy this game."
    stop music fadeout 1.0#dừng nhạc bgmusic
    with Dissolve(2)#2 dòng này dùng để chuyển cảnh
    pause 1
    scene truong
    play music "chuongtruong.mp3"
    "This is my first day at this school..."
    "And i am about to be late...tch (should not have stayed up so late last night). "
    "Oh, sorry i forgot to introduce myself..."
    "I'm ABC and today is my first day at Aurora high school."
    stop music fadeout 3.0
    "Although i might look like a typical high school student with no talents or special interests..."
    "I'm actually quite famous..."
    "In the.... game development community."
    "Hahaha."
    "To be honest, i'm just working part time in a few indie game studios."
    "So you can say that i'm quite good at programming."
    "I used to be mocked and teased back in my secondary school..."
    "Because i always talked about games..."
    "I won't make the same mistake twice..."
    "I will lead a new normal life in this high school: hanging out with friends, chatting, and going trips together... "
    "As long as they don't know my hobby."
    "It will still be fine."
    "Actually..."
    "I wish i could find friends who understand my hobby and help me make my own games."
    "A dream is just a dream... i guess..."
    "I gotta be hurry!"
    play music "running.mp3"
    with Dissolve(3)
    pause 2
    stop music fadeout 3.0
    scene lophoc with Dissolve(2)
    "Feww... glad i made it on time..."
    "Let's see..."
    "Okay that seat near the window would be great."
    s "Hey... wait "
    "Huh."
    "I turn around and a girl is running towards me"
    image c1 = im.Scale("charlottev3.png", 1100, 950)
    show c1 with Dissolve(1)
    s "Can i have that seat please?"
    "Oh you want that seat near the window?"
    s "..."
    menu:
        "Agree and let her take the seat":
            jump agree
        "Disagree":
            jump disagree
label agree:
    "Alright just take the seat,... i dont mind."
    s "..."
    s "thank you."
    hide c1
    "She walks to her seat"
    jump after_choice1
label disagree:
    "I'm afraid not, i want to seat near the window too."
    s "..."
    s "...."
    s "..... alright."
    pause 2
    hide c1
    "She walks away"
    jump after_choice1
label after_choice1:
    "She seems like a shy girl."
    "She is pretty tho..."
    "Nah i don't have time to think about her."
    "Let's just focus on making new friends now..."
    with Dissolve(2)
    pause 2
    scene truongchieu:
        size(1920,1080)
    play music "chuongtruong.mp3"
    "Fewwww what a tiring day."
    "Today i make friends with 2 other dudes."
    "They all seemed nice."
    "A good start... i guess"
    stop music fadeout 3.0
    "Guess i will go eat something now..."
    "Oh right..."
    "I forgot to mention it in the morning..."
    "I moved to this city to study high school."
    "So now i live in a rented-apartment and i don't live with my parents..."
    "Which means i often eat out at night."
    "Though i would love to cook."
    "I think i should give myself a treat today."
    "I think i might go grab some ramen for dinner."
    play music "walking.mp3"
    with Dissolve(2)
    pause 2
    scene ramenstore:
        size(1920,1080)
    stop music fadeout 2
    "This ramen store is just 5 min-walk from school."
    "I have noticed it when i walked pass it in the morning."
    "It looks so cool and the atmosphere is cozy too..."
    image rc1 = im.Scale("ramenchef1.png", 1100, 950)
    show rc1 with Dissolve(1)
    om "Hey kiddo."
    om "You look new.."
    om "Just got to this place huh?"
    "For some reason, i don't like his voice."
    "But i guess he is a nice person."
    "Yeah i just moved into the apartment 4 blocks from here."
    "One ramen please."
    "I try to make a smile as i think that old ramen chef doesn't like young people."
    om "Okay."
    pause 3
    hide rc1  with Dissolve(2)
    "...."
    "The ramen is so good though."
    "Guess it's late now"
    "Imma head home"
    play music "walking.mp3"
    with Dissolve(2)
    pause 2
    scene nightstreet:
        size(1920,1080)
    stop music fadeout 3.0
    "Feww what a day..."
    "I guess it's hard for a newcomer like me to get used to this city."
    "At least..."
    "I'm glad that i have walked through this road before."
    "It's even hard for a native to find the right way to the apartment."
    "The road is too tangled, i guess..."
    s "Hey...Wait for me..."
    "What"
    "Has someone just called me?"
    image a3 = im.Scale("am.png", 1100, 950)
    show a3
    "A beautiful girl just appears right in front of me."
    "Hey, can i ask you something"
    "Oh now i remember her..."
    "She is the representative of the first-year student"
    "She just had a wonderful speech yesterday."
    "How could i forget her..lol..."
    "Sure. You are... Amelia - the representative right, how can i help you?"
    "She gets a little bit shy, i think she doesn't like people calling her like that"
    a "um..."
    a "I remember seeing you walking on this road this morning."
    a "I suppose..."
    a "You live in Rosemary apartment too, right? "
    "too?"
    "I guess i know what she wants."
    a "Um it's just that..."
    a "I forgot the road to the apartment."
    a "And my phone is power off too so..."
    "Okay don't worry."
    "I have just moved here too but i think i know this road pretty well."
    "Let's me guide you to the apartment then"
    "I see her face brighten up for a moment."
    a "Thank you very much."
    "She smiles and starts to walk with me."
    hide a3 with Dissolve(2)
    play music "walking.mp3"
    with Dissolve(2)
    pause 2
    scene flat:
        size(1920,1080)
    stop music fadeout 3
    "After walking for 5 minutes we finally arrive at the apartment."
    "Both of us have been silenced since and it gradually turns awkward..."
    image a3 = im.Scale("am.png", 1100, 950)
    show a3
    a "Ummm..."
    a "..."
    a "Thank you for guiding me..."
    a "What is your name though?"
    "Oh, I'm ABC"
    a "Um thank you ABC"
    a "It seems that we live in the same place."
    a "Hope to see you around soon..."
    a "Goodbye..."
    a "She smiles at me and walks away"
    hide a3 with Dissolve(3)
    "She is such a charming and gentle girl..."
    "I think i got a wrong impression of her when i knew she is the representative of the first year student."
    "I think she would be strict and ... unapproachable..."
    "Not many students have talked to her though..."
    "..."
    "She would be hellar popular in school in like 2 to 3 days."
    "when others get to know more about her..."
    "After all..."
    "She is the type of person everyone wants to be friend with."
    "Unlike me..."
    "I sigh as i walk to the elevator"
    play music "elevatorbell.wav"
    with Dissolve(2)
    pause 2
    scene hall:
        size(1920,1080)
    stop music fadeout 3
    "I walk out of the elevator and head to my room."
    "Until i see..."
    show a3 with Dissolve(2)
    "Amelia is standing right at the end of the hall."
    "It seems that we both live on the same floor."
    "She sees me and waves at me."
    "I wave back and say goodnight to her."
    "She smiles and walks into her room."
    hide a3 with Dissolve(3)
    "I guess we are gonna get close soon..."
    "I close my door behind me."
    scene room:
        size(1920,1080)
    "Feww..."
    "This first day isn't too bad."
    "Hope i will make more friends tomorrow..."
    "..."
    "The people i have met today..."
    "They are all nice and friendly."
    "I wonder what will happen if they know about my secret..."
    "that i'm a total gaming nerd..."
    "Nahh..."
    "Let's just forget it and go to bed now"
    "Let's call it a day..."









































