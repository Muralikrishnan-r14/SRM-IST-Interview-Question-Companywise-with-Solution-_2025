import math
def isqrt(lst):
    n=len(lst)
    cnt=0
    for i in range(n):
        if math.sqrt(lst[i]).is_integer():
            print(lst[i],end=" ")
            cnt += 1
    print()
    return cnt
lst=[1,4,7,99,88,36,64,77,60]
print(isqrt(lst))