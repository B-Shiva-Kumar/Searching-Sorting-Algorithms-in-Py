def binaryToDecimal(strArr):

    decimalSumValues = []

    if (len(strArr) % 4) != 0:
        print("Invalid Input Data")
    else:
        print("Valid Data")

        for i in range(0, len(strArr), 4):
            temp = int(strArr[i:i+4], 2)
            decimalSumValues.append(temp)
            print(f"Binary : {strArr[i:i+4]} to Decimal : {temp}")

    print("Sum of binary to decimal values : ", decimalSumValues)

arr = "110010110011010110000110"
binaryToDecimal(arr)

# output

# Binary : 1100 to Decimal : 12
# Binary : 1011 to Decimal : 11
# Binary : 0011 to Decimal : 3
# Binary : 0101 to Decimal : 5
# Binary : 1000 to Decimal : 8
# Binary : 0110 to Decimal : 6
# Sum of binary to decimal values :  [12, 11, 3, 5, 8, 6]