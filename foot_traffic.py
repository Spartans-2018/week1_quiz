mylist=[]
myvistors=[]
myrooms=[]
with open("traffic.txt") as myfile:
    for i in myfile.readlines():
        mylist.append(i.strip().split(" "))
# entries = sum(1 for i in mylist if i[2]=="I")
# mylist.sort(key=lambda x:(x[2],x[0],x[1]))
# myvistors= list(set(i[0] for i in mylist))
myrooms=list(set(int(i[1]) for i in mylist))
myrooms.sort()
for rooms in myrooms:
    tentry = 0
    texit = 0
    tcount = 0
    for i in mylist:
         if(i[2])=="I" and int(i[1])==rooms:
            tentry += int(i[3])
         elif(i[2])=="O" and int(i[1])==rooms:
            texit += int(i[3])
            tcount+=1
    tavg= (texit - tentry)/tcount
    print(f'Room {rooms}, {tavg:.2f} minute average visit, {tcount} visitor(s) total')


