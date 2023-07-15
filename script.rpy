define a = "Amelia" # gán biến cho tên nhân vật
define l = "Layla"
define c = "Charlotte"
define m = "me"
define s = "someone"
label start:

    play music "bgmusic.mp3"#chạy nhạc
    image v1 = im.Scale("ameliav1.png", 1160, 1000)#chỉnh kích cỡ hình
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
    image c1 = im.Scale("charlottev3.png", 1160, 1000)
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
    "She walked to her seat"
    jump after_choice1
label disagree:
    "I'm afraid not, i want to seat near the window too."
    s "..."
    s "...."
    s "..... alright."
    hide c1
    "She walked away"
    jump after_choice1
label after_choice1:
    "She seems like a shy girl."
    "She is pretty tho..."
    "Nah i dont have time to think about her."
    "Let's just focus on making new friends now..."
    with Dissolve(2)
    pause 2
    scene truong with Dissolve(2)
    play music "chuongtruong.mp3"
    "Fewwww what a tiring day."
    "Today i make friends with 2 other dudes."
    "They all seemed nice."
    "A good start... i guess"





























