"This a farmer related sum, but I don't remember the full qn Bcz I'm doing this after a week"
# Our task is to help a farmer by finding the profit for the day . The values are given in the n*n matrix
# profit = sum of middle rows and column in the matrix
# remove zeroes from the row and col sum and reverse it
''' IP = 1 2 2 4 5     
         3 4 20 8 9     OP = sum of 2,20,40,78,90 and 5,0,40,3,7
         3 0 40 3 4     remove Zero from the sum, reverse and return it
         0 7 78 2 9     op = 82
         8 2 90 6 7                     '''
# If is sum means use + or multiply means use *
def farm_grid(mtrx):
    n = len(mtrx)
    mid = n // 2  # To iterate through the middle of the matrice
    r,c = 0,0 # To store the sum or multiples of row and column
    for i in range(n):
        r += mtrx[mid][i]      # if they ask multiples use *= instead of +=
        c += mtrx[i][mid]
    p = r + c
    s = str(p)
    res = ''
    for digit in range(len(s)-1,-1,-1):
        res += s[digit]
    return int(res)      # int by default removes zeroes at the initial pos "082" int(082) is 82
mtrx = [[1,2,2,4,5],[3,4,20,8,9],[3,0,40,3,4],[0,7,78,2,9],[8,2,90,6,7]]
print(farm_grid(mtrx))

