# this script is about that the phone is not charging
# here again i want to ask a question 
# and realy reason that are importebt

# here i want to unsderstand that user use another charger other than her/him charger
charge = input("do you use another charger and still it does not charging   yes or no=====>")
# then i give solution that if charger is die what to do
if charge == "no":
    print("your charger is die")
    print("you have to change your cable or change your charger head")
# here if it is still not charging with another charger 
# i ask some another question to give solution
elif charge == "yes":
    print("please answer this question")
    # here i want to understand that chareger socket has output or no
    output_socket_charger = input("does your charger socket has an output?  say yes or no===>")
    # and here if charger socket does not have output i write what to do to it will solve
    if output_socket_charger == "no":
        print("your charger socket is die")
        print("for fix it you have to change it")
    # here if it has output so ask question to understand it problem
    elif output_socket_charger == "yes":
        print("please ask this question") 
        # here i ask that is the ohm meter number is 0
        ohm_meter = input("does ohm meter show 0?   say yes or no===>")
        # if it is 0 solution for it
        if ohm_meter == "yes":
            print("your socket charger is die")
            print("for fix it you have to change your socket charge")
            # here if it is not 0 so it is defenetly 4.99
            # and some another question
        elif ohm_meter == "no":
            print("ok so it defenetly show 4.99")
            print("okay answer this quastion")
            # here i ask is her/him was phone wet?
            ways = input("does your phone has wet?    say yes or no===>")
            # and it was wet i write solution to it will fix
            if ways == "yes":
                print("your ways has problem")
                print("for fix it you have to find disconnect way")
            # and if it was not wet 
            # some another question (:
            elif ways == "no":
                print("okay answer this quastion")
                # here i want to underestan to was the phone hit or not
                charge_ic = input("does your phone hit?  say yes or no====>")
                # if it was hit so i write solution for fix it
                if charge_ic == "yes":
                    print("your charge ic has die")
                    print("for fix it you have to change or repair it")
                # if not so another question (:(:
                elif charge_ic == "no":
                    print("okay answer this question")
                    # then i want to understand is she/he put down batter a lot to the connector be break or not
                    battery_connector = input("do you put down battery a lot?   say yes or no==>")
                    # if yes so solution
                    if battery_connector == "yes":
                        print("the problem is battery connector")
                        print("for fix it you have to change it or soldier the battery connector")
                    # if not some another question(:(:(:
                    elif battery_connector == "no":
                        print("okay please ask this question")
                        # here i want to understand if her/him phone hit
                        ic_supply = input("does your phone hit? say yes or no===>")
                        # if yes some another solution
                        if ic_supply == "yes":
                            print("your phone problem is ic supply")
                            print("for fix it you have to change it")
                        # if not the last question
                        elif ic_supply == "no":
                            print("okay answer this question")
                            # then i want to understan if they push bad charger or put charger whack in socket
                            socket_charger = input("do you use bad charger or push the cherger whack?   say yes or no==>")
                            # here if she/he use bad charger or put charger whack so some solution
                            if socket_charger == "yes":
                                print("your problem is socket charger")
                                print("for fix it you have to change it")
                            elif socket_charger == "no":
                                print("i realy do not know your problem ")        
                            # error handling
                            else:
                                print("incorrect")
                        else:
                            print("incorrect")
                    else:
                        print("incorrect")
                else:
                    print("incorrect")
            else:
                print("incorrect")
        else:
            print("incorrect")
    else:
        print("incorrect")
else:
    print("incorrect")    