# Key generation:
#   - compute private key (p, q)
#   - compute public key n = p * q
import random


# generate private key (2 blum primes p and q of the same size)
def generate_private_key(bit_length=512):
    p = generate_blum_prime(bit_length // 2)
    q = generate_blum_prime(bit_length // 2)
    return p, q


# a blum prime represents a prime number which fulfills the condition n = 3 mod 4
def generate_blum_prime(bit_length):
    while True:
        p = random.getrandbits(bit_length)
        if is_prime(p) and p % 4 == 3:
            return p


def repeated_squaring_exponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


# testing primality using the Miller-Rabin test
def is_prime(n, k=100):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        seq = repeated_squaring_exponentiation(a, t, n)
        if seq == 1 or seq == n - 1:
            continue
        for _ in range(s - 1):
            seq = repeated_squaring_exponentiation(seq, 2, n)
            if seq == n - 1:
                break
        else:
            return False

    return True


# compute public key n = p * q
def generate_public_key(p, q):
    return p * q


# p, q = generate_private_key()
# n = generate_public_key(p, q)
