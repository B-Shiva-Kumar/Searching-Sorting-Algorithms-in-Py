lo = 2
hi = 10

output = []

while (lo < hi):
    output.append(lo)
    # print(lo)
    lo += 1
    output.append(hi - 1)
    # print(hi - 1)

print(output)