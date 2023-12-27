# Palindrome Program in Python

def isPalindrome():

    while True:

        data = input("Enter the value (0 to STOP) : ")
        reverseData = data[::-1]

        if (data == str(0)):
            print("STOPPED")
            break

        if (data == reverseData):
            print("Yes, it is a Palindrome.")
        else:
            print("No, it is not a Palindrome.")


# function call
isPalindrome()