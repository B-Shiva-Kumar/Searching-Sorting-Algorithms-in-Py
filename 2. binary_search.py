## Binary Search algorithm 

## Binary search is a fast search algorithm. 
# This search algorithm works on the principle of divide and conquer. 
# For this algorithm to work properly, the data collection should be in the sorted form.

##  `https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm`

## formula :1.  mid = first + last //2
        # or
 #         2. mid = first + (last - first) // 2

## pseudo code :


# Procedure binary_search
#    A ← sorted array
#    n ← size of array
#    x ← value to be searched

#    Set lowerBound = 1
#    Set upperBound = n 

#    while x not found
#       if upperBound < lowerBound 
#          EXIT: x does not exists.
   
#       set midPoint = lowerBound + ( upperBound - lowerBound ) / 2
      
#       if A[midPoint] < x
#          set lowerBound = midPoint + 1
         
#       if A[midPoint] > x
#          set upperBound = midPoint - 1 

#       if A[midPoint] = x 
#          EXIT: x found at location midPoint
#    end while
   
# end procedure


## python code :


numbers = [10, 14, 18, 23, 55, 65, 78, 99]

usr_num = int(input('Enter number to find :'))

def binary_search(numbers: list, usr_num: int):

    first = 0
    mid = 0
    last = len(numbers) - 1

    while first <= last:
        
        mid = (first + last) // 2

        if numbers[mid] < usr_num:
            first = mid + 1
        elif numbers[mid] > usr_num:
            last = mid - 1
        else:
            return mid
    return -1


result = binary_search(numbers, usr_num)

if result != -1:
    print(f'Number is found at index {result}')
else:
    print('Number not found')