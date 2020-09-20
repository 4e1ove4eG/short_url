def CountZero(x):
    s = bin(x)
    s = str(s)
    count = 0
    for j in s[2:]:
        if j == "0":
            count += 1
    return count
#40^n - 8^n - 2^n = K2
n = 2
while CountZero(64**n - 8**n - 2**n) != 7:
    n += 1
print(n) 
    

