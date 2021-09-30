# here we want to write script that show your problem 
# the problem is about speaker
print("please answer this question")
# here i ask question that the sound is weak or it is disconnect
sound = input("is your phone sound weak or it is disconnect?  say weak or diconnect===>")
# if sound weak some solution for it
if sound == "weak":
    print("your speaker is die")
    print("for fix it please change your speaker")
# if it is disconnec you have to answer some question
elif sound == "diconnect":
    print("please anwer this question")
    # here i want to understand that is handsfree socket wet?
    handsfree_wet = input("is your handsfree socket wet?  say yes or no====>")
    # and here i want to understand that is her/him phone hit or not
    hit = input("is your phone hit?   say yes or no ==.")
    # here i ask that is her/him phone drop in water?
    water = input("is your phone drop in water?")
    # if her/him handsfree wet solution for it
    if handsfree_wet == "yes":
        print("your handsfree socket die")
        print("for fix it you have to change it or repair it")
    # here i write elif to if user write no it write next question
    elif handsfree_wet == "no":
        # here if her/him phone hit solution for it
        if hit == "yes":
            print("your phone problem ic sound ic")
            print("for fix it you have to change or repair it")
        # here i write elif to if user write no it write next question
        elif hit == "no":
            # here if the phone drop in wather some solution for it
            if water == "yes":
                print("the problem is ic ways to speaker")
                print("for fix it check all the ways or check your resistor and condenser in the wave ic to speaker")
            # here i write elif to if user write no it write next question
            elif water == "no":
                print("incorrect")
            # error handling
            else:
                print("incorrect")
        else:
            print("incorrect")
    else:
        print("incorrect")
else:
    print("incorrect")

