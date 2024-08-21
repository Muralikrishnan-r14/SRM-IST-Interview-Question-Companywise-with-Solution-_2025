# Find the missing and repeating elements in the array by using Natural numbers[1,2...N]
# the output array should consist a length of 2 elements [A,B]
# A should be the smallest missing number
# B should be the first repeating number if there is more than one repeating number
# arr=[3,1,3] N=3 output=[2,3]
#Time complexity = O(n) and Space Complexity = O(n)
def missing_repeating(arr, n):
    frq = {}  # O(n) Space complexity for Initialization of frequency map
    output = [-1, -1]
    for i in range(n):
        if arr[i] in frq:
            frq[arr[i]] += 1
        else:
            frq[arr[i]] = 1
    for i in range(n):
        if i+1 not in frq:
            if output[0] == -1:
                output[0] = i+1  # missing number
        elif frq[arr[i]] > 1 and output[1] == -1:
            output[1] = arr[i]  # first repeating number
    return output



arr = [6,1,2,3,4,5,5]
n=len(arr)
print(missing_repeating(arr,n))



