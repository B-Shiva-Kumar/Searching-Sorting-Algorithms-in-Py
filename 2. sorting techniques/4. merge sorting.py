#%%

### Merge sort algorithm :

# Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

# worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.

# Here, a problem is divided into multiple sub-problems. 
# Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

### Steps :

        # 1. if two unsorted arrays are given to merge sort, it performs sorting.
        # 2. if one arr unsorted array is given, it divides into recursively until it can no more divided.
        # 3. merge the smaller lists into new list in sorted order.


## Pseudo Code :

# # procedure mergesort( var a as array )
# #    if ( n == 1 ) return a

# #    var l1 as array = a[0] ... a[n/2]
# #    var l2 as array = a[n/2+1] ... a[n]

# #    l1 = mergesort( l1 )
# #    l2 = mergesort( l2 )

# #    return merge( l1, l2 )
# # end procedure

# # procedure merge( var a as array, var b as array )

# #    var c as array
# #    while ( a and b have elements )
# #       if ( a[0] > b[0] )
# #          add b[0] to the end of c
# #          remove b[0] from b
# #       else
# #          add a[0] to the end of c
# #          remove a[0] from a
# #       end if
# #    end while
   
# #    while ( a has elements )
# #       add a[0] to the end of c
# #       remove a[0] from a
#    end while
   
#    while ( b has elements )
#       add b[0] to the end of c
#       remove b[0] from b
#    end while
   
#    return c
	
# end procedure
#%%

### Python Code :

def merge_sort(arr):
     
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)


    merge_two_sorted_lists(left, right, arr)


## merged 2 - sorted lists 
def merge_two_sorted_lists(a, b, arr):

    len_a = len(a)
    len_b = len(b)

    i = j = k = 0   ## k --> sorted list.

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k +=1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


# if __name__ == '__main__':

a = [12, 3, 50, 11, 43, 15, 98, 6, 13]
# b = [12, 23, 44, 50]

# merge_two_sorted_lists(a, b)
# print(merge_sort(a))
merge_sort(a)
print(a)
#%%

# -----> time complexity = O(nlogn).
# -----> Divide & Conquer rule.