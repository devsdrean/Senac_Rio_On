def reverse_string(text):
    inverso = ""
    for letra in text:
        inverso = letra + inverso
    return inverso

palavra = "Andre"
resultado = reverse_string(palavra)

print("String invertida:", resultado)
