'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=None):
    print(n)
    # Your code here
    # base case:
    # this represents there being a number of cookies were we can just take
    #that many cookies
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check the cache to see if the asnwer is stored in there
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            #init an empty cache
            cache = {i: 0 for i in range(n + 1)}
    # store answers in our cache
    cache[n] = eating_cookies(n - 1, cache) + eating_cookies(
        n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]


# this implementation does not efficiently scales because of its branching nature,
# the run time is O(3^)

# print(eating_cookies(20))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 1

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
