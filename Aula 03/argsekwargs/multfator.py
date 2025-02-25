def multiply_all(*args):
    produto = 1
    for num in args:
        produto = produto * num
    return produto

resultado = multiply_all(1, 2, 3, 4)
print("O produto é:", resultado)
