# Que: Given a Square matrix, calculate the absolute difference bw the sums of its diagonal values.

# Square Matrix -> NxN matrix
# Trick -> for finding the diagonal values (left to right diagonal) -> always -> i == j
# (right to left for N=5) -> i = 0 then j = 4 | i = 1 then j = 3 etc..

#  arr is a 2d arrary or NxN matrix

def diagonalDifference(arr):
    n = len(arr)
    rightDiaValues = 0
    leftDiaValues = 0

    for i in range(n):
        rightDiaValues += arr[i][i]
        leftDiaValues += arr[i][n-1-i]
    
    print(f"Order of Matrix: {n}x{n}")
    print(f"sum of right diagonal values {rightDiaValues}")
    print(f"sum of left diagonal values {leftDiaValues}")

    return abs(rightDiaValues - leftDiaValues)


arr1 = [[1,2,3],[4,5,6],[9,8,9]]
print("Absolute difference of sum of diagonal matrix : ", diagonalDifference(arr1))