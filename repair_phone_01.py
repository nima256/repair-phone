# here we want to talk about repair phone that it is turn off and it does not turn on

# here i ask that his/her phone has battery or not  
battery = input("is your phone before it turn of has battery?     say yes , no==>")
# now hi/she have to connect it supply power
if battery == "yes":
    # if it yes now we have to know number of the suooly power 
    print("you have to connect it to suplly power")
    print("after answer this question")
    # i ask that is supply power show 0/7?
    seven = input("does supply power show 0/7?   say yes , no===>")
    if seven == "yes":
        # if hi/she say yes she/he has to answer a question 
        print("okay answer this question")
        # a qestion is does her/him phone turn on?
        phone_on = input("does your phone turn on?  say yes , no")
        if phone_on == "yes":
            # if yes solution for it
            print("it okay do not worry")
            print("for fix it you just have to change battery")
        # if no another qestion
        elif phone_on == "no":
            print("okay answer this question")
            # question is dose him/her phone has sound but not image or not?
            sound_not_image = input("does your phone has sound but not image   say yes , no ==>")
            # if yes solution for it
            if sound_not_image == "yes":
                print("it has tow condition")
                print("first your lcd is broken for fix it you have change all the lcd")
                print("second image output problem for fix it you have to understand if the lcd socket is the problem or lcd flat or image ic after that for fix all of this problem you have change it repair it")
            # if no it defently yes (:
            elif sound_not_image == "no":
                print(" it defently yes you say incorrect")
        # every thing else incorrect 
        else:
            print("incorrect")
    # elif the supply power does not show 0/7 number some question
    elif seven == "no":
        print("answer this question")
        # a question is does power supply show the 0/2 number?
        two = input("does supply power show 0/2 fix?  say yes , no==>")
        # if yes solution for it
        if two == "yes":
            print("the problem is software")
            print("it has two condition")
            print("first your hard is die for fix it you have to change it or you can say goodbye with your phone")
            print("second your boot is gone for fix it you have to install boot")
        # elif no some question
        elif two == "no":
            print("okay answer this question")
            # a question does power suplly show the 0/5 number when you hold power key and when you leave the key it show 0 ?
            hold_5_leave_0 = input("does power supply show 0/5 if you hold power key and when you leave the key it show 0 ?    say yes , no==>")
            # if yes solution for it
            if hold_5_leave_0 == "yes":
                print("it has tow condition")
                print("first your problem is software for fix it you have to enter usb android")
                print("second the problem is cpu for fix it you have to change cpu or say bye to your phone")
            # if no a question 
            elif hold_5_leave_0 == "no":
                print("okay answer this question")
                # is power supply show 0 number?
                zero = input("does the supply power show the 0 ?     say yes , no===>")
                # if yes solution for it
                if zero == "yes":
                    print("it has two condition")
                    print("first your ic supply and cpu has die for fix it you have change both of them or change all board")
                    print("second the connector battery is disconnect for fix it you have to understand that the connector is break or is discoonect if is break you have to change it or if disconnect you have to repair it")
                # if no a qustion
                elif zero == "no":
                    print("okay please answer this question")
                    # a question is the current your phone is using more than 4 or is your power supply alarming?
                    short_circuit = input("is the current your phone is using more than 4 or is your power supply alarming?   say yes , no===>")
                    # if yes solution for it
                    if short_circuit == "yes":
                        print("the problem is a connection board")
                        print("answer this question")
                        # a question does your phone drop in water or sprinkle water on it?
                        water = input("does your phone drop in water or sprinkle water on it?   say yes , no===>")
                        # if yes solution for it
                        if water == "yes":
                            print("it has two condition")
                            print("first your phone is drop in water for fix it you have to wash it with ultrasonic")
                            print("second find piece that syndetic")
                        # if no a question
                        elif water == "no":
                            print("okay answer this question")
                            # a question have you used a faulty charger or have you recently had severe power fluctuations?
                            input_power_oscillation = input("have you used a faulty charger or have you recently had severe power fluctuations?    say yes , no===>") 
                            # if yes solution for it
                            if input_power_oscillation == "yes":
                                print("it has two condition")
                                print("first you have to find defective piece")
                                print("second you have to change ic suplly")
                            # if no it defently yes
                            elif input_power_oscillation == "no":
                                print("it is defently yes you say incorrect")
                    # elif short circuit no i do not know
                    elif short_circuit == "no":
                        print("i don't know")
                        # error handling
                    else:
                        print("incorrect")
                else:
                    print("incorrect")
            else:
                print("incorrect")
        else:
            print("icorrect")
    else:
        print("incorrect")
# elif battery has no charge connect it to charge
elif battery == "no":
    print("connect it to charge")
    # a qustion
    charge = input("is your phone charge?")
    # if yes the battery was empty do not worry
    if charge == "yes":
        print("your battery was empty do not worry you can use it")
    # if no solution for it
    elif charge == "no":
        print("your battery is sleep for fix it you have to connect it to supply power and with a current of 4 mA give it a direct shock to charge the battery")
# else incorrect
else:
    print("incorrect")