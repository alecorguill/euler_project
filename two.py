p = 1
n = 2
res = 2
while n < 4000000:
    temp = p
    p = n
    n = temp + p
    if n%2 == 0:
        res += n
#print(res)