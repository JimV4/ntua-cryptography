import sympy
import random
import time


def generate_s0(p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos):
    n = p * q
    carmichael_n_dia_2 = p_tonos * q_tonos

    while True:
        def find_s0_quadratic_residue(p, q, n):
            # with probability 1 / 4 s0 is quadratic residue mod pq
            s0 = random.randint(1, n - 1)
            while not (pow(s0, (p - 1) // 2, p) == 1 and pow(s0, (q - 1) // 2, q) == 1 and sympy.gcd(s0, n) == 1):
                s0 = random.randint(1, n - 1)
            return s0

        # order of s0 mod N must be λ(N) / 2
        s0 = find_s0_quadratic_residue(p, q, n)

        if pow(s0, carmichael_n_dia_2, n) == 1:
            if not pow(s0, 2, n) == 1 and not pow(s0, p_tonos, n) == 1 and not pow(s0, q_tonos, n) == 1:
                print("Safe Safe p : " + str(p))
                print("Safe Safe q : " + str(q))
                print("Special n : " + str(n))
                print("Seed s0 : " + str(s0))
                return s0
        k += 1

def blum_blum_shub(s0, p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos, iterations):
    print("Theoretically calculated period is π(s0) = λ(λ(n)) = 2p''q'' = " + str(2 * p_tonos_tonos * q_tonos_tonos))
    n = p * q

    first = s0
    second = pow(s0, 2, n)
    third = pow(second, 2, n)
    fourth = pow(third, 2, n)

    first_four_elements = [first, second, third, fourth]
    current = s0
    window = []
    period = 0
    for i in range(1, iterations):
        current = pow(current, 2, n)
        if i > 4:
            window.append(current)
        if len(window) == 4:
            if window == first_four_elements:
                period = i - 3
                break
            else:
                window = window[1:5]

    print("Programmatically calculated period is " + str(period))


def program(p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos, iterations):
    s0 = generate_s0(p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos)
    blum_blum_shub(s0, p, q, p_tonos, q_tonos, p_tonos_tonos, q_tonos_tonos, iterations)
    

program(2879, 359, 1439, 179, 719, 89, 25000000000)
#program(571199, 786959, 285599, 393479, 142799, 196739, 25000000000)