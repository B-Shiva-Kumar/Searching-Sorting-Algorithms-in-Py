# Python Program to Count Each Vowel Present in a String Entered by the User

# Without function

user_input_string = input("Enter a String: ")
user_input_string = user_input_string.casefold()


# vowels
vowels = "aeiou"

# initiaize vowelsData
vowelsData = {}.fromkeys(vowels, 0)
totalVowelsCount = 0

for character in user_input_string:
    if character in vowels:
        vowelsData[character] += 1
        totalVowelsCount += 1

for vowel in vowelsData:
    print(vowel, " => ", vowelsData[vowel])

print("Total Vowel Count: ", totalVowelsCount)


# -------------------------------------------------------

# With function/def

# def checkVowelsCount(userInputString):
#     # vowels
#     vowels = "aeiou"

#     # initiaize vowelsData
#     vowelsData = {}.fromkeys(vowels, 0)
#     totalVowelsCount = 0

#     for character in userInputString:
#         if character in vowels:
#             vowelsData[character] += 1
#             totalVowelsCount += 1

#     return vowelsData, totalVowelsCount


# # calling function

# user_input_string = input("Enter a String: ")
# user_input_string = user_input_string.casefold()

# print(checkVowelsCount(user_input_string))