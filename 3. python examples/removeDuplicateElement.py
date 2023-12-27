# Python Program to Remove Duplicate Elements from a List

#  duplicate date
data = [10, 10, 20, 30, 40, 45, 45, 50, 60, 65, 65, 70, 80, 90, 90, 95, 95, 100]

# py function to remove duplicate data
def removeDuplicateElement(duplicateData):
    noDuplicateData = []
    for element in duplicateData:
        if element not in noDuplicateData:
            noDuplicateData.append(element)
    
    return noDuplicateData



# calling function
print(removeDuplicateElement(data))


# OUTPUT:
# [10, 20, 30, 40, 45, 50, 60, 65, 70, 80, 90, 95, 100]
