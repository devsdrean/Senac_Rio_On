def sum_all(*args):
    soma = 0
    for num in args:
        soma = soma + num
    return soma

resultado = sum_all(1, 2, 3, 4, 5)
print("A soma é:", resultado)
