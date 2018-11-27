def quicksort(myinput):
    if len(myinput)==0:
        return []
    # taking 0th element ***
    # pivot = myinput[0]
    # myinput.pop(0)

    # Max and Min ***
    # pivot = min(myinput)
    # pop_ind = myinput.index(pivot)
    # myinput.pop(pop_ind)

    import statistics
    med = statistics.median(myinput)
    pivot = min(myinput, key=lambda x:abs(x-int(med)))
    pop_ind = myinput.index(pivot)
    myinput.pop(pop_ind)

    lessthan = []
    greaterthan=[]
    for i in myinput:
        if i <= pivot:
            lessthan.append(i)
        else:
            greaterthan.append(i)

    outlist = quicksort(lessthan) + [pivot] + quicksort(greaterthan)
    return outlist

# exp_output = [10,12,31,4,5,-1,100,200,500,-2]
# exp_output.sort()
# assert quicksort([10,12,31,4,5,-1,100,200,500,-2]) == exp_output, "Not Sorted"
import timeit
inlist=[10,12,31,4,5,-1,100,200,500,-2]
t = timeit.Timer(stmt="quicksort(inlist)", globals=globals())
print(t.timeit(number=10000000))
# print(timeit.timeit("func_call()", setup="from __main__ import func_call"),1)

# 0th element --> time 13.072976090000001 (10 million iterations)
# max element --> time 16.462494274999997 (10 million iterations)
# min element --> time 16.16.289814959000 (10 million iterations)
# closest to median element --> 15.895517873000001 (10 million iterations)









