'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#
# def single_number(arr):
# Your code here
# for num in arr:  # O(n)
#     if arr.count(num) == 1:  # O(n)
#         return num


# O(n) This is using a *Set*
def single_number(arr):
    # sets are a closely-related cousing to dicts
    # they don't associate values with keys
    # they're useful for when you need the uniqueness
    # property of dics
    s = set()

    for num in arr:  # O(n)
        if num in s:  #O(1)
            s.remove(num)  # O(1)
        else:
            s.add(num)  # O(1)
    # at this point, the only element in the set
    # is our odd-element-out
    return list(s)[0]  # O(1)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")