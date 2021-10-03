# here we want to write script that solve insert SIM card error
# here i ask a question that underdtand is her/his sim old or not 
old_sim = input("does your sim card old?  say yes or no==>")
# if her/his sim is old solution for it 
if old_sim == "yes":
    print("okay the problem is your sim card")
    print("for fix it you have to change sim or put it in sim socket again")
# elif her/his sim is not old another question
elif old_sim == "no":
    print("okay answer this question")
    # this question ask that your sim card stuck inside the sim connector
    stuck = input("has your SIM card been stuck inside the sim connector?   say yes or no==>") 
    # if the sim card stuck inside the sim connector solution for it
    if stuck == "yes":
        print("okay your sim connector is die")
        print("for fix we have two condition")
        print("first you have to check connector bases if the connector bases is disconnect you have to solder the bases or if connector bases is break you have to change it")
        print("second you can change all teh connector bases")
    # elif the sim card is not stuck inside the sim connector so another question 
    elif stuck == "no":
        print("okay answer this question")
        # a question ask that was your phone wet
        water = input("was your phone wet?    say yes or no")
        # if it is wet solution for it
        if water == "yes":
            print("for fix it you have to check the path of the sim cannector to find place that is disconnect")
        # elif it is not wet another question
        elif water == "no":
            # in this question i ask that does her/him phone hit or fall of the height
            hit = input("was your phone hit or fall of the height?   say yes or no==>")
            # if phone hit or fall of the height solution for it
            if hit == "yes":
                print("your problem is sim card ic")
                print("for fix it you have to change sim ic or repair it")
            # elif phone is not hit or fall of the height another question
            elif hit == "no":
                print("okay answer the last question")
                # in this question i ask do have severe power fluctuations recently
                severe_power_fluctuations = input("do you have severe power fluctuations recently?    say yes , no===>") 
                # if you have severe power fluctuations recently solution for it
                if severe_power_fluctuations == "yes":
                    print("the problem is cpu")
                    print("for fix it you have to change the cpu")
                    print("or say goodbye to your phone")
                # elif you do not have severe power fluctuations recently
                # i do not know your problem
                elif severe_power_fluctuations == "no":
                    print("i do not know youur problem")
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