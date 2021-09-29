# here we want to find your problem that you have not a sound from microphone
# here i ask question to understad the problem

# here i ask was phone wet?
water = input("is your phone wet?" "say yes , no===>")
# then i ask were you use bad handsfree?
bad_handsfree = input("do you use bad handsfree?" "say yes or no===>")
# after i ask was her/him phone hit?
phone_hit = input("is your phone hit?" "say yes or no====>")
# here i ask was her/him phone wet or repaired recently
fix_or_water = input("your phone recently repaired? or wet" "say yes or no===>")

# here if the phone was wet so solution for it
if water == "yes":
    print("your microphone has die")
    print("for fix it you have to repair your microphone or change it")
elif water == "no":
    # after if she/he use badhandsfree some solution for it
    if bad_handsfree == "yes":
        print("your handsfree socket has short circuit")
        print("for fix it you have to repair or change it")
    # here i write elif to if user write no it write next question
    elif bad_handsfree == "no":
        # here if her/him phone was hit so some solution for it
        if phone_hit == "yes":
            print("your sound ic has die")
            print("for fix it you have to repair or change it")
        # here i write elif to if user write no it write next question
        elif phone_hit == "no":
        # here if her/him phone fix recently or wet?
            if fix_or_water == "yes":
                print("the problem is the ways")
                print("for fix it you have to check all the ways or check resistance and condenser")
            elif fix_or_water == "no":
                print("i do not know")
            # error handling
            else:
                print("incorrect")
        else:
            print("incorrect")
    else:
        print("incorrect")
else:
    print("incorrect")