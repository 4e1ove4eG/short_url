def Seven2Dec(s):
    l = len(s)
    r = 0
    for j in (s):
        r += int(j) * (7 ** (l - 1))
        l -=  1
        print(r)
    return str(r)
        

        

x = input()
c = "34" + x + "2"
y = Seven2Dec(c)
print(x + ","  + y[2])