#!/usr/bin/python3
""" UTF-8 Module """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    def is_starting_byte(byte):
        """ Helper function to check if a byte is a valid starting byte """
        return (byte >> 6) != 0b10

    def bytes_to_expect(starting_byte):
        """ Number of bytes to expect for a given starting byte """
        if starting_byte & 0b10000000 == 0:
            return 1
        elif starting_byte & 0b11100000 == 0b11000000:
            return 2
        elif starting_byte & 0b11110000 == 0b11100000:
            return 3
        elif starting_byte & 0b11111000 == 0b11110000:
            return 4
        else:
            return 0

    # Iterate through the data
    i = 0
    while i < len(data):
        starting_byte = data[i]

        # Check if the starting byte is a valid one
        if not is_starting_byte(starting_byte):
            return False

        # Determine the number of bytes to expect for this character
        num_bytes = bytes_to_expect(starting_byte)

        # Check if the number of bytes is valid
        if num_bytes == 0:
            return False

        # Check if there are enough bytes left in the data
        if i + num_bytes > len(data):
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            if not (data[i + j] >> 6) == 0b10:
                return False

        i += num_bytes

    return True
