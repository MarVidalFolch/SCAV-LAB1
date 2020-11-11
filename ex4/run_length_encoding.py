# LAB 1 - EXERCISE 4: Create a script which contains a function which applies a run-length encoding from a series of
# bytes given.

def run_length_encode():

    data = input("Enter series to encode: ")  # ask to the user to input the series
    encoding = ''  # init encoding string that will be the return of the function 
    prev_char = ''  # init prev_char string used to compare characters
    count = 1  # init the counter to 1

    for char in data:  # start a loop through the input data
        if char != prev_char:  # if the previous and current characters don't match:
            if prev_char:  # if we are not in the first position of the data string
                encoding += str(count) + prev_char  # add the count and the character to our decoding
            count = 1
            prev_char = char  # if we are in the fisrt position of the data string, set char as prev_char
        else:  # if the characters match, increment the counter
            count += 1
    else:  # finish off the encoding
        encoding += str(count) + prev_char  # append to the encoding string the encoded char
        return encoding  

# call the function an print its result
encoded_seq = run_length_encode()
print('Encoded sequence: ', encoded_seq)
