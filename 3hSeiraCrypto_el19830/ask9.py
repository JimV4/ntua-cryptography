from primality import primality
import random
import hashlib

def generate_p_q_g():
    p = 4
    i = 42
    r = 1
    # find p, q
    while not primality.isprime(p):
        q = primality.nthprime(i)
        r += 1
        p = q * r + 1
        i += 1
    # find h
    while True:
        h = random.randint(2, p - 1)
        if pow(h, r, p) != 1:
            break
    # find g
    g = pow(h, r, p)
    return p, q, g

def generate_keys(p, q, g):
    sk = random.randint(1, q - 1)
    pk = pow(g, sk, p)
    return pk, sk

def sign(p, q, g, sk, pk, m):
    t = random.randint(1, q - 1)
    T = pow(g, t, p)
    val = bin(T)[2:] + bin(pk)[2:] + m 

    sha256_hash = hashlib.sha256()
    sha256_hash.update(val.encode('utf-8'))
    hashed_value = sha256_hash.digest()
    c = int.from_bytes(hashed_value, byteorder='big') % q

    s = (t + c * sk) % q
    return T, s

def verify(p, q, g, pk, T, s, m):
    val = bin(T)[2:] + bin(pk)[2:] + m 

    sha256_hash = hashlib.sha256()
    sha256_hash.update(val.encode('utf-8'))
    hashed_value = sha256_hash.digest()
    c = int.from_bytes(hashed_value, byteorder='big') % q

    first = pow(g, s, p)
    second = (T * pow(pk, c, p)) % p
    print("g^s = " + str(first))
    print("T * pk^c = " + str(second))
    if first == second:
        print("Message Verified!")
    else:
        print("Oops...Malicious user!")

def program():
    p, q, g = generate_p_q_g()
    pk, sk = generate_keys(p, q, g)
    print("p: " + str(p))
    print("q: " + str(q))
    print("g: " + str(g))
    print("pk: " + str(pk))
    m = input("Give message: ")
    binary_m = ''.join(format(ord(x), '08b') for x in m)
    T, s = sign(p, q, g, sk, pk, binary_m)
    print("Signature (T, s) = (" + str(T) + ", " + str(s) + ")")
    verify(p, q, g, pk, T, s, binary_m)

program()