def decimal_to_binary(num):
    if num==0:
        return [0]
    bnum=[]
    while num/2>0:
        bnum.append(num%2)
        num=int(num/2)
    return "".join(str(i) for i in bnum[::-1])

def binary_to_decimal(dec):
    dec_list=list(str(dec))
    output=0
    for i in range(len(dec_list)):
        output+=(2**i)*int(dec_list.pop())
    return(output)

# print(decimal_to_binary(100))
print(binary_to_decimal(10))