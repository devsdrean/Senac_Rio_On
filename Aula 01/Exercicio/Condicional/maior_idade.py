def verificarmaioridade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
    
idade = int(input("Digite sua idade: "))
resultado = verificarmaioridade(idade)

print(f"Você tem {idade} anos e é {resultado}.")