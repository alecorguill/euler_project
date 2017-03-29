
def sum_square(n):
    return n*(n+1)*(2*n+1)/6.0

def sum_squared(n):
    return (n*(n+1)/2)**2

print(sum_squared(100)-sum_square(100))