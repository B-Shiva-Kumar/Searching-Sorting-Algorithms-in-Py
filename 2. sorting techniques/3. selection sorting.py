#%%

## Seletion sorting algorithm :

# Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, 
# 1. The Selection sort algorithm divides the given list into two halves 
# where the first half will be the sorted list and the second is an unsorted list. 
# At first, the sorted list is empty and all elements to be sorted are present in the unsorted list.

# 2. The Selection sort algorithm will look at all the elements present in the unsorted list, 
# pick up the item that is supposed to come first, and then places it in the sorted list.
# It then repeats the searching process and 
# places the next element to the right of the first element in the sorted list.

### Steps :

        # 1. Make the first element as the minimum and compare it with the next element. 
        # If the next element is less than the selected element, mark that as the minimum and 
        # compare it with the next element. Repeat the same process until you compare all the elements of the unsorted list.

        # 2. Place the minimum in the sorted array (This becomes the first element of the sorted array).

        # 3. Increment the position of the counter to point at the first element of the unsorted array and 
        # repeat steps 1 and 2 for all the elements of the unsorted array.

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
            if array[j] < array[min_indx]:
                ## high value > low value
                ## array[j] > array[i] gives decesending order of an array

                # set minimum index to j
                min_indx = j
                

            ## swapping
        array[min_indx], array[i] = array[i], array[min_indx]
                
    return print(array)
#%%

## unsorted array
arr1 = [64, 25, 12, 22, 11, 98]
selection_sorting(arr1)

arr2 = [912, 432, 42, 12, 542, 11, 54, 553]
selection_sorting(arr2)