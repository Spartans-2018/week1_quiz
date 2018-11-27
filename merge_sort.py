def merge(list1,list2):
    temp=[]
    i=0
    j=0
    while len(list1)!=0 and len(list2)!=0:
        if list1[i] >= list2[j]:
            temp.append(list1[i])
            list1.pop(i)
        else:
            temp.append(list2[j])
            list2.pop(j)
    while len(list1)!=0:
        temp.append(list1[i])
        list1.pop (i)
    while len(list2)!=0:
        temp.append(list2[j])
        list2.pop (j)
    return (temp)

def merge_sort(mylist):
    if len(mylist)==0 or len(mylist)==1:
        return mylist
    else:
        ls1 = mylist[0:len(mylist)//2]
        ls2 = mylist[len(mylist)//2:len(mylist)]
        a = merge_sort(ls1)
        b = merge_sort(ls2)
        return merge(a,b)


print(merge_sort([10,12,31,4,5,-1,100,200,500,-2]))
# print(merge_sort([10,12,31,4,5,-1,100,200,500,-2]))
import timeit
inlist=[10,12,31,4,5,-1,100,200,500,-2]
t = timeit.Timer(stmt="merge_sort(inlist)", globals=globals())
print(t.timeit(number=1000000))

# time for 1 million iterations ---> 225.678915055

