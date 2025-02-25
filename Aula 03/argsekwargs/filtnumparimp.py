def filter_numbers(*args, parity="even"):
    resultado = []
    for num in args:
        if parity == "even" and num % 2 == 0:
            resultado.append(num)
        elif parity == "odd" and num % 2 != 0:
            resultado.append(num)
    return resultado

numeros = filter_numbers(1, 2, 3, 4, 5, 6, parity="odd")
print("Números ímpares:", numeros)

numeros = filter_numbers(1, 2, 3, 4, 5, 6, parity="even")
print("Números pares:", numeros)
