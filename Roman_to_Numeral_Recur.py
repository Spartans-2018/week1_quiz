num_rom_pairs = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

def arabic_to_roman(mynum):
    sybflag = None
    for symbol, num in num_rom_pairs.items():
        if num==mynum: return symbol
        if mynum > num:
            sybflag = symbol
    num_remain = mynum - num_rom_pairs[sybflag]
    return sybflag + arabic_to_roman(num_remain)


print(arabic_to_roman(95))





