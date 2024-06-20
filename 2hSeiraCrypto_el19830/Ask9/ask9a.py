import sympy
import random

def generate_s0(p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos):
    n = p * q
    carmichael_n_dia_2 = p_tonos * q_tonos

    def find_s0_quadratic_residue(p, q, n):
        # with probability 1 / 4 s0 is quadratic residue mod pq
        s0 = random.randint(1, n - 1)

        # check if s0 is indeed a quadratic residue. if not choose another s0
        while not (pow(s0, (p - 1) // 2, p) == 1 and pow(s0, (q - 1) // 2, q) == 1 and sympy.gcd(s0, n) == 1):
            s0 = random.randint(1, n - 1)
        return s0
        
    while True:
        s0 = find_s0_quadratic_residue(p, q, n)

        # order of s0 mod N must be λ(N) / 2
        if pow(s0, carmichael_n_dia_2, n) == 1:
            if not pow(s0, 2, n) == 1 and not pow(s0, p_tonos, n) == 1 and not pow(s0, q_tonos, n) == 1:
                return s0

def program(p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos):
    n = p * q
    s0 = generate_s0(p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos)
    print("Safe Safe p : " + str(p))
    print("Safe Safe q : " + str(q))
    print("Special n : " + str(n))
    print("Seed s0 : " + str(s0))

program(571199, 786959, 285599, 393479, 142799, 196739)