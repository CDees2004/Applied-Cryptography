# RSA
#
# Team Name: Encryptodes
# Members:Barry Dees, Niko Krause, Javen Wilson,
#         Steven Alleman, and Isiah Hinds.
#
# A program that implements the RSA algorithm 

import sys

# tests if a given input is prime 
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 2
    return True

# factors the input as the product of two prime numbers 
def factor_n(n: int) -> tuple[int, int]:
    # iterating to find two primes between 2 and 2^n + 1
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            q = n // p
            if is_prime(p) and is_prime(q):
                return p, q

# calculates the greatest common divisor of two integers
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# calculates the lowest common multiple of two integers
def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

# generates values of e where 1 < e < z 
# and that are of the form: 2^n + 1
def generate_e(z: int) -> list[int]:
    values = []
    k = 1
    
    # infinite looping until e is GTE z 
    # all combos with gcd 1 are added to e
    while True:
        e = (2 ** k) + 1

        if e >= z:
            break

        if gcd(e, z) == 1:
            values.append(e)

        k *= 2
    return values

# calculates the modular inverse of e such that 
# d = e^-1 (mod z)
def mod_inverse(e: list[int], z: int) -> int:
    d = 1

    while d < z:
        if (e * d) % z == 1:
            return d
        d += 1

# decrypting the ciphertexts with the private key 
def decrypt_ciphertexts(ciphertexts: list[str], d: int, n: int) -> str:
    message = ""

    for c in ciphertexts:
        m = pow(c, d, n)

        if m < 0 or m > 127:
            raise ValueError()

        message += chr(m)

    return message

# utilizing stdin to read user input 
def read_input() -> tuple[int, str]:
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    n = int(lines[0])
    ciphertexts = [int(x.strip()) for x in lines[1].split(",")]
    return n, ciphertexts

### MAIN ###
def main():
    n, ciphertexts = read_input()

    p, q = factor_n(n)
    z = lcm(p - 1, q - 1)

    print(f"p={p}, q={q} n={n} z={z}")

    e_values = generate_e(z)

    for e in e_values:
        try:
            d = mod_inverse(e, z)

            print(f"trying : e={e} d={d}")
            print(f"public key: ({e}, {n})")
            print(f"private key: ({d}, {n})")

            message = decrypt_ciphertexts(ciphertexts, d, n)
            print(message)

        except Exception:
            print("ERROR: invalid plaintext.")

if __name__ == "__main__":
    main()
