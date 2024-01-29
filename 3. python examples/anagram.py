# what is Anagram?
# a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

def anagram(str1, str2):

    if (sorted(str1) == sorted(str2)):
        print("Anagram : ", sorted(str1))
    else:
        print("Not Anagram")

# user input
str1 = str(input("Enter 1st Word : "))
str2 = str(input("Enter 2nd Word : "))

# function call 
anagram(str1, str2)