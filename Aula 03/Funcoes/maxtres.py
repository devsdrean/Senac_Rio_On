def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

numero1 = 10
numero2 = 25
numero3 = 15
resultado = max_of_three(numero1, numero2, numero3)

print("O maior número é:", resultado)
