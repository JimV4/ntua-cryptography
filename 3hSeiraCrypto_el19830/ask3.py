import rsa

def rsa_encrypt(e, m, n):
    return pow(m, e, n)

def oracle(d, c, n):
    m = pow(c, d, n)
    location = 0
    if m % n > (n // 2):
        location = 1
    else:
        location = 0
    return location

def attack(e, d, c, n):
    low = 0
    high = n
    prev_high = high
    prev_low = low
    location = oracle(d, c, n)
    i = 1
    while low <= high:
        if location == 0:
            prev_high = high 
            high = high - (n // (2 ** i)) 
        
        elif location == 1:
            prev_low = low
            low = low + (n // (2 ** i)) 

        location = oracle(d, c * rsa_encrypt(e, 2 ** i, n), n)
        i += 1
        if (prev_high == high and prev_low == low):
            break

    for m in range(low, high):
        if c == pow(m, e, n):
            print("Message generated from the attack: " + str(m)) 
            break
    
def program():
    keys = rsa.newkeys(128)
    n = keys[0].n
    e = keys[0].e
    d = keys[1].d
    print("n = " + str(n) + "\n" + "e = " + str(e) + "\n" + "d = " + str(d) + "\n")
    m = int(input("Give Message: "))
    print("Original Message: " + str(m))
    c = rsa_encrypt(e, m, n)
    attack(e, d, c, n)

program()