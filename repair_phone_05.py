# here want to write script about antenna problem
# here i ask a question that understand error that phone give it 
antenna = input("does your phone give a sim card insertion error or not finding a network?   say sim  ,  network==>")
# if phone give sim card insertion error solution for it 
if antenna == "sim":
    print("i will write sim card insertion error you can be read it")
# elif phone give not finding a network another question for it  
elif antenna == "network":
    print("okay please answer this question")
    # this question ask that did you use another sim card and it is still error
    another_sim = input("do you use another sim and it is still error?    say yes or no==>")
    # if it is still error solution for it
    if another_sim == "yes":
        print("okay do not worry the problem is telecommunications")
    # elif it is not error when you enter another sim a question again
    elif another_sim == "no":
        print("okay answer this question")
        # in this question about sim that is it old or distorted
        distorted_sim = input("is your sim card is distorted or old?   say yes or no")
        # if it is distorted or old solution for it
        if distorted_sim == "yes":
            print("you have to enter sim card again if it still error you have change your sim card")
        # elif it is not distorted or old another question
        elif distorted_sim == "no":
            print("okay please answer this question")
            # this is about that your phone hit or no
            ic_pf  = input("does your phone hit?  say yes or no==>")
            # if it is hit solution for it
            if ic_pf == "yes":
                print("your problem is IC PF")
                print("for fix it you have to repair it or change it")
            # if it is not hit another question
            elif ic_pf == "no":
                print("okay answer this question")
                # this question ask that does your phone old or your phone wet 
                antenna_connections = input("does your phone old or your phone wet?   say yes or no ==>")
                # if it is wet or old solution for it
                if antenna_connections == "yes":
                    print("your ptoblem is antenna connections")
                    print("for fix it you have to do tin removal dead or change foundation")
                # if it is not wet or old another quedtion for it
                elif antenna_connections == "no":
                    print("please answer this question")
                    # this question ask that is your phone wet  
                    water = input("was your phone wet")
                    # if it is wet solution for it
                    if water == "yes":
                        print("well the problem is antenna headquarters")
                        print("for fix it you have to change antenna headquarters or check foundation connection")
                    # if it is not wet another question
                    elif water == "no":
                        print("okay answer this question")
                        # this question ask that your phone recently repair or not
                        antenna_transmission_cable = input("does your phone recently repair?   say yes or no===>")
                        # if it is repair recently solution for it 
                        if antenna_transmission_cable == "yes":
                            print("well your problem is antenna transmission cable")
                            print("for fix it you have to change the cable")
                        # elif if is not repair recently another question 
                        elif antenna_transmission_cable == "no":
                            print("okay answer the last question")
                            # this question ask do you use non-standard charger or power swing 
                            cpu  = input("do you use non-standard charger or power swing?   say yes or no===>")
                            # if he/she use non-standard charger or power swing solution for it
                            if cpu == "yes":
                                print("okay your problem is CPU")
                                print("you have to change or repair it")
                            # elif she/he does not use non-standard charger or power swing so his/her phone is not broken beacause he/she say all the question no(:
                            elif cpu == "no":
                                print("you say all thing no):")
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