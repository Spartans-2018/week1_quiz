def to_hex_string(num):
    hexo_list = "0123456789ABCDEF"
    hexo_char = ""
    if (num < len(hexo_list)):
        hexo_char = hexo_list[num]
    else:
        print("number out of range(0,15)")

    return hexo_char


def to_hex(decimal):
    return to_any(decimal, 16)


def to_binary(decimal):
    return to_any(decimal, 2)


def to_any(decimal, new_base):
    remainder = 0
    result = [decimal % new_base]
    decimal = decimal // new_base

    while(decimal >= new_base):
        remainder = decimal % new_base
        result.insert(0, remainder)
        decimal = decimal // new_base

    result.insert(0, decimal)

    return result


def print_hex(digits):
    result = ""

    for digit in digits:
        result = result + to_hex_string(digit)

    return result


# testing
assert (print_hex(to_binary(12)) == "1100"), "binary convertion error"
assert (print_hex(to_hex(16)) == "10"), "this is an exception"  # should return 10
assert (print_hex(to_hex(65536)) == "10000")  # should return 10
assert (print_hex(to_hex(15)) == "0F")
