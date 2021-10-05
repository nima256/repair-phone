#!/bin/python3

# hello here we want to repire 
# wifi and bluetooth dose not turn on
# here i ask a question that understand does her/him phone hit or not
hit = input("does your phone hit?   say yes or no===>")
# if the phone hit solution for it
if hit == "yes":
    print("okay for fix it you have to change the wifi ic or repair it the bluetooth and wifi ic is the same")
# elif the phone does not hit answer this question
elif hit == "no":
    print("okay answer this question")
    # question is does your phone wet
    water = input("does your phone wet?    say yes or no==>")
    # if the phone is wet solution for it
    if water == "yes":
        print("for fix it you have to wash the ic")
        print("if top solution does not work do this change or repair ic")
    # elif the phone is not wet answer another question
    elif water == "no":
        print("answer question")
        # question is does your phone restart automatically
        restart = input("does your phone restart automatically?   say yes or no===>")
        # if the phone restart automatically so;ution for it 
        if restart == "yes":
            print("for fix it you have to flash your phone")
            print("if top solution does not work do this one change ic")
        # elif the phone does not restart automatically another question 
        elif restart == "no":
            print("answer last question")
            # question is does your phone flasd recently 
            flash = input("does your phone flash recently?    say yes or no==>")
            # if the phone flash recently 
            if flash == "yes":
                print("you have to do this to fix your phone : change ic")
            elif flash == "no":
                print("i do not know your problem")
            # error handling
            else:
                print("incorrect")
        else:
            print("incorrect")
    else:
        print("incorrecct")
else:
    print("incorrect")
