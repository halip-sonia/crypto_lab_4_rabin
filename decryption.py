# Decryption:
#   - compute square root of c modulo p and q
#   - find y_p and y_q such that yp * p + yq * q = 1
#   - find the 4 square roots of c modulo n
#   - decide which message is the correct one


def extended_euclidean(p, q):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = q, p
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    # old_r represents the gcd of p and q, and old_s and old_t represent
    # the coefficients of the identity p * y_p + q * y_q = gcd(p, q)
    # in this context, however, we can assume gcd is 1

    return old_s, old_t


def decrypt(c, p, q, n):
    # we obtain the two square roots using the formula:
    # m_p = (c ^ (1 // 4)(p+1)) mod p
    m_p = pow(c, (p + 1) // 4, p)
    m_q = pow(c, (q + 1) // 4, q)

    y_p, y_q = extended_euclidean(p, q)

    # we obtain the 4 possible methods using the Chinese remainder theorem
    r1 = (y_p * p * m_q + y_q * q * m_p) % n
    r2 = n - r1
    r3 = (y_p * p * m_q - y_q * q * m_p) % n
    r4 = n - r3

    return [r1, r2, r3, r4]

