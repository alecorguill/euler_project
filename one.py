def isnmultiple(x,n):
    if n == 0 or x == 0:
        return False
    return x%n == 0


sum = 0

for i in range(1000):
    if isnmultiple(i,3) or isnmultiple(i,5):
        sum += i

#print(sum)