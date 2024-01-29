def reverseAndReplace(text):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    counter = 1

    text = list(text)
    ans = ""

    for i in text:
        if i in vowels:
            ans += str(counter)
            counter += 1
        else:
            ans += i
    print(ans[::-1])




a = "Language"
reverseAndReplace(a)
# output -> 4g32gn1L

