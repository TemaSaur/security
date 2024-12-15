import random
import math


RANDOM_E = False


def is_prime(x: int):
    if x < 2:
        return False
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True


def get_prime(bit_length: int):
    p = 0
    while not is_prime(p):
        p = random.getrandbits(bit_length)
        # ensure length, not even
        p |= (1 << bit_length - 1) | 1
    return p


def get_e(phi: int):
    if not RANDOM_E:
        return 65537
    while True:
        e = random.randint(3, phi - 1)
        if math.gcd(e, phi) == 1:
            return e


def generate_keys(bit_length: int):
    p = q = get_prime(bit_length)
    while p == q:
        q = get_prime(bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    d = pow(e, -1, phi)

    return (e, n), (d, n)


def encrypt(public_key: (int, int), message: str):
    e, n = public_key

    bin_message = int.from_bytes(message.encode('utf-8'))

    return pow(bin_message, e, n)


def decrypt(private_key: (int, int), encoded: int):
    d, n = private_key
    bin_message = pow(encoded, d, n)
    byte_length = (bin_message.bit_length() + 7) // 8
    return bin_message.to_bytes(byte_length).decode('utf-8')


if __name__ == "__main__":
    bit_length = 16
    public_key, private_key = generate_keys(bit_length)

    message = 'Hi'
    encrypted = encrypt(public_key, message)
    decrypted = decrypt(private_key, encrypted)
    print(f'original: {message}')
    print(f'encrypted: {encrypted}')
    print(f'decrypted: {decrypted}')
