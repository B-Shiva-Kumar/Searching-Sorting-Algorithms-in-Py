# Shallow Copy
# A shallow copy creates a new object which stores the reference of the original elements.

# Deep Copy
# A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

# difference bw copy vs deepcopy
# Shallow Copy reflects changes made to the new/copied object in the original object. 
# Deep copy doesn't reflect changes made to the new/copied object in the original object.

# ---
# copy example 

import copy

list1 = [1, 2, 3, 4]
list2 = copy.copy(list1)

print(list1)
print(list2)

# check Ids OR references:
list1IDs = [id(i) for i in list1]
list2IDs = [id(i) for i in list2]

print("IDs of list1 contents : ", list1IDs)
print("IDs of list2 contents : ", list2IDs)


# ---
# Deep Copy example

list3 = copy.deepcopy(list1)
list3[1] = 1
list3IDs = [id(i) for i in list3]
print(list1)
print(list3)
print("IDs of list1 contents : ", list1IDs)
print("IDs of list3 contents : ", list3IDs)

# reference: https://www.programiz.com/python-programming/shallow-deep-copy