# LAB 1 - EXERCISE 1: Start a script and create a translator from 3 values in RGB into the 3 YUV values,
# plus the opposite operation.

def rgb_to_yuv():
    # ask the user to input the parameters:
    r = int(input('Enter R value: '))
    g = int(input('Enter G value: '))
    b = int(input('Enter B value: '))
    # apply the mathematical formula to convert RGB to YUV:
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    cb = -0.148 * r - 0.291 * g + 0.439 * b + 128
    cr = 0.439 * r - 0.368 * g - 0.071 * b + 128
    print('RGB: ', r, g, b, '-> YUV: ', y, cb, cr)  # print the results
    return y, cb, cr  # return the results


def yuv_to_rgb():
    # ask the user to input the parameters:
    y = int(input('Enter Y value: '))
    cb = int(input('Enter Cb value: '))
    cr = int(input('Enter Cr value: '))
    # apply the mathematical formula to convert YUV to RGB
    b = 1.164 * (y - 16) + 2.018 * (cb - 128)
    g = 1.164 * (y - 16) - 0.813 * (cr - 128) - 0.391 * (cb - 128)
    r = 1.164 * (y - 16) + 1.596 * (cr - 128)
    print('YUV: ', y, cb, cr, '-> RGB: ', r, g, b)  # print the results
    return r, g, b  # return the results

# create a menu for the user to choose between the two options.
option = input('Enter a number: \n"1" for converting rgb to yuv. \n"2" for converting yuv to rgb. \nYour selection: ')
if option == "1":
    rgb_to_yuv()
elif option == "2":
    yuv_to_rgb()
