'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # receives an array of ints [1, 7, 3, 4] arr
    # nested loop
    # check to see if we're on that index in the loop
    # if we're on that index, ignore that index's value (skip) and keep going (increase index)
    # otherwise, multiple all values together and keep going (increase index)
    # insert each answer into a new array
    # returns new array

    # starting point
    outer_loop_index = 0
    output_array = []

    while outer_loop_index < len(arr):
        # loop until you have run the entire size of the array
        # counter for inside loop
        inner_loop_index = 0
        # need this to multiply elements
        mult_num = 1
        # loop over array for each item
        while inner_loop_index < len(arr):
            # if the inside index is the same amount of times as the current index
            if inner_loop_index == outer_loop_index:
                # then increment the inside counter loop by 1
                inner_loop_index += 1
            else:
                # otherwise
                # multiple the items together
                mult_num = mult_num * arr[inner_loop_index]
                # increment the inside counter loop by 1
                inner_loop_index += 1
        # append mult_num to new array
        output_array.append(mult_num)
        # increment index for outer loop by 1
        outer_loop_index += 1
    return output_array


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [
        2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4,
        8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5,
        1, 7, 7, 8
    ]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )
