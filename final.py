#Project: Receptionist Hell Author KQ

#so far the script and dialogue works great, there's just no graphical interface yet so it's difficult to read in the terminal

def game_over():
    print('GAME OVER')
    print('')
    start_again = input("Would you like to start again, perhaps with less sass? yes|no : ")
    if start_again == 'yes':
        start_game()
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
        print('')
        print(name + ": Uhhh......he says he's busy.......torturing the mortal souls of ye sinners and what not...")
    else:
        print("-Are you, like, four years old? Neither a yes or no is an acceptable answer to that question.-")
        print('')
        response_5b()
        
        

def response_5a():
    print("All Seeing Eye: This colleague of the All Seeing Eye's home phone number is 666.666.666....7.")
    print('')
    ans = input(name + ": Oh no, not today Satan! = y | *dial the number....* = n: ")
    ans = ans.lower()
    if ans == 'y':
        print('')
        print("All Seeing Eye: That's it. I, the All Seeing Eye am fed up with your incompetence! I wish to speak with your manager!")
        print('')
        print(name + ": ......Ok....")
        print('*you dial the aforementioned number*')
        response_5b()
    elif ans == 'n':
        response_5b()
    else:
        print("-The only acceptable excuse for mispelling one letter is -OH WAIT THERE ISN'T ONE!-")
        print('')
        response_5a()

#----------

def response_4a():
    print("All Seeing Eye: I wish to meet a colleague of the All Seeing Eye, but I refuse to levitate to his abode for fear of ruining my Louis Vuitton in the brimstone surrounding his house.")
    print("I, the All Seeing Eye, foresee that you shall call this man, and convince him to commute across the entire Hell Dimension, so that I personally can be satisfied.")
    print("")
    ans = input(name + ": Wait, you're wearing Vuitton...But you don't have any legs? = y |" \
                + "Of course, what is this colleague's phone number? = n: ")
    print("")
    ans = ans.lower()
    if ans == 'y':                                                                                                                                                                                                                                                                                            
        print("All Seeing Eye: I exist within an inter-dimensional plane between your one dimensional reality and the rest of the cosmos, I do not need legs to wear shoes. I have space feet.")
        response_5a()
    elif ans == 'n':
        response_5a()
    else:
        print("-You're the reason why I have no faith in humanity.-")
        print('')
        response_4a()

def response_4b():
    print("All Seeing Eye: I do not need....'shank'...I have eyedrops.")
    response_4a()

#---------

def response_3b():
    print('')
    print("Old Lady: *if shock were a person* I WAN'T TO SPEAK WITH YOUR MANAGER! *for I am shooketh*")
    print('')
    game_over()

def response_3a():
    print(name + ": Oh look, I think I see the case!")
    print("")
    print("*an eyeball floats into the room, unblinking.....it hands the case to the old woman*")
    print("")
    print("Old Lady: Oh, thank goodness! You found my Justin! You're so much more helpful than this pathetic excuse for a receptionist. How did you find my Justin?")
    print("")
    print("All Seeing Eye: I am Eye, the All Seeing Eye. I see all things with my eye that I wish to see with my eye. I see your case, and I see the incompetence of this receptionist.")
    print("")
    ans = input(name + ": And I see a bit of irritation around your pupil, may I suggest a healthy dosage of shank to quwell the redness? = y |" \
                + "......How may I assist you...Eyeball.. = n: ")
    print("")
    ans = ans.lower()
    if ans == 'y':
        response_4b()
    elif ans == 'n':
        response_4a()
    else:
        print("-If you can't type, you can't be my type.-")
        print('')
        response_3a()

#----------

def response_2c():
    print('')
    print("Old Lady: You darn millenials, you kids should learn to respect your elders!")
    print('')
    ans = input(name + ": And you old people should learn to respect your kids, cause we're gonna be the ones deciding if we should unplug your life support to charge our phones. = y |" \
                + "You're right mam, I'm sorry. = n: ") 
    ans = ans.lower()
    if ans == 'y':
        response_3b()
    elif ans == 'n':
        response_3a()
    else:
        print("-Every one of my genie wishes is for you to learn how to type.-")
        print('')
        response_2c()

def response_2b():
    print("Barack Obama, right?")
    print('')
    ans = input(name + ": Ahh, so you're annoying and ignorant...score. = y |" \
                + "Nevermind. = n: ")
    ans = ans.lower()
    if ans == 'y':
        response_2c()
    elif ans == 'n':
        response_3a()
    else:
        print("-Are you pressing the keys with a yard stick while you desperately cling to the end of a cliff for your life? If so, then why are you playing this game?-")
        print('')
        response_2b()
    
def response_2a():
    print('')
    print("Old Lady: Hmmm, that doesn't seem to be working, maybe you should be less annoying when you say it.")
    print('')
    ans = input(name + ": Or maybe I should be more annoying, you know, give you a run for your money. = y |" \
                + "*imitates Morgan Freeman* Here Justin the Case.. = n: ")
    ans = ans.lower()
    if ans == 'y':
        response_2c()
    elif ans == 'n':
        print('')
        print("Old Lady: Who are you immitating, that one black guy.....")
        response_2b()
    else:
        print("-Even if you're the world's most notorious pecker, I never imagined that you could stoop so low as to make a typo with one letter.-")
        print('')
        response_2a()

#-----------

def response_1a():
    print("Old Lady: Can you help me find my case? I named him Justin, I've been calling him for hours but he isn't answering: ")
    print('')
    ans = input(name + ": Maybe you should try again, you know, Justin Case. = y |" \
                + "Of course! Here Justin, here Justin the Case! = n: ")
    ans = ans.lower()
    if ans == 'y':
        print('')
        print("Old Lady: You're not funny. Just like that one black guy...The one with the voice that could make anything sound interesting...")
        response_2b()
    elif ans == 'n':
        response_2a()
    else:
        print("-I literally made it as simple as possible to answer the question.-")
        print('')
        response_1a()
    
def response_1b():
    print("Old Lady: Really, but you don't look smart enough to be anything else.")
    print('')
    ans = input(name + ": And you don't look young enough to still be alive, yet here you are. = y |" \
                + "Ha ha, I get that a lot. How can I help you? = n : ")
    ans = ans.lower()
    print("")
    if ans == 'y':
        print('')
        print("Old Lady: Ughh, how rude.")
        response_1a()
    elif ans == 'n':
        response_1a()
    else:
#if the user somehow fails to type a y or an n, there is a default output that is triggered to condescendlingly
#chastise them for their incompetance
        print("-Am I asking too much here? Are your fingers just really bad at typing?-")
        print('')
        response_1b()
        
#-----------
def question_1():
    ans = input("Old Lady: Excuse me, are you the receptionist? yes|no : ")
    ans = ans.lower()
    if ans == 'yes':
        response_1a()
    elif ans == 'no':
        response_1b()
    else:
        print("It's literally a yes or no question ya dingus!")
        print('')
        question_1()
        


#there are going to be lists of 'acceptable' and 'non-acceptable' answers
#too many non-acceptable answers will trigger a Game Over, aka you'll be fired
#questions and answer reactions will be stored in functions, which will be called
#depending upon user input:
#there will be an interface which may be uploaded from pygame.com, or created by myself

def start_game():
    print('')
    print("*An elderly woman approaches your desk, the smell of old-person-soap is so pungent it begins to choke the air from your lungs.*")
    print('')
    question_1()

name = input("Enter a name for yourself (literally anythig except Nigel Thornberry you ignoramous): ")
if name == 'Nigel Thornberry':
    print('')
    print("Sometimes I'm very dissapointed with my generation.")
    name == ''
    game_over()
elif name == 'nigel thornberry':
    print('')
    print("Sometimes I'm very dissapointed with my generation.")
    name == ''
    game_over()
else:
    start_game()


