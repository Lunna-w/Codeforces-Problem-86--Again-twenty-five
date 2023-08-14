def mod_pow(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        
        if exponent % 2 == 1:
            result = (result * base) % mod
        
        base = (base * base) % mod
        exponent //= 2
    return result

n = int(input())
print(f"{mod_pow(5, n, 100):02}")
