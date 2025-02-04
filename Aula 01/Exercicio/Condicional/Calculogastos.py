def calculogasto(dias, km):
    preco_dia = 50
    preco_km = 0.18
    return (dias * preco_dia) + (km * preco_km)

dias = int(input("quantos dias durou o carro foi alugado? "))
km = float(input("quanto de km percorrido? "))

total = calculogasto(dias, km)

print(f"o total é R$ {total:.2f}")