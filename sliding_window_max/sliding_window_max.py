'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # k is window
    # make a new array to hold temp numbers in window (if k=3, hold array index0, index1, index2)
    # make another array to hold expected output
    # loop (first pass is 1, so ind0, ind1, ind2. 2nd pass is 2, so ind1, ind2, ind3)
    # loop over numbers in window
    # append numbers to window_array
    # sort window array
    # get the last element of the window array (max)
    # append max to expected_output array
    # delete first number of the nums array, so you start on the next window
    # clear the window_array to start fresh on the next loop
    # return expected output array

    window_array = []
    expected_output = []
    while 0 < len(nums) - (k - 1):
        for num in nums[0:k]:
            window_array.append(num)
        # sort window_array in ascending order
        window_array.sort()
        # assign variable max_number to the last elemetn on window_array
        max_number = window_array[k - 1]
        # add max_number to expected_output array
        expected_output.append(max_number)
        # pop the rest of the elements that fall into the first index in a sequence
        nums.pop(0)
        window_array = []
    return expected_output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}"
    )
