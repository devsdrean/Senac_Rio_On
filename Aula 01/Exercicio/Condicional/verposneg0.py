def verposnegzero(numero):
    if numero > 0:
        return "o numero e positivo"
    elif numero < 0:
        return "numero negativo"
    else:
        return "numero e zero"
    
numero = float(input("digite um numero"))
resultado = verposnegzero(numero)

print (resultado)