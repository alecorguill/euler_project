import one

def divsible_pfirst(n,p):
    for i in range(1,p+1):
        if not one.isnmultiple(n,i):
            return False
    return True

res = 12252240

while not divsible_pfirst(res,10):
    res += 1

#print(res)
