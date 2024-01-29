firstLne =1
secondLine = 2

maxLines = 5
listPage = [0] * maxLines

listPage[0], listPage[1] = firstLne, secondLine

if (secondLine < firstLne) or (firstLne <= 0) or (secondLine <=0):
    print("Invalid Input")

for i in range(2, maxLines):
    listPage[i] = listPage[i-1] + listPage[i-2]

print(listPage)