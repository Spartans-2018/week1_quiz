# dict_lookup = {1000:"M",900:"CM",500:"D",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4: "IV",1:"I"}
numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def arabic_to_roman(mynum):
    result = []
    for i in range(len(numbers)):
        count = int(mynum / numbers[i])
        result.append(romans[i] * count)
        mynum -= numbers[i] * count
    return ''.join(result)

print(arabic_to_roman(1))
