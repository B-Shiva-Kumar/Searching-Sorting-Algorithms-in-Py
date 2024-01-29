# find missing number in the given unsorted arr.
# arr = 2 3 2 4 5
# NOTE: * is used to unpack values from list, tupes, set etc..

# Method 1 - using list comprenhensions and sorted function.
def findNum(arr):

    arr = sorted(arr)
    missingEle = [item for item in range(arr[0], arr[-1]+1) if item not in arr]

    return missingEle   

# function call 
arr1 = [2, 1, 4, 1]
print(*findNum(arr1))

arr2 = [1, 3, 2, 5, 5]
print(*findNum(arr2))
# print(sorted(set([2, 1, 4, 1])))

arr3 = [4, 1, 1, 5, 6, 2, 4, 8]
print(*findNum(arr3))

arr4 = [1,2,3,4,5,7,6,9,10]
print(*findNum(arr4))

# output
# 3
# 4
# 3 7
# 8

###########################################################

# Method 2 - using set()

# def missingNum(arr):

#     missingEle = set(range)
arr5 = [1,2,3,4,5,7,6,9,10]
missingEle = set(range(arr5[0], arr5[-1]+1)) - set(arr5)
print(*missingEle)

# output
# 8

