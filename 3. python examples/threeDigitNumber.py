# ex1
# givenArr = [550, 67, 45, 820, 717, 3, 3, 90, 636]

# arrLen = 8
# n = 2 # nth position
# ans = []

# for i in givenArr:
#     if len(str(i)) in givenArr:
#         ans.append(int(i))
#     else:
#         pass
# print(sorted(ans)[n - 1])

# ---

# ex2
text = "Hello World"
text = text.split(" ")
text = text[0][::-1] + " " + text[1][::-1]
print(text)

# ---

# ex3 - strictly palindrome number - one line code
text = "tx"
print(["Palindrome" if text == text[::-1] else "Not Palindrome"])
