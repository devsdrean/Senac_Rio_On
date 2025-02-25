def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = 8
resultado = is_prime(numero)

print("O número é primo?", resultado)
