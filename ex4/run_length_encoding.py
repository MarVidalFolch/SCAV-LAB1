# LAB 1 - EXERCISE 4: Create a script which contains a function which applies a run-length encoding from a series of
# bytes given.

def run_length_encode():

    data = input("Enter series to encode: ")
    encoding = ''
    prev_char = ''
    count = 1

    for char in data:
        if char != prev_char:  # if the previous and current characters don't match:
            if prev_char:
                encoding += str(count) + prev_char  # add the count and the character to our decoding
            count = 1
            prev_char = char
        else:  # if the characters match, increment the counter
            count += 1
    else:  # finish off the encoding
        encoding += str(count) + prev_char
        return encoding


encoded_seq = run_length_encode()
print('Encoded sequence: ', encoded_seq)
