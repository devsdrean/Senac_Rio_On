def word_count(sentence):
    palavras = sentence.split()
    return len(palavras)

frase = "Estudo no Rio on"
resultado = word_count(frase)

print("Quantidade de palavras:", resultado)
