'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # loop through array:
    # if num is != 0, then move to the left
    # if num is == 0, then insert to the end of the array
    # hold the moved nums to an output_array
    # return the output_array
    i = 0
    output_array = []
    while i < len(arr):
        num = arr[i]
        if num == 0:
            # if num is 0 then we insert num to the end of the array
            # by using the total length of the array as the index
            output_array.insert(len(arr), num)
        else:
            # else we insert none-0 value to the begining of the array
            # order of none-0 does not matter
            output_array.insert(0, num)
        i += 1
    return output_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
