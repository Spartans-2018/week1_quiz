thirthyfiveistoone = ["00","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","35","36"]
# oneistoone=["black","red","odd","even"]
# oneistotwo=["1st Column","2nd Column", "3rd Column", "1st Dozen", "2nd Dozen", "3rd Dozen"]
red=[1, 3, 5, 7, 9, 12,14, 16, 18, 19, 21, 23,25, 27, 30, 32, 34, 36]
black=[2, 4, 6, 8, 10, 11,13, 15, 17, 20, 22, 24,26, 28, 29, 31, 33, 35 ]
col1=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34 ]
col2=[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35 ]
col3=[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36 ]
doz1=[1,2,3,4,5,6,7,8,9,10,11,12]
doz2=[13,14,15,16,17,18,19,20,21,22,23,24]
doz3=[25,26,27,28,29,30,31,32,33,34,35,36]
dict_35to1 = {}
dict_1to1 = {}
dict_2to1 = {}

def print_payout(num):
    total_payout=0
    for i in dict_35to1.keys():
        if int(i)==num:
            payout=int(dict_35to1[i])*35
            print(f'Payout for betting on {i} is {dict_35to1[i]} * 35 = {payout}')

    for j in dict_1to1.keys():
        if j == "black":
            if num in black:
                payout = int(dict_1to1[j])*2
                print (f'Payout for betting on {j} is {dict_1to1[j]} * 2 = {payout}')
        elif j == "red":
            if num in red:
                payout = int(dict_1to1[j])*2
                print (f'Payout for betting on {j} is {dict_1to1[j]} * 2 = {payout}')
        if j == "odd":
            if num%2!=0 and num not in ["0","00"]:
                payout = int(dict_1to1[j])*2
                print (f'Payout for betting on {j} is {dict_1to1[j]} * 2 = {payout}')
        elif j == "even":
            if num%2==0 and num not in ["0","00"]:
                payout = int(dict_1to1[j])*2
                print (f'Payout for betting on {j} is {dict_1to1[j]} * 2 = {payout}')
    # "1st Column", "2nd Column", "3rd Column", "1st Dozen", "2nd Dozen", "3rd Dozen"
    for k in dict_2to1.keys():
        if k=="1st Column":
            if num in col1:
                payout = int(dict_2to1[k])*2
                print (f'Payout for betting on {k} is {dict_2to1[k]} * 3 = {payout}')
        elif k=="2nd Column":
            if num in col2:
                payout = int(dict_2to1[k])*2
                print (f'Payout for betting on {k} is {dict_2to1[k]} * 3 = {payout}')
        elif k=="3rd Column":
            if num in col3:
                payout = int(dict_2to1[k])*2
                print (f'Payout for betting on {k} is {dict_2to1[k]} * 3 = {payout}')

        if k=="1st Dozen":
            if num in doz1:
                payout = int(dict_2to1[k])*2
                print (f'Payout for betting on {k} is {dict_2to1[k]} * 3 = {payout}')
        elif k=="1st Dozen":
            if num in doz2:
                payout = int(dict_2to1[k])*2
                print (f'Payout for betting on {k} is {dict_2to1[k]} * 3 = {payout}')
        elif k=="1st Dozen":
            if num in doz3:
                payout = int(dict_2to1[k])*2
                print (f'Payout for betting on {k} is {dict_2to1[k]} * 3 = {payout}')


def roulette_input():
    innum=None
    print("Please enter the word ***F**** in the bet amount when you have finished entering the amout and location of your bet")
    while innum!="F":
        innum=input("Please enter number you want to bet on: ")
        if innum=="F":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        dict_35to1[innum] = inval
    innum=None
    while innum!="F":
        innum=input("Please enter black, red, even, odd to bet on and F to exit: ")
        if innum=="F":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        dict_1to1[innum]=inval
    innum=None
    while innum!="F":
        innum=input("Please enter 1st Column, 2nd Column, 3rd Column, 1st Dozen, 2nd Dozen, 3rd Dozen  to bet on and F to exit: ")
        if innum=="F":
            break
        inval=input(f"Please enter amount you want to bet on {innum}: ")
        dict_2to1[innum] = inval

def roulette_spin():
    import random
    return (random.choice(thirthyfiveistoone))

#Call to functions
roulette_input()
lucky_num = roulette_spin()
print(f'WINNING NUMBER IS {lucky_num}')
print_payout(lucky_num)


