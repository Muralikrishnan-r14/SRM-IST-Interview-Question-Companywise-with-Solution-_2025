# Find the missing and repeating elements in the array by using Natural numbers[1,2...N]
# the output array should consist a length of 2 elements [A,B]
# A should be the smallest missing number
# B should be the first repeating number if there is more than one repeating number
# arr=[3,1,3] N=3 output=[2,3]
def missing_repeating(arr, n):
    output = [-1,-1]
    seen = set(arr)
    for i in range(n):
        if arr[i] in seen:
            output[1]=arr[i]
            break
    for i in range(n):
        if i+1 in seen:
            pass
        else:
            output[0]=i+1
            break
    return output

arr = [6,6,1,2,3,4,5,5]
n=len(arr)
print(missing_repeating(arr,n))



