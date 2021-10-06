#!/bin/python3
# hello
# here we want to repaire a camera that does not work
# here i ask a question that understand does her/him phone fall of the high or not
fall = input("does your phone fall of the high?      say yes or no==>")
# if yes the phone fall of the high solution for it 
if fall == "yes":
    print("okay answer this question")
    # question is does your phone damaged
    hurt = input("does your phone damaged?     say yes , no==>")
    # if the phone damaged solution for it
    if hurt == "yes":
        print("okay for fix it you have to change the camera")
    # if the phone does not damaged answer a question 
    elif hurt == "no":
        print("okay answer this question")
        # question is is the camera socket is out of place
        camera_place = input("is the camera socket is out of place?      say yes or no==>")
        # if the camera socket is out of place solution for it 
        if camera_place == "yes":
            print("for fix it have to take a camera socket on it's place")
        # if the camera socket is not out of place your camera is not broken beacause you say all the question no
        elif camera_place == "no":
            print("i don't know")
        # error handling
        else:
            print("incorrect")
    else:
        print("incorrect")
# if the phone does not fall of high answer another question 
elif fall == "no":
    print("okay answer this question")
    # question is does your phone wet
    water = input("does your phone wet?   sa yes or no==>")
    # if the phone is wet solution for it 
    if water == "yes":
        print("for fix it you have to wash the camera socket")
        print("or you can change your camera")
    # you say all thing no
    elif water == "no":
        print("okay i don't know your problem")
    # error handling
    else:
        print("incorrect")
else:
    print("incorrect")