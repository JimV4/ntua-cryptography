import random

def MillerRabin(k, n, r, a):
    b = pow(a, k ,n)
    if b == 1 or b == n - 1:
        return True
    for i in range(0, r - 1):
        b = pow(b, 2, n)
        if b == n - 1:
            return True
    return False

def IsPrime(base, exp, offset):
    n = base ** exp - offset
    if n == 2 or n == 3 or n == 1:
        return True
    
    k = n - 1
    r = 0
    while k % 2 == 0:
        k //= 2
        r += 1
    for i in range(1, 30):
        a = random.randint(2, n - 2)
        if not MillerRabin(k, n, r, a):
            print("Not Prime\n")
            return False
    print("Prime\n")
    return True

""" print("67280421310721 ") 
IsPrime(67280421310721, 1, 0)

print("1701411834604692317316873037158841057 ") 
IsPrime(1701411834604692317316873037158841057, 1, 0)

print("2^1001 - 1 ")
IsPrime(2, 1001, 1)

print("2^2281 - 1 ")
IsPrime(2, 2281, 1)

print("2^9941 - 1 ")
IsPrime(2, 9941, 1) """

print("2^19939 - 1 ")
IsPrime(2, 19939, 1)

