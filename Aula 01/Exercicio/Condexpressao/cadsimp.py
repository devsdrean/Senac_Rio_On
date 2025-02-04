idade = int(input("digite sua idade: "))
renda = float(input("digite sua renda mensal: $ "))

if idade > 18 or renda > 3000:
    print("cadastro permitido")
else:
    print("cadastro nao permitido")