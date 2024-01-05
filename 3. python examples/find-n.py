# 1
# numbers = [n, n-1, n-2,...,1]
# s = sum(numbers)
# c = len(numbers)

# for i in range(0, len(numbers), 2):
#     s -= numbers.pop()
# print(s, numbers)

# ANS: The answer is depnedent on n and the time of complexity of code is O(n).

# ---

# 2
# def  my_func(n):
#     if n<= 0:
#         return False
#     return (n & (n-1)) == 0

# n = 18

# if __name__ == "__main__":
#     print(my_func(n))

# ANS: FALSE

# ---    

# 3
# def my_func(s, z):
#     total = 0
#     len_str = len(s)

#     for x, y in z:
#         if x == 0:
#             total += y
#         else:
#             total -= y
#     total = total % len_str
#     print(s[total:] + s[:total])

# s = "cutshort"
# z = [[0, 3], [1, 11]]

# if __name__ == "__main__":
#     print(my_func(s, z))

# ANS: cutshort
    
# ---
    
