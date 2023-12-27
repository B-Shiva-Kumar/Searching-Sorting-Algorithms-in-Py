# To Convert Distance from Kilometer to Mile

while True:

    try:
        kmValue = float(input("Enter the Distance in Kilometers (0 to STOP) : "))
        mileValue = (kmValue * 0.621371)
        print("%.2f kilometer = %.2f miles" %(kmValue, mileValue))

        if (int(kmValue) == 0):
            print("STOPPED")
            break

    except ValueError as err:
        print("ValueError: ", err)