#%%
# Linear search 

# Linear search is a very simple search algorithm. 
# In this type of search, a sequential search is made over all items one by one. 
# Every item is checked and if a match is found then that particular item is returned, 
# otherwise the search continues till the end of the data collection.


## pseudo code:

# procedure linear_search (list, value)

#    for each item in the list
#       if match item == value
#          return the item's location
#       end if
#    end for

# end procedure
# %%
# python code

def linear_search(array: list):

    usr_num = int(input('Enter number to find : '))
    flag = False

    for indx in range(len(numbers)):
        # if found
        if usr_num == numbers[indx]:
            print(f'Number fount at index number {indx}')
            flag = True
            break

    # if not found
    if flag != True:
        print('Number not found')

#%%

numbers = [12, 43, 55, 21, 42, 88, 10, 67]
linear_search(numbers)