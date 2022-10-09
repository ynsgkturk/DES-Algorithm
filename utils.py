def permutation(inp, permutation_box, length):
    """
        :param inp:str: value to be permuted
        :param permutation_box:list: permutation value list
        :param length:int: length of the permuted inp

        :return permuted:str: permuted inp
    """
    permuted = ""
    for i in range(0, length):
        permuted = permuted + inp[permutation_box[i] - 1]

    return permuted


def shift_left(key, shift_value):
    """
      :param key:str: The key value that will be shifted
      :param shift_value:int: how much will it be shifted to the left

      :return shifted_key:str: left shifted key value
    """
    return key[shift_value:] + key[0: shift_value]


def xor(value1, value2):
    output = ""
    for idx in range(len(value1)):
        output += str(int(value1[idx] != value2[idx]))

    return output


def ascii2bin(char):
    """
        :param char: character
        :return binary_value:str: binary equal of the char
    """
    ascii_number = ord(char)
    binary_value = bin(ascii_number)
    return binary_value[2:]


def _8bits_binary(binary_value):
    """
        :param binary_value:str
        :return: the 8 bits binary value
    """
    return "0" * (8 - len(binary_value)) + binary_value


def _4bits_binary(binary_value):
    """
        :param binary_value:str
        :return: the 4 bits binary value
    """
    return "0" * (4 - len(binary_value)) + binary_value


def binary2ascii(binary_value):
    if binary_value == "0" * 8:
        return ""
    return chr(int("0b" + binary_value, 2))


def get_binary_message(message):
    """
        :param message: string or text
        :return: binary equal of the message
    """
    binary_message = ""

    for i in message:
        binary = ascii2bin(i)
        binary = _8bits_binary(binary)

        binary_message += binary

    return binary_message


def get_ascii_message(binary):
    message = ""
    for idx in range(0, len(binary), 8):
        char = binary2ascii(binary[idx: idx + 8])
        message += char

    return message
