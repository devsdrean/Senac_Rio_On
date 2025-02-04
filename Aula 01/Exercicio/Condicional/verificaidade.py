def verificaidade(idade):
    if idade < 16:
        return "Voce e de menor e nao pode votar nem dirigir."
    elif 16 <= idade < 18:
        return "Voce pode votar, mas nao pode dirigir."
    elif 18 <= idade:
        return "Voce pode votar e dirigir."

idade = int(input("Digite sua idade: "))
resultado = verificaidade(idade)

print(resultado)