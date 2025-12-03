# Encryption:
#   - Define alphabet (Space + A-Z)
#   - Convert text to integer representative
#   - Compute ciphertext c = m^2 mod n

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SIZE = len(ALPHABET)
CHAR_TO_INT = {c: i for i, c in enumerate(ALPHABET)}
INT_TO_CHAR = {i: c for i, c in enumerate(ALPHABET)}

def validate_plaintext(text):
    # validates that the plaintext only contains characters from the alphabet.
    return all(c.upper() in ALPHABET for c in text)

def text_to_int(text):
    # converts a string to an integer using base-27 encoding.
    text = text.upper()
    if not validate_plaintext(text):
        raise ValueError(f"Plaintext contains invalid characters. Allowed: '{ALPHABET}'")
    
    m = 0
    for char in text:
        m = m * ALPHABET_SIZE + CHAR_TO_INT[char]
    return m

def int_to_text(number):
    # converts an integer back to a string using base-27 encoding.
    if number == 0:
        return ALPHABET[0]
    
    chars = []
    while number > 0:
        number, rem = divmod(number, ALPHABET_SIZE)
        chars.append(INT_TO_CHAR[rem])
    return "".join(reversed(chars))

def encrypt(plaintext, n):
    # encrypts plaintext using public key n.
    # c = m^2 mod n
    m = text_to_int(plaintext)
    
    # ensure message is smaller than n
    if m >= n:
        raise ValueError(f"Plaintext is too long for the current key size. Message value: {m}, n: {n}")
        
    return pow(m, 2, n)