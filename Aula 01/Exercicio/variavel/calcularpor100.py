def calcularpor100(valor, percentual):
    return (valor * percentual) / 100

valor = float(input("digite o valor total: "))
percentual = float(input("digite a porcentagem: "))

resultado = calcularpor100(valor, percentual)

print(f"{percentual:.0f}% de {valor:.0f} é {resultado:.0f}")
