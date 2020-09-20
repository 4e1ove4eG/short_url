n = int(input())
a = []
for i in range(n):
    x = int(input())
    flag = False
    for i in range(0, len(a)):
        if x >= a[i]:
            a.insert(i, x)
            flag = True
            break
    if flag == False:
        a.append(x)
ans_k = 0
ans_s = 0
max_p = 0
for i in range(len(a)):
    p = a[i] * (i + 1)
    if p > max_p:
        max_p = p
        ans_s = a[i]
        ans_k = i + 1
print(ans_k, ans_s)
