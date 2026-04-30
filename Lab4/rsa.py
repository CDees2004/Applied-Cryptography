import sys

def is_prime(num):
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

def factor_n(n):
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            q = n // p
            if is_prime(p) and is_prime(q):
                return p, q

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def generate_e(z):
    values = []
    k = 1

    while True:
        e = (2 ** k) + 1

        if e >= z:
            break

        if gcd(e, z) == 1:
            values.append(e)

        k *= 2
    return values

def mod_inverse(e, z):
    d = 1

    while d < z:
        if (e * d) % z == 1:
            return d
        d += 1

def decrypt_ciphertexts(ciphertexts, d, n):
    message = ""

    for c in ciphertexts:
        m = pow(c, d, n)

        if m < 0 or m > 127:
            raise ValueError()

        message += chr(m)

    return message

def read_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    n = int(lines[0])
    ciphertexts = [int(x.strip()) for x in lines[1].split(",")]
    return n, ciphertexts

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
