def factorial(n):
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1
    return resultado

numero = 5
resultado = factorial(numero)

print("O fatorial é:", resultado)
