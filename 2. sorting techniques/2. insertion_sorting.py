#%%

## Insertion Sorting Algorithm :

## Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
## Insertion sort works similarly as we sort cards in our hand in a card game.

## explanation : 
## We assume that the first card is already sorted then, we select an unsorted card. 
## If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. 
## In the same way, other unsorted cards are taken and put in their right place.


# pseudo code :

## procedure insertionSort( A : array of items )
#    int holePosition
#    int valueToInsert
	
#    for i = 1 to length(A) inclusive do:
	
#       /* select value to be inserted */
#       valueToInsert = A[i]
#       holePosition = i
      
#       /*locate hole position for the element to be inserted */
		
#       while holePosition > 0 and A[holePosition-1] > valueToInsert do:
#          A[holePosition] = A[holePosition-1]
#          holePosition = holePosition -1
#       end while
		
#       /* insert the number at hole position */
#       A[holePosition] = valueToInsert
      
#    end for
	
# end procedure
#%%

# python code :

def insert_sort(array):

    ## insortion algorithm starts from index 1
    for step in range(1, len(array)):

        key = array[step]
        j = step - 1

        ## we can change `arr[j] > key to arr[j] < key to get in desending order`.
        while j >= 0 and array[j] > key: # ---> comparing the next unsorted list until last

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return print(array)
#%%

# unsorted arrays

arr1 = [32, 31, 56, 12, 78, 31, 24, 66, 54]
insert_sort(arr1)


arr2 = [912, 432, 42, 12, 542, 11, 54, 553]
insert_sort(arr2)