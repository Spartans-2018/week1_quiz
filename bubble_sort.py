def bubble_sort(mylist):
    for i in range(len(mylist)-1):
        for j in range(len(mylist)-1):
            if mylist[j]<mylist[j+1]:
                temp = mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
    return mylist

in_list = [10,12,31,4,5,-1,100,200,500,-2]
exp_op = in_list
exp_op.sort()
in_list1=[1,2,500,20,-1,4,4,500,20,-1,4,4]
exp_op1 = in_list1
exp_op1.sort()

assert bubble_sort(in_list)==exp_op
assert bubble_sort(in_list1)==exp_op1
import timeit
inlist=[10,12,31,4,5,-1,100,200,500,-2]
t = timeit.Timer(stmt="bubble_sort(in_list)", globals=globals())
print(t.timeit(number=1000000))

#for 1 million iterations time take was 87.712716285