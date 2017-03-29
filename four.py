def is_palindrome(n):
    return str(n) == str(n)[::-1]

max = 0
for i in range(1000):
    for j in range(1000):
        if is_palindrome(i*j) and i*j > max :
            max = i*j

#print(max)