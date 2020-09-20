c = int(input())
n = input()
i = 0
p = ""
for x in range(0, c):
    if p == "":
        p = n[x]   
    elif n[x] == p:
        i += 1
    else:
        p = n[x]
print(i)
    
    
        
        
        
        