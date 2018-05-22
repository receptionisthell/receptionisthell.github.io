#Project: Receptionist Hell Author KQ v 5.4.934

#so far the script and dialogue works great, there's just no graphical interface yet so it's difficult to read in the terminal
def game_over():
    print('GAME OVER')
    print('')
    start_again = input("Would you like to start again, perhaps with less sass? yes|no : ")
    if start_again == 'yes':
        question_1()
    elif start_again == 'no':
        print("Loser.")
    else:
        print("That's not very nice.")
#---------



def response_5b():
    print("*the phone rings, it's uncanny tone seeming to echo out of the black depths of the receiver as you press the cold plastic to your ear, " \
    + "sweat dripping from your brow.....*")
    print('')
    #wait a few seconds in game
    print("*Suddenly the second phone at your desk rings, breaking the silence of certain death.*")
    print('')
    ans = input("*Realising that you've only reached his receptionist, you hang up on the devil.* = y |" \
    + "*pick up the phone* Hello this is receptionist hell -I m-mean Hell's Receptionist, how may I help you? = n: ")
    ans = ans.lower()
    if ans == 'y':
        game_over()
    elif ans == 'n':
        print("*you hand the phone to the All Seeing Eye, he only blinks at you slowly, scrutinizing the fabric of your soul*")
        
        

def response_5a():
    print("This colleague of the All Seeing Eye's home phone number is 666.666.666....7.")
    print('')
    ans = input("Oh no, not today Satan! = y | *dial the number....* = n: ")
    ans = ans.lower()
    if ans == 'y':
        print('')
        print("That's it. I, the All Seeing Eye am fed up with your incompetence! I wish to speak with your manager!")
        print('')
        print("......Ok....")
        print('*you dial the aforementioned number*')
        response_5b()
    elif ans == 'n':
        response_5b()

#----------

def response_4a():
    print("I wish to meet a colleague of the All Seeing Eye, but I refuse to levitate to his abode for fear of ruining my Louis Vuitton in the brimstone surrounding his house.")
    print("I, the All Seeing Eye, foresee that you shall call this man, and convince him to commute across the entire Hell Dimension, so that I personally can be satisfied.")
    print("")
    ans = input("Wait, you're wearing Vuitton...But you don't have any legs? = y |" \
                + "Of course, what is this colleague's phone number? = n: ")
    print("")
    ans = ans.lower()
    if ans == 'y':                                                                                                                                                                                                                                                                                            
        print("I exist within an inter-dimensional plane between your one dimensional reality and the rest of the cosmos, I do not need legs to wear shoes. I have space feet.")
        response_5a()
    elif ans == 'n':
        response_5a()

def response_4b():
    print("I do not need....'shank'...I have eyedrops.")
    response_4a()

#---------

def response_3b():
    print('')
    print("*if shock were a person* I WAN'T TO SPEAK WITH YOUR MANAGER! *for I am shooketh*")
    print('')
    game_over()

def response_3a():
    print("Oh look, I think I see the case!")
    print("")
    print("*an eyeball floats into the room, unblinking.....it hands the case to the old woman*")
    print("")
    print("Oh, thank goodness! You found my Justin! You're so much more helpful than this pathetic excuse for a receptionist. How did you find my Justin?")
    print("")
    print("I am Eye, the All Seeing Eye. I see all things with my eye that I wish to see with my eye. I see your case, and I see the incompetence of this receptionist.")
    print("")
    ans = input("And I see a bit of irritation around your pupil, may I suggest a healthy dosage of shank to quwell the redness? = y |" \
                + "......How may I assist you...Eyeball.. = n: ")
    print("")
    ans = ans.lower()
    if ans == 'y':
        response_4b()
    elif ans == 'n':
        response_4a()

#----------

def response_2c():
    print('')
    print("You darn millenials, you kids should learn to respect your elders!")
    print('')
    ans = input("And you old people should learn to respect your kids, cause we're gonna be the ones deciding if we should unplug your life support to charge our phones. = y |" \
                + "You're right mam, I'm sorry. = n: ") 
    ans = ans.lower()
    if ans == 'y':
        response_3b()
    elif ans == 'n':
        response_3a()

def response_2b():
    print("Barack Obama, right?")
    print('')
    ans = input("Ahh, so you're annoying and ignorant...score. = y |" \
                + "Nevermind. = n: ")
    ans = ans.lower()
    if ans == 'y':
        response_2c()
    elif ans == 'n':
        response_3a()
    
def response_2a():
    print('')
    print("Hmmm, that doesn't seem to be working, maybe you should be less annoying when you say it.")
    print('')
    ans = input("Or maybe I should be more annoying, you know, give you a run for your money. = y |" \
                + "*imitates Morgan Freeman* Here Justin the Case.. = n: ")
    ans = ans.lower()
    if ans == 'y':
        response_2c()
    elif ans == 'n':
        print('')
        print("Who are you immitating, that one black guy.....")
        response_2b()

#-----------

def response_1a():
    print("Can you help me find my case? I named him Justin, I've been calling him for hours but he isn't answering: ")
    print('')
    ans = input("Maybe you should try again, you know, Justin Case. = y |" \
                + "Of course! Here Justin, here Justin the Case! = n: ")
    ans = ans.lower()
    if ans == 'y':
        print('')
        print("You're not funny. Just like that one black guy...The one with the voice that could make anything sound interesting...")
        response_2b()
    elif ans == 'n':
        response_2a()
    
def response_1b():
    print("Really, but you don't look smart enough to be anything else.")
    print('')
    ans = input("And you don't look young enough to still be alive, yet here you are. = y |" \
                + "Ha ha, I get that a lot. How can I help you? = n : ")
    ans = ans.lower()
    print("")
    if ans == 'y':
        print('')
        print("Ughh, how rude.")
        response_1a()
    elif ans == 'n':
        response_1a()                                                   
        
#-----------
def question_1():
    print("*An elderly woman approaches your desk, the smell of old-people-soap so potent it chokes the air from your lungs*")
    print("")
    ans = input(" Excuse me, are you the receptionist? yes|no : ")
    ans = ans.lower()
    if ans == 'yes':
        response_1a()
    elif ans == 'no':
        response_1b()
        





#there are going to be lists of 'acceptable' and 'non-acceptable' answers

#too many non-acceptable answers will trigger a Game Over, aka you'll be fired

#questions and answer reactions will be stored in functions, which will be called
#depending upon user input:


#there will be an interface which may be uploaded from pygame.com, or created by myself
question_1()
