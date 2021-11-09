#%%

# Shell Sorting :

# Shell sort is a highly efficient sorting algorithm.

# Shell sort is a generalized version of the insertion sort algorithm. 
# It first sorts elements that are far apart from each other and 
# successively reduces the interval between the elements to be sorted.

# The interval between the elements is reduced based on the sequence used. 
# Some of the optimal sequences that can be used in the shell sort algorithm are:

# Shell's original sequence: N/2 , N/4 , …, 1
# Knuth's increments: 1, 4, 13, …, (3k – 1) / 2
# Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
# Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…
# Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
# Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....


# Steps :

    # 1: Find the value of the gap by dividing the number of elements by 2.
    # 2: Divide the given array into smaller sub-arrays having equal gap intervals.
    # 3: Using insertion sort, sort the sub-arrays.
    # 4: Repeat steps 1, 2 and 3 until the complete array is sorted.



### Pseudo Code :

        # procedure shellSort()
#    A : array of items 
	
#    /* calculate interval*/
#    while interval < A.length /3 do:
#       interval = interval * 3 + 1	    
#    end while
   
#    while interval > 0 do:

#       for outer = interval; outer < A.length; outer ++ do:

#       /* select value to be inserted */
#       valueToInsert = A[outer]
#       inner = outer;

#          /*shift element towards right*/
#          while inner > interval -1 && A[inner - interval] >= valueToInsert do:
#             A[inner] = A[inner - interval]
#             inner = inner - interval
#          end while

#       /* insert the number at hole position */
#       A[inner] = valueToInsert

#       end for

#    /* calculate interval*/
#    interval = (interval -1) /3;	  

#    end while
   
# end procedure
#%%

### Python Code :

def ss(array):

    n = len(array)
    gap = n // 2

    while gap > 0:
        for rv in range(gap, n):
        
            # temp var
            key = array[rv]
            j = rv

            while j >= gap and array[j - gap] > key:

                array[j] = array[j - gap]
                j -= gap

            array[j] = key
        
        gap //= 2
    
    return print(array)
            
    
### driver code
arr1 = [9, 8, 2, 3, 7, 5, 6, 4, 1]
ss(arr1)