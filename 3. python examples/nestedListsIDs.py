# ref => https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/

# part-1
nestedLists1 = [[]] * 5
print(nestedLists1)

for objects in nestedLists1:
    print(id(objects))


# part-2
nestedLists2 = [[] for i in range(5)]
print(nestedLists2)

for objects in nestedLists2:
    print(id(objects))



# part-3
nestedLists3 = [[], [], [], [], []]
print(nestedLists3)
for i in nestedLists3:
    print(id(i))

    