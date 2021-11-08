#%%

## Seletion sorting algorithm :

# Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, 
# 1. the sorted part at the left end and 
# 2.the unsorted part at the right end. 
# Initially, the sorted part is empty and the unsorted part is the entire list.

# The smallest element is selected from the unsorted array and swapped with the leftmost element, 
# and that element becomes a part of the sorted array.
#  This process continues moving unsorted array boundary by one element to the right.

# This algorithm is not suitable for large data sets.


## Psuedo Code :

# procedure selection sort 
#    list  : array of items
#    n     : size of list

#    for i = 1 to n - 1
#    /* set current element as minimum*/
#       min = i    
  
#       /* check the element to be minimum */

#       for j = i+1 to n 
#          if list[j] < list[min] then
#             min = j;
#          end if
#       end for

#       /* swap the minimum element with the current element*/
#       if indexMin != i  then
#          swap list[min] and list[i]
#       end if
#    end for
	
# end procedure
#%%


def selection_sorting(array : list):

    # traverse through all array elements
    for i in range(len(array)):

        # minimum ind
        min_indx = i

        ## traverse through unsorted array
        for j in range(i + 1, len(array)):

            # arr[1] < arr[0]...
            # checking min number
            if array[min_indx] > array[j]:
                ## high value > low value
                ## array[j] > array[i] gives decesending order of an array

                ## swapping
                array[min_indx], array[j] = array[j], array[min_indx]
                
    return print(array)
#%%

## unsorted array
arr1 = [64, 25, 12, 22, 11, 98]
selection_sorting(arr1)

arr2 = [912, 432, 42, 12, 542, 11, 54, 553]
selection_sorting(arr2)