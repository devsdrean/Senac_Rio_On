def count_vowels(word):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in word:
        if letra in vogais:
            contador = contador + 1
    return contador

palavra = "banana"
resultado = count_vowels(palavra)

print("Quantidade de vogais:", resultado)
