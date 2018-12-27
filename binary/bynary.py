# Step 1 | #Write a method that takes binary numbers and outputs a base 10 number.
def binary_to_decimal__OLD(binary):
    number = 0
    index = 0
    for element in binary:
        number = number + int(element)*2**(len(binary) - index - 1)
        index = index + 1

    return number


def binary_to_decimal(binary):
    number = 0
    index = 0
    power_of_2 = 1

    length = len(binary)
    for i in range(0, length):
        digit = int(binary[length-i-1])
        number = number + power_of_2 * digit

        power_of_2 = power_of_2 * 2
        index = index + 1

    return number


# Step 2 | Write a method that takes decimal numbers and returns it in binary notation.

def decimal_to_binary(number):
    binary = ""

    while (number >= 1):
        if (number % 2 == 0):
            binary = "0" + binary
            number = number//2
        elif (number % 2 == 1):
            binary = "1" + binary
            number = number//2
        else:
            print("check the number")

    return binary


# print(binary_to_decimal(1011)) #== returns 11)
input_num = 12
binary = decimal_to_binary(input_num)
reversed_num = binary_to_decimal(binary)

assert reversed_num == input_num  # == returns 11)

# print(decimal_to_binary(12)) #==  1100)
