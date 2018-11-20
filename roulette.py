thirthyfiveistoone = ["00","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","35","36"]
oneistoone=["black","red","odd","even"]
oneistotwo=["1st Column","2nd Column", "3rd Column", "1st Dozen", "2nd Dozen", "3rd Dozen"]
red=[1, 3, 5, 7, 9, 12,14, 16, 18, 19, 21, 23,25, 27, 30, 32, 34, 36]
black=[2, 4, 6, 8, 10, 11,13, 15, 17, 20, 22, 24,26, 28, 29, 31, 33, 35 ]
list_35to1 = []
list_1to1 = []
list_2to1 = []

def print_payout(num):
    print(list_35to1)

def roulette_input():
    innum=None
    print("Please enter the word ***finish**** in the bet amount when you have finished entering the amout and location of your bet")
    while innum!="finish":
        innum=input("Please enter number you want to bet on: ")
        if innum=="finish":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        list_35to1.append(inval)
    innum=None
    while innum!="finish":
        innum=input("Please enter black, red, even, odd to bet on and finish to exit: ")
        if innum=="finish":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        list_1to1.append(inval)
    innum=None
    while innum!="finish":
        innum=input("Please enter 1st Column, 2nd Column, 3rd Column, 1st Dozen, 2nd Dozen, 3rd Dozen  to bet on and finish to exit: ")
        if innum=="finish":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        list_2to1.append(inval)

def roulette_spin():
    import random
    return (random.choice(thirthyfiveistoone))

#Call to functions
roulette_input()
lucky_num = roulette_spin()
print_payout(lucky_num)


