import one

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def largest_factor(n):
    max = 0
    for i in range(1,int(n**0.5)+1):
        if one.isnmultiple(n,i) and is_prime(i):
            max = i
    return max
#print(largest_factor(600851475143))