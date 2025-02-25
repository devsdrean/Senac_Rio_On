def average(numbers):
    soma = 0
    for num in numbers:
        soma = soma + num
    media = soma / len(numbers)
    return media

lista = [10, 20, 30, 40, 50]
resultado = average(lista)

print("A média é:", resultado)
