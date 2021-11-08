#%%
## bubble sorting :

## Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. 
## This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
## This algorithm is not suitable for large data sets as its average.


## pseudo code

# procedure bubbleSort( list : array of items )

#    loop = list.count;
   
#    for i = 0 to loop-1 do:
#       swapped = false
		
#       for j = 0 to loop-1 do:
      
#          /* compare the adjacent elements */   
#          if list[j] > list[j+1] then
#             /* swap them */
#             swap( list[j], list[j+1] )		 
#             swapped = true
#          end if
         
#       end for
      
#       /*if no number was swapped that means 
#       array is sorted now, break the loop.*/
      
#       if(not swapped) then
#          break
#       end if
      
#    end for
   
# end procedure return list
#%%



### python code

def bubble_sort(array : list):

    ## iterating row
    for i in range(len(array) - 1):
        
        ## iterating col for each value 
        ## - i is used for excluding the sorted element
        for j in range(len(array) - i - 1):

            # comparing adjacent values
            if array[j] > array[j+1]:

                # temp var
                # temp = array[j + 1]
                # array[j+1] = array[j]
                # array[j] = temp

                # or 

                # easy swapping
                array[j], array[j + 1] = array[j + 1], array[j]

    return print(array)

#%%

### unsorted array 

arr  = [12, 43, 11, 2, 56, 77, 34, 89, 67, 80]
bubble_sort(arr)

arr1 = [556, 32, 654, 223, 89, 11, 96, 123]
bubble_sort(arr1)