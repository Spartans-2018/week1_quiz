def roulette_odds():
    thirthyfiveistoone = ["00","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","35","36"]
    oneistoone=["black","red","odd","even"]
    oneistotwo=["1st Column","2nd Column", "3rd Column", "1st Dozen", "2nd Dozen", "3rd Dozen"]
def roulette_input():
    dict_35to1={}
    dict_1to1={}
    dict_2to1={}
    innum=None
    print("Please enter the word ***finish**** in the bet amount when you have finished entering the amout and location of your bet")
    while innum!="finish":
        innum=input("Please enter number you want to bet on: ")
        if innum=="finish":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        dict_35to1[innum]=inval
    innum=None
    while innum!="finish":
        innum=input("Please enter black, red, even, odd to bet on and finish to exit: ")
        if innum=="finish":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        dict_1to1[innum]=inval
    innum=None
    while innum!="finish":
        innum=input("Please enter 1st Column, 2nd Column, 3rd Column, 1st Dozen, 2nd Dozen, 3rd Dozen  to bet on and finish to exit: ")
        if innum=="finish":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        dict_2to1[innum]=inval

    print(dict_35to1)
    print(dict_1to1)

roulette_input()
