#The problem you're describing involves creating the largest possible number with n digits
# such that the sum of its digits equals s.
# Given n = 3 and s = 20, the largest number that can be formed is 992
def largestpossible(n,s):
    # if sum is 0 we need at least one digit it's impossible to form
    if s == 0:
        if n == 1:
            return "0"
        else:
            return "-1"
    # if sum is too large to be represented with n digits
    if s > 9 * n:
        return '-1'
    # empty list to store the output
    result = []
    # Iterate through each element
    for i in range(n):
        # finding the maximum digit we can place at that place
        for digit in range(9, -1, -1):
            if s >= digit and (n - i - 1)*9 >= s - digit:
                result.append(str(digit))
                s -= digit
                break
    return ''.join(result)
s,n = 20, 3
print(largestpossible(n,s))
# Time complexity
""" The outer loop runs O(n) times
    This inner loop can run up to 10 times, but on average, it will break early, 
    reducing the number of iterations. However, in the worst case 10 iterations"""
# the total time complexity is O(10 * n), which simplifies to O(n) , n is number of digits in resulting number
# space complexity O(n), n is number of digits in resulting number








