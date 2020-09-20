a = int(input())
b = int(input())
n = int(input())
m = int(input())
sum_1 = n * a + (n - 1)
sum_2 = m * b + (m - 1)
if n <= 1 or m <= 1:
    print(-1)
elif sum_1 > sum_2:
    print(sum_2, sum_1)
else:
    print(sum_1, sum_2)
    
    


        