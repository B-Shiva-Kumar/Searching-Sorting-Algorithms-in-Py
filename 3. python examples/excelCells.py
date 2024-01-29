# find number of cells in excel?

excelCell = "B10:F20"

excelCell = excelCell.split(":")
a, b, c, d = excelCell[0][0], excelCell[1][0], int(excelCell[0][1:]), int(excelCell[1][1:])

if (a == b) and (c == d):
    print("Invalid Input")
else:
    num1 = abs(c -d) + 1
    num2 = abs(ord(a) - ord(b)) + 1

    print("number of selected cells : ", num1*num2)